from django.contrib import admin
from django.urls import path
from asosiy.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('xabarlar', xabarlar),

    # path('logout/', logoutview),
    # path('', loginview),
    # path('register/', register),

]
