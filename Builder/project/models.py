from django.db import models
import uuid
# Create your models here.

class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    description = models.TextField(default=None,null=True)
    created_by = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=250,unique=True)
    is_published = models.BooleanField(default=False)
    
    def __str__(self):
        return (f"Project: {self.name} created by {self.created_by} on"
                " {self.created_on}")


class Page(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_by = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.JSONField()
    project = models.ForeignKey(Project, related_name='pages', 
                                on_delete=models.CASCADE)
    html = models.TextField(default=None,null=True)
