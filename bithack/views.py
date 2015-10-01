from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):

    return render_to_response("index.html", {}, RequestContext(request))


def success(request):

    return render_to_response("success.html", {}, RequestContext(request))
