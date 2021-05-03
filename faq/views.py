from django.shortcuts import render, redirect, get_object_or_404
from .models import Faq
from .forms import FaqForm

# Create your views here.


def get_faq(request):
    faqs = Faq.objects.all()
    context = {
        'faqs': faqs
    }
    return render(request, 'faq/faq.html', context)


def add_faq(request):
    if request.method == 'POST':
        form = FaqForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_faq')

    form = FaqForm
    context = {
        'form': form
    }
    return render(request, 'faq/add_faq.html', context)


def edit_faq(request, faq_id):
    faq = get_object_or_404(Faq, id=faq_id)

    if request.method == 'POST':
        form = FaqForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            return redirect('get_faq')
    
    form = FaqForm(instance=faq)
    context = {
        'form': form
    }
    return render(request, 'faq/edit_faq.html', context)
