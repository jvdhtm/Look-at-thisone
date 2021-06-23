from rest_framework import serializers
from record_api.models import New_Records
 
class NewRecordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = New_Records
        fields = ('name', 'time', 'date')