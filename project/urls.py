from django.urls import path
from .views import PostProjectView, ProjectView, EachProjectView

urlpatterns = [
    path('post_project', PostProjectView.as_view()),
    path('view_project', ProjectView.as_view()),
    path('view_project/<int:pk>', EachProjectView.as_view()),
]