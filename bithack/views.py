from bithack.forms import RegisterForm

from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):

    if request.method == 'POST':
        # TODO check handling for registrant submission
        form = RegisterForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/success')
        else:
            response = HttpResponseBadRequest()
            response.reason_phrase = "Invalid form submission"
            return response

    register_form = RegisterForm()

    context = {'register_form': register_form}

    return render_to_response("index.html", context, RequestContext(request))
