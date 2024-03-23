from dataManagement.models import models
from django.forms.models import model_to_dict

from dataManagement.models import billOfLading, Shipper, Consignee, Cargo, VesselDetails

def getClient(clientName):
    shippers = models.Shipper.objects.all()
    client = None
    for shipper in shippers:
        if shipper.name == clientName:
            return shipper
        
def getContractList(client):
    contracts = models.billOfLading.objects.all()
    contract_list = []
    for contract in contracts:
        if (client == contract.shipper):
            contract_list.append(contract)
    return contract_list

def convert_matchs_to_dict(contracts):
    dictContractList = []
    for contract in contracts:
        dict_match['shipper'] = model_to_dict(contract.shipper, \
                                              fields=['name', 'address', 'contact'])
        dict_match['consignee'] = model_to_dict(contract.consignee, \
                                                fields=['name', 'address', 'contact'])
        dict_match['cargo'] = model_to_dict(contract.cargo, \
                                            fields=['description', 'quantity', 'weight', 'volume', 'value'])
        dict_match = model_to_dict(contract, \
                                fields=['billOfLadingNumber', 'termsOfDelivery', \
                                        'carrierSignature', 'specialInstructions'])
        dict_match['vesselDetails'] = model_to_dict(contract.vesselDetails, \
                                                    fields=['name', 'loadingPort', 'destinationPort', 'dateOfLoading'])
        dictContractList.append(dict_match)
    return dictContractList