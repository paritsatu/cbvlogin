from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic.base import TemplateView
from .views import BlogHomeView,pesan

urlpatterns = [
	url(r'^artikel/',include('artikel.urls',namespace='artikel')),
	url(r'^$',BlogHomeView.as_view(),name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^message/', pesan,name='message'),
]
