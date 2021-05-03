from django.contrib.auth.models import User
from .serializer import myModserial, personSerial
from .models import myMod
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions


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


class person_list(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = myMod.objects.all()
    serializer_class = personSerial

    def perform_create(self, serializer):
        serializer.save(person = self.request.user)


class persondetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = myMod.objects.all()
    serializer_class = personSerial


