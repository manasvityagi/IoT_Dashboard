from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Installed Device/ Thing Serializer
# Manufacturer List serializer
# DeviceModels Serializer
# SubscribersList Serializer
# Sellers Serializer
from dashboard.models import Thing, Manufacturer, DeviceModels, SubscribersList, Seller


# 1
class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thing
        fields = ['owner', 'description', 'device_model_info', 'installed_home_id', 'purchase_date', 'life_used',
                  'value_stream_id']


# 2
class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['name', 'address', 'is_certified', 'phone_number']


# 3
class DeviceModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceModels
        fields = ['name', 'max_life', 'warranty_days', 'image', 'energy_rating', 'safety_rating',
                  'current_consumption', 'mfg', 'model_number', 'serial_number']


# 4
class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscribersList
        fields = ['name',  'email']


# 5
class SellerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seller
        fields = ['name', 'address', 'phone_number', 'type_of_device_sold']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
