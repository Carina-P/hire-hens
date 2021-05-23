from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Faq
from .forms import FaqForm


def get_faq(request):
    """
    Get FAQ from the database and render to page.

    Input:
        request (object): The HttpRequest object
    """
    try:
        faqs = Faq.objects.all()
    except Exception as e:
        messages.error(
            request,
            'Error! Something went wrong, retrieving information from database.\
            Please inform site owner!:', e
        )
        faqs = None

    context = {
        'faqs': faqs
    }
    return render(request, 'faq/faq.html', context)


def add_faq(request):
    """
    Render a form to add FAQ.
    when user saves information, form information is saved to database.
    Only superusers are authorized to add information.

    Input:
        request (object): The HttpRequest object
    """
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
    """
    Render a form and show information for an FAQ that user wants to edit.
    When user saves changed information, form information is saved to database.
    Only superusers are authorized to edit information.

    Input:
        request (object): The HttpRequest object
        faq_id: int, database id of the question
    """
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
    """
    Delete a question and then redirect user to FAQ page.
    Only superusers are authorized to delete information.

    Input:
        request (object): The HttpRequest object
        faq_id: int, database id of the question
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('faq')

    faq = get_object_or_404(Faq, id=faq_id)

    try:
        faq.delete()
        messages.success(request, "FAQ succesfully removed")
    except Exception as e:
        messages.error(
            request,
            'Error! Something went wrong, deleting question.\
            Please inform support!',
            e
        )

    return redirect('faq')
