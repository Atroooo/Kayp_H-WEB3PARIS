from dataManagement.models import models
from django.forms.models import model_to_dict

from dataManagement import models

def getClient(clientName):
    shippers = models.Shipper.objects.all()
    for shipper in shippers:
        if shipper.name == clientName:
            return shipper
        
def getContractList(client):
    contracts = models.BillOfLading.objects.all()
    contract_list = []
    for contract in contracts:
        if (client == contract.shipper):
            contract_list.append(contract)
    return contract_list

def convert_matchs_to_dict(contracts):
    dictContractList = []
    for contract in contracts:
        dict_ebl['shipper'] = model_to_dict(contract.shipper, \
                                              fields=['name', 'address', 'contact'])
        dict_ebl['consignee'] = model_to_dict(contract.consignee, \
                                                fields=['name', 'address', 'contact'])
        dict_ebl['cargo'] = model_to_dict(contract.cargo, \
                                            fields=['description', 'quantity', 'weight', 'volume', 'value'])
        dict_ebl = model_to_dict(contract, \
                                fields=['billOfLadingNumber', 'termsOfDelivery', \
                                        'carrierSignature', 'specialInstructions'])
        dict_ebl['vesselDetails'] = model_to_dict(contract.vesselDetails, \
                                                    fields=['name', 'loadingPort', 'destinationPort', 'dateOfLoading'])
        dict_ebl = model_to_dict(contract, \
                                fields=['contractAddress', 'state'])
        dictContractList.append(dict_ebl)
    return dictContractList