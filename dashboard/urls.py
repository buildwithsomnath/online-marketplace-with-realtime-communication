from django.urls import path

from .views import (
    DashboardView,
    MyItemsView,
    MyItemDetailView,
)

app_name = "dashboard"

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),

    path("items/", MyItemsView.as_view(), name="my-items"),

    path(
        "items/<int:pk>/",
        MyItemDetailView.as_view(),
        name="my-item-detail",
    ),
]