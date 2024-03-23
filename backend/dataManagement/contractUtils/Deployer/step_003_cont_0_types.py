import smartpy as sp

tstorage = sp.record(contracts = sp.map(sp.nat, sp.address)).layout("contracts")
tparameter = sp.variant(CreateContract = sp.record(id = sp.nat, part_hashes = sp.map(sp.string, sp.bytes), whole_hash = sp.bytes).layout(("id", ("part_hashes", "whole_hash")))).layout("CreateContract")
tprivates = { }
tviews = { }
