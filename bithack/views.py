from bithack.forms import RegisterForm

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):

    if request.method == 'POST':
        # TODO make Register Form into HackerForm that's a modelForm
        # TODO make another form for user registration to handle the user creation
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            return HttpResponseRedirect('/success')
        else:
            response = HttpResponseBadRequest()
            response.reason_phrase = "Invalid form submission"
            return response

    register_form = RegisterForm()

    context = {'register_form': register_form}

    return render_to_response("index.html", context, RequestContext(request))
