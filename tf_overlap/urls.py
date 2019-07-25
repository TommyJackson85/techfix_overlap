"""django_auth URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.static import serve
from .settings import MEDIA_ROOT
from accounts.views import index
from accounts import urls as accounts_urls
from cart import urls as cart_urls
from charts import urls as charts_urls
from checkout import urls as urls_checkout

#maybe replace with url(r'^$', RedirectView.as_view(url='posts/')),
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^bugs/', include('bugs.urls')),
    url(r'^features/', include('features.urls')),
    url(r'^cart/', include(cart_urls)),
    url(r'^charts/', include(charts_urls)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
]


