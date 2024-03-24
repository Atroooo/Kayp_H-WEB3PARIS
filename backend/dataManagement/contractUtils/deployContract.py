from pytezos import pytezos
from pytezos import ContractInterface
from pytezos.operation.result import OperationResult

from dataManagement.models import models, BillOfLading

key = "edskS2w2qaNik7bepNQi1MinJ52ratUHUJzbnyumdLJMcfGBH9U3p8yjk3Gs1Lh84iSNNfXTbNLkEvekpYB5FTnqAFezNF4jkk"
pytezosWallet = pytezos.using(key=key)


def deployContract(bill):
    """
    Deploy and save the hash of the smart contract
    Parameters
    ----------
    arg1 : billOfLanding object
        bill of landing model

    Returns
    -------
    str
        contract's hash
    """
    global key, pytezosWallet

    contract = ContractInterface.from_file('deployerContract.tz')
    ci = contract.using(key=key)

    value = pytezosWallet.origination(script=ci.script()).send(min_confirmations=1)
    opg = pytezos.shell.blocks[value.branch:].find_operation(value.opg_hash)

    contract_address = opg["contents"][0]["metadata"]["operation_result"]["originated_contracts"][0]
    bill.contractAddress = contract_address
    bill.save()

    return contract_address

deployContract(None)


def checkIfContractIsActive(billOfLadingID):
    """
    Check if the billOfLading is already existing or not
    Parameters
    ----------
    arg1 : string
        bill of lading ID

    Returns
    -------
    str
        return contract hash if contract is finded
    """
    billOfLadingList = models.BillOfLading.objects.all()
    for billOfLading in billOfLadingList:
        if billOfLading.billOfLadingNumber == billOfLadingID:
            return billOfLading.contractAddress
    return None



def fillContract(contractAddress, contractID, mainHash, hashedData):
    """
    Fill the smart contract with the hashes
    
    Parameters
    ----------
    arg1 : str
        contract address
    arg2 : str
        contract's ID
    arg3 :  str
        data hashed
    arg4 : map
        every data field hashed

    """
    builder = pytezos.contract(contractAddress)

    mainHash = str(mainHash).encode('utf-8')
    hashedDataEncoded = dict()
    for key, value in hashedData.items():
        hashedDataEncoded[key] = str(value).encode('utf-8')

    opg = pytezos.bulk(builder.CreateContract(contractID, hashedDataEncoded, mainHash)).send(min_confirmations=1)