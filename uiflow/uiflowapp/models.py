from django.db import models


class User(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)

    def __str__(self):
        return 'User: {} at {}'.format(self.fullname, self.email)


class Project(models.Model):
    name = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    timestamp = models.DateTimeField("date created", auto_now=True)
    project_creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Project {} by {}'.format(self.name, self.project_creator)

    class Meta:
        ordering = ['-timestamp']
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'project_creator'], name='unique_project'),
        ]


class ProjectMember(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        verbose_name="name of the project"
    )

    project_member = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="member of the project"
    )

    def __str__(self):
        return 'Project {} member {}'.format(self.project, self.project_member)

    class Meta:
        order_with_respect_to = 'project_member'
