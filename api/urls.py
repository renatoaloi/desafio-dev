"""CNAB Parser API urls file"""
from django.urls import path
from api.views import CnabImportView, ImportsView, \
    SchedulerView, StoresView

urlpatterns = [
    path(
        'scheduler',
        SchedulerView.as_view()
    ),
    path(
        'file/<int:template_id>/import',
        CnabImportView.as_view(),
        name='file_import'
    ),
    path(
        'stores',
        StoresView.as_view(),
        name='stores'
    ),
    path(
        'imports',
        ImportsView.as_view(),
        name='imports'
    )
]
