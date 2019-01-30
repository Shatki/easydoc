from django.http import HttpResponse
from django.http import JsonResponse

# import time
from .models import Counterpart, Bank


# --------------До введения REST----------------
def contractors_json(request):
    response = []
    try:
        contractors = Counterpart.objects.all()
    except Counterpart.DoesNotExist:
        return HttpResponse(u"Conteractor.contractor_json. BD error", content_type='text/html')
    for contractor in contractors:
        elem = dict(
            id=str(contractor.id),
            name=contractor.name,
        )
        response.append(elem)
    return JsonResponse(response, safe=False)

# Create your views here.
