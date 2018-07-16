from django.db import models
from django.db.models import Model


def format_photo_path(instance, filename):
    return '{}/{}'.format(
        instance.name.replace(' ', '-'),
        filename.replace(' ', '-')
    )


class Speaker(Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(
        upload_to=format_photo_path
    )
    degree = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    abstract = models.TextField()

    def __str__(self):
        return self.name


class Metatag(Model):
    NAME = 'name'
    PROP = 'property'
    ITEM = 'itemprop'

    tag = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    attr = models.CharField(
        max_length=30,
        choices=((NAME, NAME), (ITEM, ITEM), (PROP, PROP)),
        default=NAME,
    )

    def __str__(self):
        return '{}: {}'.format(self.tag, self.value)


class Content(Model):
    field = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.field


class Affiliates(Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(
        upload_to=format_photo_path
    )

    def __str__(self):
        return self.name
