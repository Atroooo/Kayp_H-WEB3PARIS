from ..models import BillOfLading, Shipper, Consignee, Cargo, VesselDetails

import hashlib

def parseData(data):
    bill = BillOfLading.objects.create(billOfLadingNumber = data["billOfLadingNumber"], termsOfDelivery = data["termsOfDelivery"], \
                                carrierSignature = data["carrierSignature"], specialInstruction = data["specialInstructions"])
    shipperData = data["shipper"]
    bill.shipper.set(Shipper.objects.create(name = shipperData["name"], address = shipperData["address"], contact = shipperData["contact"]))

    consigneeData = data["consignee"]
    bill.consignee.set(Consignee.objects.create(name = consigneeData["name"], address = consigneeData["address"], contact = consigneeData["contact"]))

    cargoData = data['cargo']
    bill.cargo.set(Cargo.objects.create(description = cargoData["description"], quantity = cargoData["quantity"], weight = cargoData["weight"], volume = cargoData["volume"], value = cargoData["value"]))

    vesselDetailsData = data["vesselDetails"]
    bill.vesselDetails.set(VesselDetails.objects.create(name = vesselDetailsData["name"], loadingPort = vesselDetailsData["loadingPort"], destinationPort = vesselDetailsData["destinationPort"], dateOfLoading = vesselDetailsData["dateOfLoading"]))

    bill.save()
    return (bill)

def hash_value(value):
  """Hashes a value using SHA-256 and returns the hexdigest."""
  m = hashlib.sha256()
  m.update(str(value).encode())  # Convert to string and encode for hashing
  return m.hexdigest()

def hashData(data2):
    data = {
    "shipper": {
        "name": "Acme Widgets Inc.",
        "address": "123 Main Street, Anytown",
        "contact": "555-1212"
    },
    "consignee": {
        "name": "Gadget Emporium",
        "address": "456 Elm Street, Springfield",
        "contact": "555-5555"
    },
    "cargo": {
        "description": "100 boxes of widgets",
        "quantity": 100,
        "weight": 500,
        "volume": 2,  
        "value": 10000
    },
    "billOfLadingNumber": "BL-12345",
    "termsOfDelivery": "FOB (Free on Board)",
    "vesselDetails": {
        "name": "MV Ever Given",
        "loadingPort": "Los Angeles",
        "destinationPort": "Singapore",
        "dateOfLoading": "2024-03-24" 
    },
    "carrierSignature": "John Smith (Captain)",
    "specialInstructions": "Handle with care. Keep dry."
    }

    m = hashlib.sha256()
    mainHash = m.hexdigest(data)

    hashedData = {}
    for key, value in data.items():
        if isinstance(value, dict):
            hashed_value = {}
            for subkey, subvalue in value.items():
                hashed_value[str(key + '.' + subkey)] = hash_value(subvalue)
            hashedData[key] = hashed_value
        else:
            hashedData[key] = hash_value(value)

    print(hashedData)

hashData(None)