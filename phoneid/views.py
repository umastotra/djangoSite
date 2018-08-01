from django.shortcuts import render
from .forms import ContactPlusForm
from telesign.messaging import MessagingClient
from requests.auth import HTTPBasicAuth
import requests
import json
from django.template import RequestContext

def contact_plus(phone_number, zip):
    data = {
        'first_name': 'Bob',
        'last_name': 'Fake',
        'address': 'Fake Address'

    }

    return data


def index(request):
    return render(request, 'home.html')

def demos(request):
    data = None
    template_params = None
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactPlusForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            phone_number = request.POST.get("phone_number", "")
            zip = request.POST.get("zip", "")
            data = contact_plus(phone_number, zip)
            template_params = {
                'form': form,
                'contact_plus_data': contact_plus_data}

            # redirect to a new URL:

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactPlusForm()
    # return render(request, 'demos.html', template_params, context=RequestContext(request))
    return render(request, 'demos.html', { 'form': form,'data': data})