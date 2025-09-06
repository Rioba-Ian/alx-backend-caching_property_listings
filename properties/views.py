from serializers import PropertySerializer
from django.http import JsonResponse
from properties.models import Property
from django.views.decorators.cache import cache_page

# Create your views here.


@cache_page(60 * 15)  # Cache the view for 15 minutes
def property_list(request):
    properties = Property.objects.all()
    serializer = PropertySerializer(properties, many=True)
    return JsonResponse({"properties": serializer.data}, safe=False)
