from django.db import models
from django.db.models import Model


def speaker_photo_path(instance, filename):
    return '{}/{}'.format(
        instance.name.replace(' ', '-'),
        filename.replace(' ', '-')
    )


class Speaker(Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(
        upload_to=speaker_photo_path
    )
    degree = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    abstract = models.TextField()

    def __str__(self):
        return self.name


class Metatag(Model):
    tag = models.CharField(max_length=50)
    value = models.CharField(max_length=100)

    def __str__(self):
        return '{}: {}'.format(self.tag, self.value)


class Content(Model):
    field = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.field
