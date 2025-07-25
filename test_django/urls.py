
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('myapp/' , include('myapp.urls')),
    path('cloud/' , include('cloudi.urls')),
    path('g_auth/' , include('g_auth.urls')),
    path('auth/' , include('jwt_authen.urls')),
    path('chatbot/' , include('chatbot.urls')),
]
