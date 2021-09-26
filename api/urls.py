"""CNAB Parser API urls file"""
from django.urls import path
from api.views import CnabImportView, SchedulerView

urlpatterns = [
    path(
        'scheduler',
        SchedulerView.as_view()
    ),
    path(
        'shop/<int:shop_id>/import',
        CnabImportView.as_view(),
        name='shop_import'
    )
]
