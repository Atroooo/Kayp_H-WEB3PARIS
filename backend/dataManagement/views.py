from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from .viewUtils.viewUtils import getClient, getContractList
from .contractUtils import parseData, deployContract

# Create your views here.
class manageContract(View):

    def get(self, request):
        client = getClient(request.client)
        contracts = getContractList(client)
        return JsonResponse({'contracts': contracts}, status = 200)

    def post(self, request):
        bill = parseData.parseData(request)
        mainHash, hashedData = parseData.getHashedData(request)
        contractHash = deployContract.checkIfContractIsActive(request)
        if (contractHash is not None):
            deployContract.fillContract(contractHash, mainHash, hashedData)
        else:
            contractHash = deployContract.deployContract(bill)
            deployContract.fillContract(contractHash, mainHash, hashedData)

        return JsonResponse({"message": "success"}, status = 200)

    def on_delete(self, request):
        pass

