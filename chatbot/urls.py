from django.conf.urls import url
from django.contrib import admin
from chatbotapp.views import ChatBotView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', ChatBotView.as_view())
]
