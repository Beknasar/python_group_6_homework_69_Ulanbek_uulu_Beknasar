"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api_v1.views import index_view, json_add_view, json_subtract_view, json_multiply_view, json_divide_view, \
    get_token_view

urlpatterns = [
    path('', index_view),
    path('admin/', admin.site.urls),
    path('add/', json_add_view, name='add'),
    path('subtract/', json_subtract_view, name='subtract'),
    path('multiply/', json_multiply_view, name='multiply'),
    path('divide/', json_divide_view, name='divide'),
    path('get_token/', get_token_view)
]
