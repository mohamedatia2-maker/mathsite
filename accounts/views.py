from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from .models import UserActivity

# تسجيل جديد
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            return HttpResponse("المستخدم موجود بالفعل. جرب تسجل دخول.")
        
        user = User.objects.create_user(username=username, password=password)
        user.save()
        UserActivity.objects.create(user=user, action='signup')
        return redirect('login')
    return render(request, 'signup.html')

# تسجيل الدخول
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            UserActivity.objects.create(user=user, action='login')
            return redirect('index')
        else:
            return HttpResponse("بيانات غير صحيحة.")
    return render(request, 'login.html')

# تسجيل الخروج
def logout_view(request):
    if request.user.is_authenticated:
        UserActivity.objects.create(user=request.user, action='logout')
    logout(request)
    return redirect('login')

# لوحة التحكم
@staff_member_required
def dashboard_view(request):
    activities = UserActivity.objects.select_related('user').order_by('-timestamp')[:50]
    return render(request, 'dashboard.html', {'activities': activities})

# الصفحات
def index_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'index.html')

def years_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'years.html')

def first_year_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'first_year.html')

def first_year_unit1(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'first_year_unit1.html')

def first_year_unit2(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'first_year_unit2.html')

def first_year_unit3(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'first_year_unit3.html')

def first_year_unit4(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'first_year_unit4.html')

def first_year_unit4_functions(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'first_year_unit4_functions.html')

def first_year_unit5_calculus(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'first_year_unit5_calculus.html')

def first_year_unit6_statistics(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'first_year_unit6_statistics.html')

def second_year_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'second_year.html')

def second_year_unit1(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'second_year_unit1.html')

def second_year_unit2(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'second_year_unit2.html')
def second_year_unit3(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'second_year_unit3.html')

def second_year_unit4(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'second_year_unit4.html')

def second_year_unit1_applied(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'second_year_unit1_applied.html')

def second_year_unit2_applied(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'second_year_unit2_applied.html')
def second_year_unit4_pure(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'second_year_unit4_pure.html')

def second_year_unit5_applied(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'second_year_unit5_applied.html')

def second_year_unit6_applied(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'second_year_unit6_applied.html')
def third_year_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'third_year.html')

def third_year_unit1(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'third_year_unit1.html')

def third_year_unit2(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'third_year_unit2.html')

def tests_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'tests.html')

def game_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'game.html')

def contact_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'contact.html')