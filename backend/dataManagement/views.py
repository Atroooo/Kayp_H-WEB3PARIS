from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from .viewUtils.viewUtils import getClient, getContractList
from .contractUtils import parseData, deployContract

import json

# Create your views here.
class manageContract(View):

    def get(self, request):
        client = getClient(request.user)
        contracts = getContractList(client)
        return JsonResponse({'contracts': contracts}, status = 200)

    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf8'))
        except json.JSONDecodeError:
            return JsonResponse(data={'errors': "Invalid JSON format"}, status=400)
        bill = parseData.parseData(data)
        mainHash, hashedData = parseData.hashData(data)
        contractAddress = deployContract.checkIfContractIsActive(bill.billOfLadingNumber)
        if (contractAddress is not None):
            deployContract.fillContract(contractAddress, bill.billOfLadingNumber, mainHash, hashedData)
        else:
            contractAddress = deployContract.deployContract(bill)
            deployContract.fillContract(contractAddress, bill.billOfLadingNumber, mainHash, hashedData)

        return JsonResponse({"message": "success"}, status = 200)

    def on_delete(self, request):
        pass

