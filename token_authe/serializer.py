from rest_framework import serializers
from .models import myMod

class myModserial(serializers.ModelSerializer):
    class Meta:
        model = myMod
        fields = "__all__"