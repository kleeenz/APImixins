from rest_framework import serializers
from django.contrib.auth.models import User
from .models import myMod



class personSerial(serializers.ModelSerializer):
    myMods = serializers.PrimaryKeyRelatedField(many=True, queryset=myMod.objects.all())
    person = serializers.ReadOnlyField(source='person.username')
    class Meta:
        model = User
        fields = ['id', 'username', 'myMods', 'person']


class myModserial(serializers.ModelSerializer):
    class Meta:
        model = myMod
        fields = "__all__"

