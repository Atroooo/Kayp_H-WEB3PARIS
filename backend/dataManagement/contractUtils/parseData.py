from dataManagement.models import billOfLading, Shipper, Consignee, Cargo, VesselDetails

def parseData(data):
    bill = billOfLading.objects.create(billOfLadingNumber = data["billOfLadingNumber"], termsOfDelivery = data["termsOfDelivery"], \
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

def hashData(data):
    pass
