from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Years and Units
    path('years/', views.years_view, name='years'),
    path('years/first/', views.first_year_view, name='first_year'),
    path('years/first/unit1/', views.first_year_unit1, name='first_year_unit1'),
    path('years/first/unit2/', views.first_year_unit2, name='first_year_unit2'),
    path('years/first/unit3/', views.first_year_unit3, name='first_year_unit3'),
    path('years/first/unit4/', views.first_year_unit4, name='first_year_unit4'),
    path('years/first/unit4-functions/', views.first_year_unit4_functions, name='first_year_unit4_functions'),
    path('years/first/unit5-calculus/', views.first_year_unit5_calculus, name='first_year_unit5_calculus'),
    path('years/first/unit6-statistics/', views.first_year_unit6_statistics, name='first_year_unit6_statistics'),
    path('years/second/', views.second_year_view, name='second_year'),
    path('years/second/unit1/', views.second_year_unit1, name='second_year_unit1'),
    path('years/second/unit2/', views.second_year_unit2, name='second_year_unit2'),
    path('years/second/unit3/', views.second_year_unit3, name='second_year_unit3'),
    path('years/second/unit4/', views.second_year_unit4, name='second_year_unit4'),
    path('years/second/unit1-applied/', views.second_year_unit1_applied, name='second_year_unit1_applied'),
    path('years/second/unit2-applied/', views.second_year_unit2_applied, name='second_year_unit2_applied'),
    path('years/second/unit4-pure/', views.second_year_unit4_pure, name='second_year_unit4_pure'),
    path('years/second/unit5-applied/', views.second_year_unit5_applied, name='second_year_unit5_applied'),
    path('years/second/unit6-applied/', views.second_year_unit6_applied, name='second_year_unit6_applied'),
    path('years/third/', views.third_year_view, name='third_year'),
    path('years/third/unit1/', views.third_year_unit1, name='third_year_unit1'),
    path('years/third/unit2/', views.third_year_unit2, name='third_year_unit2'),

    # Main pages
     path('', views.index_view, name='index'),   # الصفحة الرئيسية
    path('', views.index_view, name='home'),    # alias عشان أي كود قديم يشتغل
    path('tests/', views.tests_view, name='tests'),
    path('game/', views.game_view, name='game'),
    path('contact/', views.contact_view, name='contact'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]