from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import logout, authenticate, get_user_model, login
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_http_methods
import json
from .tokens import account_activation_token
from .tasks import delete_account_if_not_activate
from .viewsUtils import (
    send_activate_email,
)

@require_http_methods(["GET"])
def activate_account(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, "activation_success.html", status = 200)
    return render(request, "activation_failed.html", status=400)

@require_http_methods(["POST"])
def register_user(request):
    try:
        data = json.loads(request.body.decode('utf8'))
    except json.JSONDecodeError:
        return JsonResponse(data={'errors': "Invalid JSON format"}, status=400)
    userData = data.get("userData", {})
    form = UserCreationForm(userData)
    if not form.is_valid():
        return JsonResponse({"errors": form.errors}, status=400)
    user = form.save(commit=False)
    user.is_active = False
    user.save()
    if send_activate_email(request, user, userData["username"]) == False:
        return JsonResponse({"error": "error sending email"}, status=400)
    delete_account_if_not_activate.apply_async(args=[user.id], countdown=3600)
    return JsonResponse({"status": "success"}, status=200)


# LOGIN / LOGOUT

@require_http_methods(["POST"])
def login_user(request):
    try:
        data = json.loads(request.body.decode('utf8'))
    except json.JSONDecodeError:
        return JsonResponse(data={'errors': "Invalid JSON format"}, status=400)
    email = data.get("email")
    password = data.get("password")
    if (email == "") or (email is None) \
        or (password == "") or (password is None):
        return JsonResponse(
            {"errors": "Missing username or password"}, status=400
        )
    user = authenticate(request, username=email, password=password)
    if user is None:
        return JsonResponse(
            {"errors": "Wrong username or password"}, status=400
        )
    login(request, user)
    return JsonResponse({"status": "success"}, status=200)


@require_http_methods(["GET"])
def logout_user(request):
    logout(request)
    return JsonResponse({"status": "success"}, status=200)



# @require_http_methods(["PUT"])
# def forgot_password(request):
#     try:
#         body = json.loads(request.body.decode('utf8'))
#     except json.JSONDecodeError:
#         return JsonResponse(data={'errors': "Invalid JSON format"}, status=400)
#     email = body.get('username')
#     try:
#         user = User.objects.get(email=email)
#     except User.DoesNotExist:
#         return JsonResponse({"error": "User with this email does not exist"}, status=400)
#     send_forgot_password_email(request, user, email)
#     return JsonResponse({"status": "success"}, status=200)


# @require_http_methods(["POST"])
# def reset_password(request, uidb64, token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is None or not reset_password_token.check_token(user, token):
#         return JsonResponse({'error':"Invalid reset link"}, status=400)
#     try:
#         body = json.loads(request.body.decode('utf8'))
#         new_password = body.get('new_password')
#     except json.JSONDecodeError:
#         return JsonResponse(data={'errors': "Invalid JSON format"}, status=400)
#     user.set_password(new_password)
#     user.save()
#     return JsonResponse({"status": "success"}, status=200)

# @login_required
# @require_http_methods(["PUT"])
# def change_password(request):
#     try:
#         data = json.loads(request.body.decode('utf8'))
#     except json.JSONDecodeError:
#         return JsonResponse(data={'errors': "Invalid JSON format"}, status=400)
#     old_password = data.get("old_password")
#     new_password = data.get("new_password")
#     user = authenticate(request, username=request.user.username, password=old_password)
#     if user is None:
#         return JsonResponse({"errors": "Wrong password"}, status=400)
#     user.set_password(new_password)
#     user.save()
#     return JsonResponse({"status": "success"}, status=200)


# CSRF
@require_http_methods(["GET"])
@ensure_csrf_cookie
def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({"csrfToken": token}, status=200)
