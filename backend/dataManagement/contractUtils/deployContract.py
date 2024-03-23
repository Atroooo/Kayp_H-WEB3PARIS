from pytezos import pytezos
from pytezos import ContractInterface

def deployContract():
    key = "edskS2w2qaNik7bepNQi1MinJ52ratUHUJzbnyumdLJMcfGBH9U3p8yjk3Gs1Lh84iSNNfXTbNLkEvekpYB5FTnqAFezNF4jkk"
    pytezosWallet = pytezos.using(key=key)

    contract = ContractInterface.from_file('step_003_cont_0_contract.tz')
    ci = contract.using(key=key)

    value = pytezosWallet.origination(script=ci.script()).send(min_confirmations=1)
    return value.opg_hash
