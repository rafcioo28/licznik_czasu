from django.urls import path, include
from .views import (
    ChildrenListView,
    TutorListView,
    FamilyCreate,
    FamilyListView,
    FamilyUpdate,
    GroupListView,
    GrupUpdate,
    PersonCreate,
    PersonJSON,
    PersonNewAjax,
    PersonUpdate,
    PersonDeleteAjax,
    RFIDDeleteAjax,
    RFIDNewAjax,
)


urlpatterns = [
    path('system/', include('django.contrib.auth.urls')),

    path('children/', ChildrenListView.as_view(), name='children'),
    path('tutor/', TutorListView.as_view(), name='tutor'),

    path('person/new/', PersonCreate.as_view(), name='person_new'),
    path(
        'person/<int:pk>/',
        PersonUpdate.as_view(),
        name='person_edit'),
    path(
        'person/<int:pk>/json/',
        PersonJSON.as_view(),
        name='person_ajax'),
    path(
        'person/new/json/',
        PersonNewAjax.as_view(),
        name='person_new_ajax'),
    path(
        'person/<int:pk>/delete/',
        PersonDeleteAjax.as_view(),
        name='person_delete'),


    path('family/new/', FamilyCreate.as_view(), name='family_new'),
    path('family_list/', FamilyListView.as_view(), name='family_list'),
    path('family/<int:pk>/', FamilyUpdate.as_view(), name='family_edit'),

    path(
        'rfid/<int:pk>/delete/',
        RFIDDeleteAjax.as_view(),
        name='rfid_delete'),

    path(
        'rfid/new/',
        RFIDNewAjax.as_view(),
        name='rfid_new_ajax'
    ),

    path('group_list/', GroupListView.as_view(), name='group_list'),
    path('group/<int:pk>/', GrupUpdate.as_view(), name='group_edit'),
]
