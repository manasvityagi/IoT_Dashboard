import datetime

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.functions import datetime
from django.utils import timezone
from django.utils.timezone import now
from django.utils.deconstruct import deconstructible


@deconstructible
class Address(models.Model):
    street = models.CharField(max_length=150, default="38 Windsor")
    zip = models.CharField(max_length=10, default="06001")

    def __str__(self):
        return str(self.street)


class Manufacturer(models.Model):
    name = models.CharField(max_length=150, default='generic manufacturer')
    # One Manufacturer can have one address, and one address can have only one manufacturer
    address = models.OneToOneField(Address, on_delete=models.DO_NOTHING)
    is_certified = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=14, default='0000')

    def __str__(self):
        return str(self.name)


# You can only create a Thing from DevicesAvailable
class DeviceModels(models.Model):
    name = models.CharField(max_length=50, default='generic device')
    max_life = models.PositiveIntegerField()
    warranty_days = models.PositiveIntegerField()
    image = models.ImageField(default='default.jpg', upload_to='device_catalogue')
    energy_rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    safety_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    current_consumption = models.IntegerField()
    mfg = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING)
    model_number = models.CharField(max_length=50)
    # Todo Serial Number should be removed from DeviceMode,
    #  as serial number is not associated with a model, but for each unit
    serial_number = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Home(models.Model):
    # many to one relationship, since many houses can belong to a single owner
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default=Address())

    def __str__(self):
        return str(self.address)


class ServiceProvider(models.Model):
    name = models.CharField(max_length=150, default='generic manufacturer')
    # One Manufacturer can have one address, and one address can have only one manufacturer
    address = models.OneToOneField(Address, on_delete=models.DO_NOTHING)
    phone_number = models.CharField(max_length=14, default='0000')
    type_of_device_handled = models.ManyToManyField(DeviceModels)

    def __str__(self):
        return str(self.name)


class Seller(models.Model):
    name = models.CharField(max_length=150, default='generic seller')
    # One Seller can have many addresses, but one address can only belong to one seller
    # Hence one to many relationship, deletion of the address should Ideally be protected when one of the seller
    # is already in business
    address = models.OneToOneField(Address, on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=14, default='0000')
    type_of_device_sold = models.ManyToManyField(DeviceModels)

    def __str__(self):
        return str(self.name)


# a time series database model
class ValueStream(models.Model):
    description = models.CharField(max_length=150, default='value stream description')
    property_name = models.CharField(max_length=25, default='default roperty name')
    value = models.FloatField(default=0.0)
    ts = models.DateTimeField(auto_now_add=True)


class Thing(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    description = models.CharField(max_length=150, default='my smart coffee machine')
    # Many to one, because, many devices can have one model type
    device_model_info = models.ForeignKey(DeviceModels, on_delete=models.DO_NOTHING)
    # many to one relationship, since many houses can belong to a single owner
    # on deletion of the Home, Thing should be destroyed
    installed_home_id = models.ManyToManyField(Home)
    purchase_date = models.DateField()
    # in hours, in case you bought it second hand, or replaced with used item
    life_used = models.IntegerField()
    # one value stream id will contain same device's data
    value_stream_id = models.ManyToManyField(ValueStream)

    def is_purchased_recently(self):
        return now - datetime.timedelta(days=7) <= self.purchase_date <= timezone.now()

    # TODO use Point field data type from GeoDjango for location

    def __str__(self):
        return str(self.description)


class ServiceDetails(models.Model):
    thing = models.OneToOneField(Thing, on_delete=models.CASCADE)
    owner_email = models.EmailField()
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)


# when a new device is added to the marketplace, email is sent to all subscriber's
class SubscribersList(models.Model):
    name = models.CharField(max_length=150, default='my coffee machine')
    email = models.EmailField()

    def __str__(self):
        return str(self.name + " " + self.email)
