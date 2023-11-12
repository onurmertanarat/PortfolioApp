from django.shortcuts import render
from .forms import ContactForm


def index_app(request):
    return render(request, 'index_app/index.html')


def projects(request):
    return render(request, 'index_app/projects.html')


def contact_me(request):
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
    else:
        form = ContactForm()

    return render(request, 'index_app/contact.html', {'form': form})