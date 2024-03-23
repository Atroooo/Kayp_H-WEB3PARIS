import smartpy as sp

@sp.module
def main():
    class HashStorage(sp.Contract):
        def __init__(self, id):
            self.data.id = id
            self.data.stored_whole_hash = sp.bytes("0x")
            self.data.stored_part_hashes = sp.cast(
                {},
                sp.map[sp.string, sp.bytes]
            )

        @sp.entrypoint
        def storeHash(self, whole_hash):
            self.data.stored_whole_hash = whole_hash

        @sp.entrypoint
        def storePartHashes(self, part_hashes):
            for item in part_hashes.items():
                self.data.stored_part_hashes[item.key] = item.value

    class Deployer(sp.Contract):
        def __init__(self):
            self.data.contracts = sp.cast(
                {},
                sp.map[sp.nat, sp.address]
            )

        @sp.entrypoint
        def CreateContract(self, id, whole_hash, part_hashes):
            if self.data.contracts.contains(id):
                old_contract_address = self.data.contracts[id]

                contract_instance_whole = sp.contract(
                    sp.bytes,
                    old_contract_address,
                    "storeHash"
                ).unwrap_some(error="Didn't find contract")

                sp.transfer(
                    whole_hash,
                    sp.tez(0),
                    contract_instance_whole
                )

                contract_instance_part = sp.contract(
                    sp.map[sp.string, sp.bytes],
                    old_contract_address,
                    "storePartHashes"
                ).unwrap_some(error="Didn't find contract")

                sp.transfer(
                    part_hashes,
                    sp.tez(0),
                    contract_instance_part
                )
            else:
                new_contract_address = sp.create_contract(
                                        HashStorage,
                                        None,
                                        sp.tez(0),
                                        sp.record(
                                            id = id,
                                            stored_whole_hash = whole_hash,
                                            stored_part_hashes = part_hashes
                                            )
                                        )
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
    whole_hash1 = sp.keccak(sp.pack("a little test"))
    whole_hash2 = sp.keccak(sp.pack(12345))
    whole_hash3 = sp.keccak(sp.pack("ddddd"))
    whole_hash4 = sp.keccak(sp.pack("Lucas Compiegne"))
    dict1 = {
        "key1": sp.keccak(sp.pack("value hashed 1")),
        "key2": sp.keccak(sp.pack("value hashed 2")),
        "key3": sp.keccak(sp.pack("value hashed 3")),
        "key4": sp.keccak(sp.pack("value hashed 4")),
    }

    dict2 = {
        "name": sp.keccak(sp.pack(12345)),
        "age": sp.keccak(sp.pack(";lkgja")),
        "cargo-ono": sp.keccak(sp.pack(6789))
    }
    scenario.h2("First hash for id 1")
    FactoryContract.CreateContract(id=id1, whole_hash=whole_hash1, part_hashes=dict1)
    scenario.h2("Second hash for id 1")
    FactoryContract.CreateContract(id=id1, whole_hash=whole_hash2, part_hashes=dict2)