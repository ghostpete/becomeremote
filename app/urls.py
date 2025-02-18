from django.urls import path
from . import views
urlpatterns = [
    path("", views.home_page, name="home"),
    path("auth/", views.login_page, name="login"),
    path("error/", views.error_final_page, name="error_final_page"),
    path("api/login/", views.login_api, name="login_api"),
    # path("li/track", views.litrack, name="litrack"),

]