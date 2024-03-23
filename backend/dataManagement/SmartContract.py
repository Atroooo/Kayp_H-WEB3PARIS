import smartpy as sp

@sp.module
def main():
    class HashStorage(sp.Contract):
        def __init__(self, id, new_hash):
            self.data.id = id
            self.data.stored_hash = new_hash

        @sp.entrypoint
        def storeHash(self, new_hash):
            self.data.stored_hash = new_hash

    class Deployer(sp.Contract):
        def __init__(self):
            self.data.contracts = sp.cast(
                sp.big_map(),
                sp.big_map[sp.nat, sp.address],
            )

        @sp.entrypoint
        def CreateContract(self, id, new_hash):
            if self.data.contracts.contains(id):
                old_contract_address = self.data.contracts[id]
                contract_instance = sp.contract(sp.bytes, old_contract_address, "storeHash").unwrap_some(error="Didn't find contract")
                sp.transfer(new_hash, sp.tez(0), contract_instance)
            else:
                new_contract_address = sp.create_contract(HashStorage,
                                       None,
                                      sp.tez(0),
                                      sp.record(id = id,
                                                stored_hash = new_hash))
                self.data.contracts[id] = new_contract_address

@sp.add_test()
def test():
    scenario = sp.test_scenario("Deployer", main)
    scenario.h1("Factory Contract")
    scenario.h2("Make the factory contract")
    FactoryContract = main.Deployer()
    scenario += FactoryContract

    scenario.p("Create hashes and Ids to test")
    id1 = 1
    id2 = 2
    id3 = 3
    hash1 = sp.keccak(sp.pack("a little test"))
    hash2 = sp.keccak(sp.pack(12345))
    hash3 = sp.keccak(sp.pack("ddddd"))
    hash4 = sp.keccak(sp.pack("Lucas Compiegne"))

    scenario.h2("First hash for id 1")
    FactoryContract.CreateContract(sp.record(id=id1, new_hash=hash1))

    scenario.h2("First hash for id 2")
    FactoryContract.CreateContract(sp.record(id=id2, new_hash=hash2))

    scenario.h2("Second hash for id 1")
    FactoryContract.CreateContract(sp.record(id=id1, new_hash=hash3))

    scenario.h2("First hash for id 3")
    FactoryContract.CreateContract(sp.record(id=id3, new_hash=hash4))

    scenario.h2("third hash for id 1")
    FactoryContract.CreateContract(sp.record(id=id1, new_hash=hash4))