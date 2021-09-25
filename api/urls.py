from api.views import SchedulerView
from django.urls import path

urlpatterns = [
    path('scheduler', SchedulerView.as_view())
]
