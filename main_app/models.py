from django.db import models
from django.contrib.auth.models import User


class WorksManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset()

    def all(self):
        return self.get_queryset().filter(ordering_option=True)


class Works(models.Model):
    name = models.CharField(max_length=100)
    work_description = models.TextField(max_length=400, null=True, blank=True)
    photo = models.ImageField(upload_to='master_works/')
    date = models.DateField()
    price = models.IntegerField()
    ordering_option = models.BooleanField(default=True)
    publishing_time = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(User, editable=False, null=True, blank=True, on_delete=models.CASCADE)
    objects = WorksManager()

    def __str__(self):
        return self.name


class Comments(models.Model):
    work = models.ForeignKey(Works, on_delete=models.CASCADE)
    description = models.TextField(max_length=400, null=True, blank=True)
    comment_author = models.ForeignKey(User, editable=False, null=True, blank=True, on_delete=models.CASCADE)
    publishing_time = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.description
