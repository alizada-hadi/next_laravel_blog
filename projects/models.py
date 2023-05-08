from django.db import models
from accounts.models import User


class Project(models.Model):
    PROJECT_TYPE = (
        ("List", "List"),
        ("Board", "Board"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    favorite = models.BooleanField(default=False)
    project_type = models.CharField(
        max_length=100,
        choices=PROJECT_TYPE,
        default="Board"
    )
    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
