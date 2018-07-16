from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Speaker


def index(req):
    speakers = Speaker.objects.all()
    context = {}
    context['speakers'] = list(speakers)
    return render(req, 'brochure/index.html', context=context)
