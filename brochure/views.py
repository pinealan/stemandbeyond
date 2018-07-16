from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Speaker, Metatag, Content


def index(req):
    context = {}
    context['content'] = {blob.field: blob.text for blob in Content.objects.all()}
    context['speakers'] = list(Speaker.objects.all())
    context['metatagss'] = list(Metatag.objects.all())

    return render(req, 'brochure/index.html', context=context)
