from django.shortcuts import render, redirect
from .models import Company, Founder
from course.models import Package, Course, PackageTaken, Earning
from .forms import ImageForm
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST
from rest_framework.response import Response
from rest_framework.decorators import api_view

User = get_user_model()

# Create your views here.


def home(request):
    package = Package.objects.all()
    company = Company.objects.all()[0]
    founder = Founder.objects.all()[0]
    all_courses = Course.objects.all()
    course = Course.objects.all().order_by('likes')[:3]
    instructor = User.objects.filter(type=1)
    context = {
        "package": package,
        "company": company,
        "founder": founder,
        "course": course,
        "instructor": instructor,
        "all_courses": all_courses
    }
    return render(request, 'index.html', context)


def dashboard(request):
    if request.user.is_authenticated:
        package_taken = PackageTaken.objects.filter(user_id=request.user.id)
        package_id = package_taken[0].package.pk
        course = Course.objects.filter(package__id=package_id)
        context = {
            'course': course,
        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect('home')


def user_profile(request):
    form = ImageForm()
    context = {
        'form': form,
    }
    return render(request, 'user_profile.html', context)


@require_POST
def set_links(request):
    website = request.POST.get('website')
    instagram = request.POST.get('instagram')
    facebook = request.POST.get('facebook')
    username = request.user.username
    User.objects.filter(username=username).update(
        website=website, instagram=instagram, facebook=facebook)
    return redirect('user_profile')


@require_POST
def set_profile_image(request):
    current_user = User.objects.get(id=request.user.id)
    image_form = ImageForm(request.POST or None,
                           request.FILES or None, instance=current_user)
    if image_form.is_valid():
        image_form.save()
    return redirect('user_profile')


def admin_dashboard(request):
    return render(request, 'course/admin_dashboard.html')


def leaderboard(request):
    if request.user.is_authenticated:
        earn = Earning.objects.filter(user__id=request.user.id)
        context = {
            'earn': earn[0]
        }
    return render(request, 'leaderboard.html', context)
