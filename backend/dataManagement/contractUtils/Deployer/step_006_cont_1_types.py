import smartpy as sp

tstorage = sp.record(id = sp.nat, stored_part_hashes = sp.map(sp.string, sp.bytes), stored_whole_hash = sp.bytes).layout(("id", ("stored_part_hashes", "stored_whole_hash")))
tparameter = sp.variant(storeHash = sp.bytes, storePartHashes = sp.map(sp.string, sp.bytes)).layout(("storeHash", "storePartHashes"))
tprivates = { }
tviews = { }
