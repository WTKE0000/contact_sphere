from django.urls import path
from .views import (
    ContactView,
    SuccessView,
    ContactListView,
    EditContactView,
    DeleteContactView,
    signup,
    profile,
)
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Contact management
    path("", ContactView.as_view(), name="contact"),   # Add contact form
    path("success/", SuccessView.as_view(), name="success"),
    path("contacts/", ContactListView.as_view(), name="contact_list"),
    path("contacts/edit/<int:pk>/", EditContactView.as_view(), name="edit_contact"),
    path("contacts/delete/<int:pk>/", DeleteContactView.as_view(), name="delete_contact"),

    # Authentication
    path("signup/", signup, name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Optional profile page
    path("profile/", profile, name="profile"),
]
