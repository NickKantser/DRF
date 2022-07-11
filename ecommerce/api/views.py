from rest_framework import status, viewsets, mixins
from store.serializers import GeneralSerializer
from rest_framework.response import Response
from django.http import Http404

from rest_framework.generics import get_object_or_404

class StoreViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    serializer_class = GeneralSerializer

    def get_queryset(self):
        model_name = self.kwargs.get('model') # url parameter
        model_class = GeneralSerializer.get_model_class_by_name(model_name)

        if model_class is None:
            raise Http404

        GeneralSerializer.Meta.model = model_class # initialize corresponding model to serializer
        return model_class.objects.all()

    def create(self, request, *args, **kwargs):
        # If we get an array we iterate over all received dictionaries
        # otherwise, we just call parent's create method
        serial_data = [] # array to which all serialized data will be appended
        if isinstance(request.data, list):
            for i in range(len(request.data)):
                serializer = self.get_serializer(data=request.data[i])
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                serial_data.append(serializer.data)
            return Response(serial_data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return super().create(request, *args, **kwargs)
