from django.urls import path

from .views import *


app_name="dashboard"

urlpatterns = [
    path("admin/page/", index, name="home_page"),
    path("teller/page/",teller_view, name="teller_page"),
]