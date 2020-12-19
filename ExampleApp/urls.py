"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from DjangoControllers.urls import Methods

from ExampleApp import ExampleController

urlpatterns = [
    path('', Methods(
        GET=ExampleController.get_view,
        POST=ExampleController.post_view,
        DELETE=ExampleController.delete_view,
    )),
    path('<int:model_id>/', Methods(
        GET=ExampleController.get_specific_view,
    )),
]
