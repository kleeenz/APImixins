from django.shortcuts import render
from .serializer import myModserial
from .models import myMod
from rest_framework import mixins
from rest_framework import generics


class myModList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    queryset = myMod.objects.all()
    serializer_class = myModserial

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def getR(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


