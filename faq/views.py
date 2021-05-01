from django.shortcuts import render
from .models import Faq

# Create your views here.


def get_faq(request):
    faqs = Faq.objects.all()
    context = {
        'faqs': faqs
    }
    return render(request, 'faq/faq.html', context)
