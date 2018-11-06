from django.contrib import admin
from django.urls import path
from main_app import views
urlpatterns = [
    path('', views.index,name='home'),
    path('admin/', admin.site.urls),
    path('login/',views.user_login,name="login"),
    path('register/', views.signup),
    path('profile/',views.Profile,name="profile"),
    path('logout',views.logouty,name="logout")
]
