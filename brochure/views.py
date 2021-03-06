from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Speaker, Metatag, Content, Affiliate


def index(req):
    context = {}
    context['content'] = {blob.field: blob.text for blob in Content.objects.all()}
    context['speakers'] = list(Speaker.objects.all())
    context['metas'] = list(Metatag.objects.all())
    context['affiliates'] = list(Affiliate.objects.all())

    return render(req, 'brochure/en.html', context=context)


def zh(req):
    context = {}
    context['content'] = {blob.field: blob.text for blob in Content.objects.all()}
    context['speakers'] = list(Speaker.objects.all())
    context['metas'] = list(Metatag.objects.all())
    context['affiliates'] = list(Affiliate.objects.all())

    return render(req, 'brochure/zh.html', context=context)
