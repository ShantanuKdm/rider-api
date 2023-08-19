from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.SignupView.as_view(), name='signup'),
    path('update_profile', views.UpdateProfileView.as_view(), name='update_profile'),
    path('tasks/<str:tour_id>/', views.TaskListByTourView.as_view(), name='tasks_by_tour'),
    path('tasks/update/<str:task_id>/', views.UpdateTaskStatusView.as_view(), name='update_task_status')
]