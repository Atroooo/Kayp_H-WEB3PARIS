# from pytezos import pytezos
# from pytezos import ContractInterface

# from dataManagement.models import models, BillOfLading

# key = "edskS2w2qaNik7bepNQi1MinJ52ratUHUJzbnyumdLJMcfGBH9U3p8yjk3Gs1Lh84iSNNfXTbNLkEvekpYB5FTnqAFezNF4jkk"
# pytezosWallet = pytezos.using(key=key)



# def deployContract(bill):
#     """
#     Deploy and save the hash of the smart contract
#     Parameters
#     ----------
#     arg1 : billOfLanding object
#         bill of landing model

#     Returns
#     -------
#     str
#         contract's hash
#     """
#     global key, pytezosWallet

#     contract = ContractInterface.from_file('deployerContract.tz')
#     ci = contract.using(key=key)

#     value = pytezosWallet.origination(script=ci.script()).send(min_confirmations=1)
#     bill.contactHash = value
#     bill.save()
#     return value.opg_hash



# def checkIfContractIsActive(billOfLadingID):
#     """
#     Check if the billOfLading is already existing or not
#     Parameters
#     ----------
#     arg1 : string
#         bill of lading ID

#     Returns
#     -------
#     str
#         return contract hash if contract is finded
#     """
#     billOfLadingList = models.BillOfLading.objects.all()
#     for billOfLading in billOfLadingList:
#         if billOfLading.billOfLadingNumber == billOfLadingID:
#             return billOfLading.contractHash
#     return None



# def fillContract(contractHash):
#     """
#     Fill the smart contract with the hashes
    
#     Parameters
#     ----------
#     arg1 : str
#         contract's hash

#     """
#     global key, pytezosWallet


