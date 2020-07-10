from django.urls import path

from .views import EnterRFID, FamilyAction

urlpatterns = [
    path('enter/', EnterRFID.as_view(), name='enter_rfid'),
    path(
        'family_action/<int:pk>/',
        FamilyAction.as_view(),
        name='family_action')
]
