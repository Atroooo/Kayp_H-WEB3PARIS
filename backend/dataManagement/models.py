from django.db import models

# Create your models here.
class Shipper(models.Model):
    name = models.CharField(max_length = 100, default="default")
    address = models.CharField(max_length = 200, default = "default")
    contact = models.CharField(max_length = 200, default = "default")

class Consignee(models.Model):
    name = models.CharField(max_length = 100, default="default")
    address = models.CharField(max_length = 200, default = "default")
    contact = models.CharField(max_length = 200, default = "default")

class Cargo(models.Model):
    description = models.CharField(max_length = 2000, default = "empty")
    quantity = models.IntegerField(default = 0)
    weight = models.FloatField(default = 0.0)
    volume = models.FloatField(default = 0.0)
    value = models.CharField(max_length = 300, default = "0$")

class VesselDetails(models.Model):
    name = models.CharField(max_length = 100, default = "default")
    loadingPort = models.CharField(max_length = 200, default = "default")
    destinationPort = models.CharField(max_length = 200, default = "default")
    dateOfLoading = models.DateTimeField(auto_now_add=True)

class BillOfLading(models.Model):
    shipper = models.OneToOneField(Shipper, on_delete=models.CASCADE, blank=True, null=True)
    consignee = models.OneToOneField(Consignee, on_delete=models.CASCADE, blank=True, null=True)
    cargo = models.OneToOneField(Cargo, on_delete=models.CASCADE, blank=True, null=True)
    billOfLadingNumber = models.CharField(max_length = 100, default = "default")
    termsOfDelivery = models.CharField(max_length = 2000, default = "default")
    vesselDetails = models.OneToOneField(VesselDetails, on_delete=models.CASCADE, blank=True, null=True)
    carrierSignature = models.CharField(max_length = 2000, default = "default")
    specialInstructions = models.CharField(max_length = 2000, default = "default")
    contractAddress = models.CharField(max_length = 100, default = "default")
    state = models.CharField(max_length = 100, default = "in progress")