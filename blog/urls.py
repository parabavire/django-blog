from django.contrib import admin #sugerido por deepseek
from django.urls import path, include #sugerido por deepseek
from .views import (
                    PublicationListView,
                    PublicationDetailView,
                    PublicationCreateView,
                    PublicationUpdateView,
                    PublicationDeleteView, #new
                    )

urlpatterns = [
    path("", PublicationListView.as_view(), name="publications-list"),
    path("publication/<int:pk>/", PublicationDetailView.as_view(), name="publication-detail"), #new
    path("publication/create/", PublicationCreateView.as_view(), name="publication-create"), #new
    path("publication/<int:pk>/update/", PublicationUpdateView.as_view(), name="publication-update"), #new
    path("publication/<int:pk>/delete/", PublicationDeleteView.as_view(), name="publication-delete"), #new
    path("admin/", admin.site.urls), #sugerido por deepseek
    #path("accounts/", include('django.contrib.auth.urls')), #sugerido por deepseek/va en urls de proyeco base
]