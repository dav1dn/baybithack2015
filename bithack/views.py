from bithack.forms import RegisterForm

from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    register_form = RegisterForm()

    context = {'register_form': register_form}

    return render_to_response("home.html", context, RequestContext(request))
