from django.contrib.auth.models import User
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
from .tokens import account_activation_token

import requests
from django.http import JsonResponse
import json
import os



def add_api_profile_picture(profile, profile_data, username):
    image_url = profile_data.get("image")
    image_url = image_url.get("link")
    # Get the image from the url
    img_temp = NamedTemporaryFile(delete=True)
    img_temp.write(urlopen(image_url).read())
    img_temp.flush()
    profile.profile_picture.save(f"{username}_profile_picture.jpg", File(img_temp))

def request_error():
    error_message = "Invalid request method."
    return JsonResponse({"error": error_message}, status=405)


def set_data(authorization_code, page):
    return {
        "grant_type": "authorization_code",
        # "client_id": os.environ.get("CLIENT_ID"),
        # "client_secret": os.environ.get("CLIENT_SECRET"),
        "client_id": "u-s4t2ud-2eb7a58d446ca29b150cc2840610be46c0af8353337ee8df58d31ada274426b4",
        "client_secret": "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",
        "code": authorization_code,
        "redirect_uri": f"https://127.0.0.1:8443/42auth/{page}",
        # "redirect_uri": f"https://127.0.0.1:3000/42auth/{page}",
    }


def make_token_exchange(post_data):
    authorization_code = post_data.get("code")
    page = post_data.get("page")
    data = set_data(authorization_code, page)
    return requests.post("https://api.intra.42.fr/oauth/token", data=data)


def success_request(token_response):
    response_data = token_response.json()
    access_token = response_data.get("access_token")
    return JsonResponse({"access_token": access_token}, status=200)


def check_if_email_unique(email):
    if User.objects.filter(email=email).exists():
        return "Email is not unique"
    return False


def send_activate_email(request, user, to_email):
    mail_subject = "Activate your user account."
    message = (
        f"Hi {user.username},\n\n"
        f"Please go to the following link to activate your account:\n\n"
        f"{request.scheme}://{get_current_site(request).domain}/authentification/activate_account/"
        f"{urlsafe_base64_encode(force_bytes(user.pk))}/{account_activation_token.make_token(user)}/\n\n"
        "Thanks for registering!"
    )
    email = EmailMessage(mail_subject, message, to=[to_email])
    return email.send()

def send_forgot_password_email(request, user, to_email):
    mail_subject = "Activate your user account."
    message = (
        f"Hi {user.username},\n\n"
        f"Please go to the following link to change your password:\n\n"
        # f"https://127.0.0.1:3000/reset-password/"
        f"https://localhost:8443/reset-password/"
        f"{urlsafe_base64_encode(force_bytes(user.pk))}/{account_activation_token.make_token(user)}/\n\n"    )
    email = EmailMessage(mail_subject, message, to=[to_email])
    return email.send()

def get_profile_data(post_data):
    authorization_code = post_data.get("access_token")
    if authorization_code is None:
        return None
    access_token = f"Bearer {authorization_code}"
    profile_data = requests.get(
        "https://api.intra.42.fr/v2/me",
        headers={"Authorization": access_token},
    )
    return None if profile_data is None else profile_data.json()

def check_if_preset_picture(path_image):
    if path_image.endswith("authentification/images/profile_pictures/bear.png") \
        or path_image.endswith("authentification/images/profile_pictures/chicken.png") \
        or path_image.endswith("authentification/images/profile_pictures/dog.png") \
        or path_image.endswith("authentification/images/profile_pictures/fox.png") \
        or path_image.endswith("authentification/images/profile_pictures/koala.png") \
        or path_image.endswith("authentification/images/profile_pictures/meerkat.png") \
        or path_image.endswith("authentification/images/profile_pictures/panda.png") \
        or path_image.endswith("authentification/images/profile_pictures/rabbit.png"):
        return True
    return False
