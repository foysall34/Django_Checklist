
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('myapp/' , include('myapp.urls')),
    path('cloud/' , include('cloudi.urls')),
    path('g_auth/' , include('g_auth.urls')),
    path('auth/' , include('jwt_authen.urls')),
    path('chatbot/' , include('chatbot.urls')),
    path('addict/' , include('step_coach.urls')),
    path('', TemplateView.as_view(template_name='chat.html')),
    path('middleware/' , include('mymiddleware.urls'))
]
