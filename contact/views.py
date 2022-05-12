
from django.shortcuts import render, redirect
from contact.forms import ContactForm


def contact(request):
    context = {
        'title': 'contact',
        'contact': 'active',
    }
    return render(request, 'contact.html', context)


def contact_form(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'title': 'contact-form',
        'contact': 'active',
        'one_contact': contact,
    }
    return render(request, 'contact.html', context)