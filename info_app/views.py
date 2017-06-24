"""Contains vews methods, that show some info about project.
"""


from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


def home(request):
    """Shows home page.
    """
    template = loader.get_template('home.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def about(request):
    """Shows about page.
    """
    template = loader.get_template('about.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
