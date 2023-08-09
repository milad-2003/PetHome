from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import ContactUsForm
from .models import ContactUs


# Create your views here.
class ContactUSView(View):
    def get(self, request):
        form = ContactUsForm()
        return render(request, "contact-us.html", context={
            'form':form
        })
    def post(self, request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            new_message = ContactUs()
            new_message.email = form.cleaned_data.get('email')
            new_message.subject = form.cleaned_data.get('subject')
            new_message.message = form.cleaned_data.get('message')
            new_message.save()
            return redirect("home:main")
        else:
            form.add_error('email', 'خطایی در تکمیل فرم رخ داده')

        return render(request, "contact-us.html", context={
            'form': form
        })