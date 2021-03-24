from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer
from . import services

class ProductViewSet(viewsets.ViewSet):
  def create(self, request):
    try:
      productSerializer = ProductSerializer(data=request.data)
      is_valid = productSerializer.is_valid()
      if not is_valid:
        return Response(data=None, status=400)
      product = productSerializer.create(productSerializer.data)
      product_created = services.create(product)
      respSerializer = ProductSerializer(product_created)
      print(respSerializer.data)
      return Response(data=respSerializer.data, status=201)
    except Exception as ex:
      return Response(status=500)

  def list(self, request):
    try:
      products = Product.objects.all()
      serializer = ProductSerializer(products, many=True)
      return Response(data=serializer.data)
    except Exception as ex:
      return Response(status=500)

  def retrieve(self, request, pk=None):
    try:
      if not pk:
        return Response('need a product id', status=400)
      product = get_object_or_404(Product, pk=pk)
      serializer = ProductSerializer(product)
      return Response(data=serializer.data)
    except Exception as ex:
      return Response(status=500)


      