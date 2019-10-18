from django.db import models


class User(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)


class Project(models.Model):
    name = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    created_at = models.DateTimeField('date published')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ProjectMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_member = models.ForeignKey(User, on_delete=models.CASCADE)
