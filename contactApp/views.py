from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from contactApp.forms import ContactForm
from contactApp.models import Contact


# ---------------------- CONTACT VIEWS ----------------------

class ContactView(LoginRequiredMixin, View):
    """Form to add a new contact"""
    login_url = "login"
    redirect_field_name = "next"

    def get(self, request):
        form = ContactForm()
        return render(request, "contact.html", {"form": form})

    def post(self, request):
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                print(f"Error occurred: {e}")
                return render(request, "contact.html", {
                    "form": form,
                    "error_server": "An error occurred while saving the contact"
                })
            return redirect("contact_list")
        else:
            print(form.errors)
            return render(request, "contact.html", {
                "form": form,
                "errors": form.errors
            })


class SuccessView(TemplateView):
    """Success page after contact submission"""
    template_name = "success.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['message'] = "Your contact has been successfully submitted!"
        return context


class ContactListView(LoginRequiredMixin, ListView):
    """List all contacts"""
    model = Contact
    template_name = "contact_list.html"
    context_object_name = "contacts"
    login_url = "login"


class EditContactView(LoginRequiredMixin, UpdateView):
    """Edit an existing contact"""
    model = Contact
    form_class = ContactForm
    template_name = "editcontact.html"
    success_url = reverse_lazy("contact_list")
    login_url = "login"


class DeleteContactView(LoginRequiredMixin, DeleteView):
    """Delete a contact (with confirmation)"""
    model = Contact
    template_name = "confirm_delete.html"  # confirmation page
    success_url = reverse_lazy("contact_list")
    login_url = "login"


# ---------------------- AUTHENTICATION VIEWS ----------------------

def signup(request):
    """Register a new user"""
    if request.user.is_authenticated:
        return redirect("contact")  # already logged in → go to contact page

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})


@login_required
def profile(request):
    """Optional profile page (not required if you redirect to contacts)"""
    return render(request, "profile.html")
