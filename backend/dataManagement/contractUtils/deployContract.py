from pytezos import pytezos
from pytezos import ContractInterface

# from dataManagement.models import models, BillOfLading

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
    # bill.contactHash = value
    # bill.save()
    print(value)
    return value.opg_hash

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
            return billOfLading.contractHash
    return None



def fillContract(contractHash, contractID, mainHash, hashedData):
    """
    Fill the smart contract with the hashes
    
    Parameters
    ----------
    arg1 : str
        contract's hash
    arg2 : str
        contract's ID
    arg3 :  str
        data hashed
    arg4 : map
        every data field hashed

    """
    builder = pytezos.contract(contractHash)

    mainHash = str(mainHash).encode('utf-8')
    hashedDataEncoded = dict()
    for key, value in hashedData.items():
        hashedDataEncoded[key] = str(value).encode('utf-8')

    opg = pytezos.bulk(builder.CreateContract(contractID, hashedDataEncoded, mainHash)).send(min_confirmations=1)


# test = dict()
# test["test"] = str("gregregre1")
# test["cc"] = str("etrefsdfs")
# fillContract("KT1MvGPyXNvNNwEAc286Xtw9Xgv5B5vBFHg3", 23, "lalla", test)