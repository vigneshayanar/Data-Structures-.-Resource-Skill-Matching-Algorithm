from django.urls import path,include
from .views import SkillViewSet,TaskAssignmentViewSet,TaskViewSet,ProjectViewSet,ResourceViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'SkillViewSet',SkillViewSet)
router.register(r'ResourceViewSet',ResourceViewSet)
router.register(r'TaskViewSet',TaskViewSet)
router.register(r'TaskAssignmentViewSet',TaskAssignmentViewSet)
router.register(r'ProjectViewSet',ProjectViewSet)


urlpatterns = [
    path('',include(router.urls)),
]