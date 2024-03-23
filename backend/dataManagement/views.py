from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from viewUtils import getClient, getContractList
from .contractUtils import parseData, deployContract, fillContract

# Create your views here.
class manageContract(View):

    def get(self, request):
        client = getClient(request.client)
        contracts = getContractList(client)
        return JsonResponse({'contracts': contracts}, status=200)

    def post(self, request):
        parseData(request)
        hash = deployContract()
        print(request)

    def on_delete(self, request):
        pass

