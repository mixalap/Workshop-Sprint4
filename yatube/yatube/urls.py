from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('notes/', include('notes.urls')),
    # path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    # path("", include("notes.urls")),

]
