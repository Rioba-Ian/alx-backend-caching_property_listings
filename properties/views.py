from serializers import PropertySerializer
from django.http import JsonResponse

# from properties.models import Property
from django.views.decorators.cache import cache_page
from properties.utils import get_all_properties

# Create your views here.


@cache_page(60 * 15)  # Cache the view for 15 minutes
def property_list(request):
    if request.method == "GET":
        properties = get_all_properties()
        serializer = PropertySerializer(properties, many=True)
        return JsonResponse({"properties": serializer.data}, safe=False)
    return JsonResponse({"error": "Method not allowed"}, status=405)
