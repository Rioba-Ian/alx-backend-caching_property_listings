from django.urls import path

from properties.views import property_list

urls = [
    path("properties/", property_list.as_view(), name="property-list"),
]
