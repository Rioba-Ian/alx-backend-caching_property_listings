from serializers import PropertySerializer
from properties.models import Property
from rest_framework.response import Response
from django.views.decorators.cache import cache_page

# Create your views here.


@cache_page(60 * 15)  # Cache the view for 15 minutes
def property_list(request):
    properties = Property.objects.all()
    serializer = PropertySerializer(properties, many=True)
    return Response(serializer.data)
