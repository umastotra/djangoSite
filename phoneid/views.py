from django.shortcuts import render
from .forms import ContactPlusForm
from telesign.messaging import MessagingClient
from requests.auth import HTTPBasicAuth
import requests
import json
from django.template import RequestContext

def contact_plus(phone_number, zip):
    customer_id = 'DDF354CF-3A6A-4581-9729-616FF2AE99CC'
    api_key = '73N4U2MQscrlrAl6CB7Sdj84HdBFZU038IeerxGI8y+knL9chktcy2a/KDhj9USc38MW5zuV62YSpoYotAQqag=='
    url = 'https://rest-ww.telesign.com/v1/phoneid/' + str(phone_number)
    headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
    r = requests.post(url, auth=HTTPBasicAuth(customer_id, api_key), json={'addons':{'contact_plus':{'billing_postal_code': str(zip)}}}, headers=headers)
    result = json.loads(r.content.decode('utf-8'))
    contact_plus_data = result['contact_plus']
    return contact_plus_data


def index(request):
    # if request.method == 'POST':
    #     if request.phone_number:
    return render(request, 'home.html')

def demos(request):
    contact_plus_data = None
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
            contact_plus_data = contact_plus(phone_number, zip)
            template_params = {
                'form': form,
                'contact_plus_data': contact_plus_data}

            # redirect to a new URL:

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactPlusForm()
    # return render(request, 'demos.html', template_params, context=RequestContext(request))
    return render(request, 'demos.html', { 'form': form,'contact_plus_data': contact_plus_data})