from symtable import Class
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'


class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'


class Post(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=256)
    content = models.CharField(max_length=256, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    tag = models.ManyToManyField('Tag', related_name='posts', blank=True, null=True)


    def __str__(self):
        return f'{self.title} - {self.content} - {self.description}'


