from django.urls import path

from properties.views import PropertyListView

urls = [
    path("properties/", PropertyListView.as_view(), name="property-list"),
]
