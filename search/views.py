# rest framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# directories
from design.serializers import Design_Serializer
from design.models import Design_Model

class Search_Handler(APIView):
    serializer_class = Design_Serializer

    def get(self, request, name, *args, **kwargs):
        designs = Design_Model.objects.filter(name__icontains = name)
        if designs.exists():
            serialized_designs = self.serializer_class(designs, many = True)
        else:
            designs = Design_Model.objects.all()
            serialized_designs = self.serializer_class(designs, many = True)
        # serialized_designs.is_valid()

        return Response(serialized_designs.data, status = status.HTTP_200_OK)