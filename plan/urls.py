from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', views.home, name='home'),
    path('same-areas/<str:width>/<str:height>', views.same_areas, name='same-areas'),
    path('individual-plan/<int:args>', views.individual_plan, name='individual-plan'),
    path('payment/<int:pk>/', views.payment, name='payment'),
    path('charge/<int:id>/', views.charge, name='charge'),
    path('success/<str:amount>/<str:newid>/', views.successMsg, name='success'),
    path('register/', views.register, name='register-page'),
    path('login/', auth_view.LoginView.as_view(template_name='plan/login.html'), name='login-page'),
    path('logout/', auth_view.LogoutView.as_view(template_name='plan/logout.html'), name='logout-page'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)