from django.db import models


class SimpleModel(models.Model):
    """
    A simple model with no special things going on.
    """

    text = models.CharField(max_length=255)
