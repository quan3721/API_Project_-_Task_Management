from django.urls import path
from .views import CreateReportView, ViewEmpPerformance
urlpatterns = [
    path('create_report/', CreateReportView.as_view()),
    path('view_perform_emp/', ViewEmpPerformance.as_view()),
]