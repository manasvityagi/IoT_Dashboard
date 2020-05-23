from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Things(models.Model):
    name = models.CharField(max_length=150)
    installed_home_id = models.IntegerField()
    #installed_home_id = models.ForeignKey(Home, on_delete=models.CASCADE)
    manufacturer_id = models.CharField(max_length=50)
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
    power_rating = models.IntegerField()
    value_stream_id =  models.IntegerField()
    # TODO use Point field data type from GeoDjango
    location = models.CharField(max_length=50)


# power_rating varchar
# alertable boolean [default: 0]
# trend_applicable boolean [default: 0]

# value_stream_id long [unique, ref: - VS.id]
# installed_home int [ref: > H.id]
