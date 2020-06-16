from django.urls import path
from .views import ChildrenListView


urlpatterns = [
    path('children/', ChildrenListView.as_view(), name='children')
]
