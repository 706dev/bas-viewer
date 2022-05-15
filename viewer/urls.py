from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("content", api.contentViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("viewer/content/", views.contentListView.as_view(), name="viewer_content_list"),
    # path("viewer/content/create/", views.contentCreateView.as_view(), name="viewer_content_create"),
    path("viewer/content/detail/<int:pk>/", views.contentDetailView.as_view(), name="viewer_content_detail"),
    path("viewer/content/update/<int:pk>/", views.contentUpdateView.as_view(), name="viewer_content_update"),
    # path("viewer/content/delete/<int:pk>/", views.contentDeleteView.as_view(), name="viewer_content_delete"),
)
