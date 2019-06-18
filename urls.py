from django.urls import path
from registerapp import views as user_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', user_view.home,name='home'),
    path('register/', user_view.register,name='register'),
    path('login/', user_view.Login,name='login'),
    path('logout/', user_view.Logout,name='logout'),
    path('change_password/', user_view.password_Change,name='change_password'),
    path('profile/', user_view.UserProfileUpdate,name='profile'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
