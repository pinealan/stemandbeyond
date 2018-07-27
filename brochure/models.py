from django.db import models
from django.db.models import Model


def format_photo_path(instance, filename):
    return '{}/{}'.format(
        instance.name.replace(' ', '-'),
        filename.replace(' ', '-')
    )


class Speaker(Model):
    name = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(
        upload_to=format_photo_path,
        blank=True
    )
    title = models.CharField(max_length=100, blank=True)
    degree = models.CharField(max_length=100, blank=True)
    subject = models.CharField(max_length=50, blank=True)
    profile = models.TextField(blank=True)
    abstract = models.TextField(blank=True)

    chin_name = models.CharField(max_length=10, blank=True)
    chin_title = models.CharField(max_length=100, blank=True)
    chin_degree = models.CharField(max_length=50, blank=True)
    chin_subject = models.CharField(max_length=50, blank=True)
    chin_profile = models.TextField(blank=True)
    chin_abstract = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Metatag(Model):
    NAME = 'name'
    PROP = 'property'
    ITEM = 'itemprop'

    tag = models.CharField(max_length=50)
    attr = models.CharField(
        max_length=30,
        choices=((NAME, NAME), (ITEM, ITEM), (PROP, PROP)),
        default=NAME,
    )
    content = models.CharField(max_length=100)

    def __str__(self):
        return '{}: {}'.format(self.tag, self.content)


class Content(Model):
    field = models.CharField(max_length=100)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.field


class Affiliate(Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(
        upload_to=format_photo_path
    )

    def __str__(self):
        return self.name
