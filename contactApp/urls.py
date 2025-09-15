from django.urls import path
from .views import ContactView, SuccessView, ContactListView, EditContactView, DeleteContactView

urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
    path('success/', SuccessView.as_view(), name='success'),
    path('contacts/', ContactListView.as_view(), name='contact_list'),
    path('contacts/edit/<int:pk>/', EditContactView.as_view(), name='edit_contact'),
    path('contacts/delete/<int:pk>/', DeleteContactView.as_view(), name='delete_contact'),
]