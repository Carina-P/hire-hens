from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('faq')

    if request.method == 'POST':
        form = FaqForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQ successfully added')
            return redirect('faq')
        else:
            messages.error(
                request, 'Failed to add faq. Please ensure the form is valid.'
                )

    form = FaqForm
    context = {
        'form': form,
        'heading': 'Add FAQ',
        'button_text': 'Add'
    }
    return render(request, 'faq/faq_input.html', context)


def edit_faq(request, faq_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('faq')

    faq = get_object_or_404(Faq, id=faq_id)

    if request.method == 'POST':
        form = FaqForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQ was succesfully changed.')
            return redirect('faq')
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.'
                )

    form = FaqForm(instance=faq)
    context = {
        'form': form,
        'heading': 'Edit FAQ',
        'button_text': 'Edit'
    }
    return render(request, 'faq/faq_input.html', context)


def delete_faq(request, faq_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('faq')

    faq = get_object_or_404(Faq, id=faq_id)
    faq.delete()
    messages.success(request, "FAQ succesfully removed")

    return redirect('faq')
