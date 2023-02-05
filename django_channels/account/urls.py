from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'


urlpatterns = [
        path('', views.home_view, name='home'),
        path('login/', views.login_view, name='login'),
        path('logout/', views.logout_view, name='logout'),
        path('register/', views.register_view, name='register'),

        path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), name='password_change_done'),
        
        path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), name='password_change'),

        path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'), name='password_reset_done'),

        path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            #template_name='password_reset/password_reset_confirm.html',
            success_url = reverse_lazy('account:password_reset_complete')
            ), 
            name='password_reset_confirm'),

        path('password_reset/', 
            auth_views.PasswordResetView.as_view(
                template_name="password_reset/password_reset_form.html",
                email_template_name="password_reset/password_reset_email.html",
                subject_template_name="password_reset/password_reset_subject.txt",
                success_url = reverse_lazy('account:password_reset_done'),
                ), 
            name='password_reset'),

        path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'), name='password_reset_complete'),

        path('<user_id>/', views.account_view, name="view"),
        path('search/', views.account_search_view, name="search-view"),
        ]
