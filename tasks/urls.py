from django.urls import path
from .views import CreateTaskView, TaskView, EachTaskView

urlpatterns = [
    path('create_Task/', CreateTaskView.as_view()),
    path('view_task/', TaskView.as_view()),
    path('view_task/<int:pk>/', EachTaskView.as_view()),
]
