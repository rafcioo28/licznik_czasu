from django.urls import path
from .views import (
    ChildrenListView,
    FamilyListView,
    GroupListView,
    person_edit
)


urlpatterns = [
    path('children/', ChildrenListView.as_view(), name='children'),
    path('family_list/', FamilyListView.as_view(), name='family_list'),
    path('group_list/', GroupListView.as_view(), name='group_lisr'),
    path('person_edit/<int:id>/', person_edit, name='person_edit'),
]
