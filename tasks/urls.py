from django.urls import path
from .views import TaskListCreateView, TaskDetailView, MilestoneListCreateView, MilestoneDetailView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('milestones/', MilestoneListCreateView.as_view(),
         name='milestone-list-create'),
    path('milestones/<int:pk>/', MilestoneDetailView.as_view(),
         name='milestone-detail'),
]
