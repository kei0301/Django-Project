from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include('account.urls')),
    path('inbox/', include('inbox.urls')),
    path('templates/', include('templates.urls')),
    path('error/', include('error.urls')),
    path('', include('privatedns.urls'))

]
