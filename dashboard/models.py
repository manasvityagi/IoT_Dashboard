from django.contrib.auth.models import User
from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=150, default='38 Whitney Street')
    zip = models.CharField(max_length=10, default='06001')

    def __str__(self):
        return str(self.street)


class Manufacturer(models.Model):
    name = models.CharField(max_length=150, default='generic manufacturer')
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Home(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default=Address())

    def __str__(self):
        return self.name


class Things(models.Model):
    description = models.CharField(max_length=150, default='my coffee machine')
    device_type = models.CharField(max_length=40, default='coffee machine')
    installed_home_id = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    # installed_home_id = models.ForeignKey(Home, on_delete=models.CASCADE)
    mfg = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING,
                            default=Manufacturer("Generic Manufacturer", Address()))
    # manufacturer_id = models.CharField(max_length=50)
    manufacturing_date = models.DateField()
    expiry_date = models.DateField()
    model_number = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    # in hours
    life_expectancy = models.IntegerField()
    life_used = models.IntegerField()
    # watt hour
    power_rating = models.IntegerField()
    alertable = models.BooleanField()
    trend_applicable = models.BooleanField()
    value_stream_id = models.IntegerField()
    # TODO use Point field data type from GeoDjango
    # for more accurate or acceptable solution for geographic data type
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class DeviceTypes(models.Model):
    name = models.CharField(max_length=50, default='generic device')

    def __str__(self):
        return self.name


# a time series database model
class ValueStream(models.Model):
    description = models.CharField(max_length=150, default='value stream description')
    property_name = models.CharField(max_length=150, default='property name')
    value = models.FloatField(default=0.0)
    ts = models.DateTimeField()
    quality = models.CharField(max_length=10, default='GOOD')

    def __str__(self):
        return self.description

# t1 = Things(description = "Kitchen Coffee Machine", device_type="coffee_machine", installed_home_id=1, image_path="",manufacturer_id=2,manufacturing_date=date.today(),
#             life_used=56,life_expectancy=850,power_rating=500,trend_applicable=True,value_stream_id=2,expiry_date=date.today(), alertable=True)
# t2 = Things(description = "Kitchen Coffee Machine", device_type="coffee_machine", installed_home_id=1, image_path="",manufacturer_id=2,manufacturing_date=date.today(),
#             life_used=56,life_expectancy=850,power_rating=500,trend_applicable=True,value_stream_id=2,expiry_date=date.today(), alertable=True)


# t3 = Things(description = "Dads Road Bike", device_type="bike", installed_home_id=2, image_path="",manufacturer_id=3,manufacturing_date=date.today(),
#             life_used=5,life_expectancy=4500,power_rating=0,trend_applicable=True,value_stream_id=2,expiry_date=date.today(), alertable=True)

# t4 = Things(description = "Garage Smart Lock", device_type="lock", installed_home_id=2, image_path="",manufacturer_id=4,manufacturing_date=date.today(),
#             life_used=1200,life_expectancy=50000,power_rating=10,trend_applicable=True,value_stream_id=3,expiry_date=date.today(), alertable=True)

# t45 = Things(description = "Garage Smart Lock", device_type="lock", installed_home_id=2, image_path="",manufacturer_id=4,manufacturing_date=date.today(),
#             life_used=1200,life_expectancy=50000,power_rating=10,trend_applicable=True,value_stream_id=3,expiry_date=date.today(), alertable=True)


# t5 = Things(description = "Energy Meter", device_type="energy_meter", installed_home_id=1, image_path="",manufacturer_id=5,manufacturing_date=date.today(),
#             life_used=15000,life_expectancy=60000,power_rating=5,trend_applicable=True,value_stream_id=2,expiry_date=date.today(), alertable=False)

# t6 = Things(description = "Water Meter", device_type="water_meter", installed_home_id=1, image_path="",manufacturer_id=6,manufacturing_date=date.today(),
#             life_used=12000,life_expectancy=60000,power_rating=5,trend_applicable=True,value_stream_id=2,expiry_date=date.today(), alertable=False)

# t7 = Things(description = "Kitchen Coffee Machine", device_type="coffee_machine", installed_home_id=1, image_path="",manufacturer_id=2,manufacturing_date=date.today(),
#             life_used=56,life_expectancy=850,power_rating=500,trend_applicable=True,value_stream_id=2,expiry_date=date.today(), alertable=True)

#
# t3 = Things(description = "Dads Road Bike", device_type="bike", installed_home_id=2, image_path="",manufacturer_id=3,manufacturing_date=date.today(),
#             life_used=5,life_expectancy=4500,power_rating=0,trend_applicable=True,value_stream_id=2,expiry_date=date.today(), alertable=True)
#
#  t3 = Things(description = "Dads Road Bike", device_type="bike", installed_home_id=2, image_path="",manufacturer_id=3,manufacturing_date=date.today(),
#              life_used=5,life_expectancy=4500,power_rating=0,trend_applicable=True,value_stream_id=2,expiry_date=date.today(), alertable=True)
