from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from contactApp.forms import ContactForm
from contactApp.models import Contact

class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, "contact.html", {"form": form})

    def post(self, request):
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # 
                form.save()
            except Exception as e:
                print(f"Error occurred: {e}")
                return render(request, "contact.html", {
                    "form": form,
                    "error_server": "An error has occurred while saving the contact"
                })
            return redirect('contact_list')  # Redirect to the success page
        else:
            print(form.errors)
            return render(request, "contact.html", {
                "form": form,
                "errors": form.errors
            })

# class SuccessView(View):
#     def get(self, request):
#         return render(request, "success.html")
class SuccessView(TemplateView):
    template_name = "success.html"
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['message'] = "Your contact has been successfully submitted!"
        return context

# class ContactListView(View):
#     def get(self, request):
#         contacts = Contact.objects.all()
#         return render(request, "contact_list.html", {"contacts": contacts})

class ContactListView(ListView):
    model = Contact
    template_name = "contact_list.html"
    context_object_name = "contacts"

class EditContactView(UpdateView):
    model=Contact
    form_class = ContactForm
    template_name = "editcontact.html"
    success_url = reverse_lazy('contact_list')

    # def get_context_data(self, **kwargs: Any):
    #     context = super().get_context_data(**kwargs)
    #     form = ContactForm()
    #     context['form'] = form

# class EditContactView(View):
#     def get(self, request, id):
#         contact = get_object_or_404(Contact, id=id)
#         form = ContactForm(initial={
#             'name': contact.name,
#             'email': contact.email,
#             'phone_number': contact.phone_number,
#         })
#         return render(request, "editcontact.html", {"form": form, "contact": contact})

#     def post(self, request, id):
#         contact = get_object_or_404(Contact, id=id)
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             contact.name = form.cleaned_data['name']
#             contact.email = form.cleaned_data['email']
#             contact.phone_number = form.cleaned_data['phone_number']
#             contact.save()
#             return redirect('contact_list')
#         return render(request, "editcontact.html", {"form": form, "contact": contact, "errors": form.errors})

# class DeleteContactView(View):
#     def get(self, request, id):
#         contact = get_object_or_404(Contact, id=id)
#         return render(request, "confirm_delete.html", {"contact": contact})

#     def post(self, request, id):
#         contact\
# /56' = get_object_or_404(Contact, id=id)
#         contact.delete()
#         return redirect('contact_list')
class DeleteContactView(DeleteView):
    model = Contact
    template_name="contact_list.html"
    success_url = reverse_lazy('contact_list')
