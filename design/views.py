from django.shortcuts import render
from django.http import HttpRequest

from .serializers import Design_Serializer, Item_Serializer
from .models import Design_Model, Item_Model

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework import status

desc = """
    This is a test description, created by team embedded3d, for prototyping the functionality of the Save Design module,
    The description in the MVP, will be filled by the designer themself and contain real description about the design
"""

class Save_Design(APIView):
    serializer_class = Design_Serializer

    def _extend_request(self, request):
        data = request.POST.copy()
        # print(request.data['content'])

        design_count = Design_Model.objects.all().count()
        data['name'] = "Design{}".format(design_count + 1)
        data['description'] = desc
        data['url'] = "http://45.141.79.228:8000/exapmle/?design={}/".format(request.data['content'])
        data['content'] = request.data['content']
        request_extended = Request(HttpRequest())
        request_extended._full_data = data

        return request_extended

    def post(self, request, *args, **kwargs):
        request_extended = self._extend_request(request)
        # print(request_extended.data['name'])
        serialized_design = self.serializer_class(data = request_extended.data)

        
        serialized_design.is_valid()
        # print(serialized_design.data['content'])

        
        # fill the object will dummy attributes
        # serialized_design.data['description'] = desc
        # serialized_design.data['name'] = 

        # serialized_design.is_valid()
        serialized_design.save()

        return Response(request.data, status=status.HTTP_200_OK)

class Retrieve_Designs_List(APIView):
    serializer_class = Design_Serializer

    def get(self, request, *args, **kwargs):
        designs = Design_Model.objects.all()
        if designs.exists():
            serialized_designs = self.serializer_class(designs, many = True)
            return Response(serialized_designs.data, status = status.HTTP_200_OK)
        else:
            return Response({"detail": "No designs"}, status = status.HTTP_404_NOT_FOUND)

class Retrieve_Design(APIView):
    serializer_class = Design_Serializer

    def get(self, request, *args, **kwargs):
        name = self.kwargs["name"]
        try:
            design = Design_Model.objects.get(name = name)
            serialized_design = self.serailizer_class(design)
            return Response(serialized_design, status = status.HTTP_200_OK)
        except:
            return Response({"detail": "not found"}, status = status.HTTP_404_NOT_FOUND)

class Retrieve_Item_List(APIView):
    serializer_class = Item_Serializer    

    def get(self, request, *args, **kwargs):
        try:
            items = Item_Model.objects.all()
            serialized_items = self.serializer_class(items)
            return Response(serialized_items, status = status.HTTP_200_OK)
        except:
            return Response(status = status.HTTP_404_NOT_FOUND)

class Add_Item(APIView):
    serializer_class = Item_Serializer

    def post(self, request, *args, **kwargs):
        try:
            serialized_item = self.serializer_class(data = request.data, many = True)
            serialized_item.is_valid()

            serialized_item.save()

            return Response(request.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_OK)


    


class Trending_Design(APIView):
    serializer_class = Design_Serializer

    def get(self, request, *args, **kwargs):
        designs = Design_Model.objects.all().order_by('-like')[:3]
        if designs.exists():
            serialized_designs = self.serializer_class(designs, many = True)
            return Response(serialized_designs.data, status = status.HTTP_200_OK)
        else:
            return Response({"detail": "No designs"}, status = status.HTTP_404_NOT_FOUND)

class Like_Design(APIView):
    def get(self, request, design, *args, **kwargs):
        design_obj = Design_Model.objects.filter(id = design)
        design_obj.like += 1
        design_obj.save(update_fields=['like'])
        return Response(status=status.HTTP_200_OK)       

class Disike_Design(APIView):
    def get(self, request, design, *args, **kwargs):
        design_obj = Design_Model.objects.filter(id = design)
        design_obj.dislike += 1
        design_obj.save(update_fields=['dislike'])
        return Response(status=status.HTTP_200_OK)       