from bithack.forms import RegisterForm

from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    register_form = RegisterForm()

    context = {'register_form': register_form}

    return render_to_response("index.html", context, RequestContext(request))
