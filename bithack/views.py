from bithack.forms import RegisterForm
from bithack.models import Hacker

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):

    if request.method == 'POST':
        # TODO make Register Form into HackerForm that's a modelForm
        form = RegisterForm(request.POST)
        if form.is_valid():

            hacker_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            hacker = Hacker()
            hacker.user = hacker_user
            hacker.first_name = request.POST['first_name']
            hacker.last_name = request.POST['last_name']
            hacker.email = request.POST['email']
            hacker.school = request.POST['school']
            hacker.tshirt_size = request.POST['tshirt_size']
            hacker.vegetarian = request.POST.get('vegetarian', False)
            hacker.source = request.POST['source']
            hacker.save()
            return HttpResponseRedirect('/success')
        else:
            response = HttpResponseBadRequest()
            response.reason_phrase = "Invalid form submission"
            return response

    register_form = RegisterForm()

    context = {'register_form': register_form}

    return render_to_response("index.html", context, RequestContext(request))
