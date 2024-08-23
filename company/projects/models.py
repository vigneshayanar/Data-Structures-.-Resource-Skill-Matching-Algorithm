from django.db import models
from django.db.models.signals import post_save

class Skill(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Resource(models.Model):
    name=models.CharField(max_length=100)
    available_From=models.DateField()
    available_To=models.DateField()
    skill=models.ManyToManyField(Skill)
    assigned=models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.name
        
class Project(models.Model):
    name=models.CharField(max_length=100)
    start_date=models.DateField()
    End_date=models.DateField()
    Description=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    projects=models.ForeignKey(Project,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    start_date=models.DateField()
    End_date=models.DateField()
    requiredSkill=models.ManyToManyField(Skill)
    assigned=models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.name

class TaskAssignments(models.Model):
    task=models.ForeignKey(Task,on_delete=models.CASCADE)
    resource=models.ForeignKey(Resource,on_delete=models.CASCADE)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.task.name} assigned to {self.resource.name} to {self.project.name}"