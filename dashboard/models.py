from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Things(models.Model):
    description = models.CharField(max_length=150,default='my coffee machine')
    device_type = models.CharField(max_length=40,default='coffee machine')
    installed_home_id = models.IntegerField()
    image_path = models.CharField(max_length=100,default='coffee machine image path')
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

    def __str__(self):
        return self.description


# power_rating varchar
# alertable boolean [default: 0]
# trend_applicable boolean [default: 0]

# value_stream_id long [unique, ref: - VS.id]
# installed_home int [ref: > H.id]
