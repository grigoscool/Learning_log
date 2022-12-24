from django.urls import path, include
from users import views
app_name = 'users'
urlpatterns = [
    # подключение стандартных url по умолчанию типо login logout
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register')

]