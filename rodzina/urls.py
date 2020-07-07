from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    ChildrenListView,
    TutorListView,
    FamilyListView,
    FamilyUpdate,
    GroupListView,
    GrupUpdate,
    PersonCreate,
    PersonUpdate,
    PersonDeleteAjax,
)


urlpatterns = [
    path('children/', ChildrenListView.as_view(), name='children'),
    path('tutor/', TutorListView.as_view(), name='tutor'),

    path('person/new/', PersonCreate.as_view(), name='person_new'),
    path(
        'person/<int:pk>',
        PersonUpdate.as_view(),
        name='person_edit'),
    path(
        'person/<int:pk>/delete/',
        PersonDeleteAjax.as_view(),
        name='person_delete'),

    path('family_list/', FamilyListView.as_view(), name='family_list'),
    path('family/<int:pk>/', FamilyUpdate.as_view(), name='family_edit'),
    path('group_list/', GroupListView.as_view(), name='group_list'),
    path('group/<int:pk>/', GrupUpdate.as_view(), name='group_edit'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
