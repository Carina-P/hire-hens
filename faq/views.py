from django.shortcuts import render, redirect, get_object_or_404, reverse
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
        # messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FaqForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faq')
        else:
            # messages.error(request, 'Failed to add faq. Please ensure the form is valid.')
            print("error")

    form = FaqForm
    context = {
        'form': form
    }
    return render(request, 'faq/add_faq.html', context)


def edit_faq(request, faq_id):
    if not request.user.is_superuser:
        # messages.error(request, 'Sorry, only store owners can do that.')
        print("error")
        return redirect(reverse('home'))

    faq = get_object_or_404(Faq, id=faq_id)

    if request.method == 'POST':
        form = FaqForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            return redirect('faq')
        else:
            # messages.error(request, 'Failed to update product. Please ensure the form is valid.')
            print("error")

    form = FaqForm(instance=faq)
    context = {
        'form': form
    }
    return render(request, 'faq/edit_faq.html', context)


def delete_faq(request, faq_id):
    if not request.user.is_superuser:
        # messages.error(request, 'Sorry, only store owners can do that.')
        print("error")
        return redirect(reverse('home'))

    faq = get_object_or_404(Faq, id=faq_id)
    faq.delete()

    return redirect('faq')
