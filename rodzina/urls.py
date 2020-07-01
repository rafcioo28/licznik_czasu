from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    ChildrenListView,
    TutorListView,
    FamilyListView,
    GroupListView,
    PersonViewAPI,
    family_edit,
    group_edit,
    PersonUpdate,
)


urlpatterns = [
    path('children/', ChildrenListView.as_view(), name='children'),
    path('tutor/', TutorListView.as_view(), name='tutor'),
    path('person/<int:pk>/', PersonUpdate.as_view(), name='person_edit'),
    path('family_list/', FamilyListView.as_view(), name='family_list'),
    path('group_list/', GroupListView.as_view(), name='group_list'),
    path('family_edit/<int:id>/', family_edit, name='family_edit'),
    path('group_edit/<int:id>/', group_edit, name='group_edit'),
    path('api/person/<int:person_id>/', PersonViewAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
