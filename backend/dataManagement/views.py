from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from .viewUtils import getClient, getContractList
from .contractUtils import parseData, deployContract

# Create your views here.
class manageContract(View):

    def get(self, request):
        client = getClient(request.client)
        contracts = getContractList(client)
        return JsonResponse({'contracts': contracts}, status = 200)

    def post(self, request):
        parseData.parseData(request)
        contractHash = deployContract.deployContract()
        hashedData = parseData.getHashedData(request)
        deployContract.fillContract(contractHash, hashedData)
        return JsonResponse({"message": "success"}, status = 200)

    def on_delete(self, request):
        pass

