from django.shortcuts import render
from rest_framework import viewsets
from .Serializer import SkillSerializer,RessourceSerializer,TaskassignmentSerializer,ProjectSerializer,TaskSerializer
from  .models import Skill,Task,TaskAssignments,Project,Resource
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

import logging

logger = logging.getLogger(__name__)

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = RessourceSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskAssignmentViewSet(viewsets.ModelViewSet):
    queryset = TaskAssignments.objects.all()
    serializer_class = TaskassignmentSerializer



    def create(self, request, *args, **kwargs):
        data = request.data
        logger.info(f"Received data: {data}")
        
        project_id = request.data.get('project')
        task_id = request.data.get('task')
        resource_id = request.data.get("resource")

        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            logger.warning(f"Project with ID {project_id} not found.")
            return Response({"error": "Project not found."}, status=404)
        
        task = Task.objects.filter(projects=project)
        resource = Resource.objects.filter(id=resource_id)

        if not task.exists():
            logger.info("No tasks available for the specified project.")
            return Response({"error": "No tasks available for the specified project."}, status=404)
        else:
            for tasks in task:
                if not tasks.assigned:
                    logger.info(f"Task ID: {tasks.id}")
                    logger.info(f"Task Name: {tasks.name}")
                    logger.info(f"End Date: {tasks.End_date}")
                    logger.info(f"Start Date: {tasks.start_date}")
                    logger.info(f"Required Skills: {set(tasks.requiredSkill.all())}")
                    
                    required_skills = set(tasks.requiredSkill.all())
                else:
                    logger.info(f"Task already assigned.{tasks.name}")
                    continue
                
                for resources in resource:
                    if not resources.assigned:
                        logger.info(f"Resource Name: {resources.name}")
                        logger.info(f"Available From: {resources.available_From}")
                        logger.info(f"Available To: {resources.available_To}")
                        logger.info(f"Resource Skills: {set(resources.skill.all())}")
                        
                        resource_skills = set(resources.skill.all())
                        if required_skills.issubset(resource_skills):
                            logger.info(f"Resource has the required skills {resources.name}")
                            
                            if resources.available_From <= tasks.start_date and resources.available_To >= tasks.End_date:
                                TaskAssignments.objects.create(task=tasks, resource=resources, project=project)
                                tasks.assigned = True
                                resources.assigned = True
                                tasks.save()
                                resources.save()
                                logger.info("Task and Resource assignment completed.")
                                return Response({"message": "Task and Resource assignment completed."}, status=201)
                        else:
                            logger.info("Resource does not have the required skills.")
                            return Response({"error": "Resource does not have the required skills."}, status=400)
                    else:
                        logger.info("Resource already assigned to another task.")
                        continue

        logger.info(f"Task ID: {task_id}")
        return Response(data, status=200)
