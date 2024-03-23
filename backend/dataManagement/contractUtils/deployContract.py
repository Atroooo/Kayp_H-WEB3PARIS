from pytezos import pytezos
from pytezos import ContractInterface

key = "edskS2w2qaNik7bepNQi1MinJ52ratUHUJzbnyumdLJMcfGBH9U3p8yjk3Gs1Lh84iSNNfXTbNLkEvekpYB5FTnqAFezNF4jkk"
pytezosWallet = pytezos.using(key=key)


def deployContract(bill):
    global key, pytezosWallet

    contract = ContractInterface.from_file('deployerContract.tz')
    ci = contract.using(key=key)

    value = pytezosWallet.origination(script=ci.script()).send(min_confirmations=1)
    bill.contactHash = value
    bill.save()
    return value.opg_hash


def fillContract(contractHash):
    global key, pytezosWallet


