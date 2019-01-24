# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import JsonResponse
# import time
from .models import Contractor, ContractorType

from .serializers import ContractorSerializer, ContractorTypeSerializer
from rest_framework import viewsets



class ContractorTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ContractorType.objects.all().order_by('name')
    serializer_class = ContractorTypeSerializer


class ContractorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Contractor.objects.all().order_by('-name')
    serializer_class = ContractorSerializer


# --------------До введения REST----------------
def contractors_json(request):
    response = []
    try:
        contractors = Contractor.objects.all()
    except Contractor.DoesNotExist:
        return HttpResponse(u"Conteractor.contractor_json. BD error", content_type='text/html')
    for contractor in contractors:
        elem = dict(
            id=str(contractor.id),
            name=contractor.name,
        )
        response.append(elem)
    return JsonResponse(response, safe=False)
