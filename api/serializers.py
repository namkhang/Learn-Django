from rest_framework import serializers
from api.models import Account

class AccountSerialiser(serializers.HyperlinkedModelSerializer):
     class Meta:
                 model = Account
                 fields = "__all__"   