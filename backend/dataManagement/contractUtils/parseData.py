from dataManagement.models import BillOfLading, Shipper, Consignee, Cargo, VesselDetails

import hashlib

def parseData(data):
    """
    Fill the model Bill of lading with the data entered by the user

    Parameters
    ----------
    arg1 : JSON
        data in JSON format

    Returns
    -------
    billOfLading object
        bill of lading object model
    """

    shipperData = data["shipper"]
    shipperObj = Shipper.objects.create(name = shipperData["name"], address = shipperData["address"])

    consigneeData = data["consignee"]
    consigneeObj = Consignee.objects.create(name = consigneeData["name"], address = consigneeData["address"])
    
    cargoData = data['cargo']
    cargoObj = Cargo.objects.create(description = cargoData["description"], value = cargoData["value"])

    vesselDetailsData = data["vesselDetails"]
    vessel = VesselDetails.objects.create(loadingPort = vesselDetailsData["loadingPort"], destinationPort = vesselDetailsData["destinationPort"])
    
    bill = BillOfLading.objects.create(billOfLadingNumber = "10", shipper = shipperObj, consignee = consigneeObj, cargo = cargoObj, vesselDetails = vessel)
    bill.save()
    return (bill)

def hash_value(value):
  """
    Hashes a value using SHA-256 and returns the hexdigest.
  
    Parameters
    ----------
    arg1 : int, str
        data that need to be hashed

    Returns
    -------
    str
        hashed data
  """
  m = hashlib.sha256()
  m.update(str(value).encode())
  return m.hexdigest()

def hashData(data):
    """
    Hash the eBL document that will be store in the smart contract.

    Parameters
    ----------
    arg1 : JSON
       data in JSON format

    Returns
    -------
    str, map
        return the contract hashed and every part of the contract hashed in a map
    """
    mainHash = hash_value(data)

    hashedData = {}
    for key, value in data.items():
        if isinstance(value, dict):
            hashed_value = {}
            for subkey, subvalue in value.items():
                hashed_value[str(key + '.' + subkey)] = hash_value(subvalue)
            hashedData[key] = hashed_value
        else:
            hashedData[key] = hash_value(value)

    return mainHash, hashedData