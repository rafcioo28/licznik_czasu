from django.urls import path
from .views import (
    ChildrenListView,
    FamilyListView,
    GroupListView,
    PersonViewAPI,
    person_edit,
    family_edit,
    group_edit,
)


urlpatterns = [
    path('children/', ChildrenListView.as_view(), name='children'),
    path('family_list/', FamilyListView.as_view(), name='family_list'),
    path('group_list/', GroupListView.as_view(), name='group_list'),
    path('person_edit/<int:id>/', person_edit, name='person_edit'),
    path('family_edit/<int:id>/', family_edit, name='family_edit'),
    path('group_edit/<int:id>/', group_edit, name='group_edit'),
    path('api/person/<int:person_id>/', PersonViewAPI.as_view()),
]
