from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from product_module.models import Product
from site_module.models import SiteSettings


class HomeView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "index.html"
    ordering = ['-price']

def site_header_component(request):
    setting : SiteSettings = SiteSettings.objects.filter(is_main_setting=True).first()
    return render(request, r"shared/header.html", context={
        'site_setting' : setting
    })

def site_footer_component(request):
    setting: SiteSettings = SiteSettings.objects.filter(is_main_setting=True).first()
    return render(request, r"shared/footer.html", context={
        'site_setting': setting
    })