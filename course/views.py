from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Earning, Package
from .serializer import EarningSerializer
from django.contrib.auth import get_user_model
import collections

User = get_user_model()

# Create your views here.


@api_view(["GET"])
def getData(request):
    earned = Earning.objects.all().order_by('-earned')
    top_earned = earned[:10]
    serializer = EarningSerializer(earned, many=True)
    top_users = serializer.data
    for i in range(len(earned)):
        top_users[i] = collections.OrderedDict(top_users[i])
        username = ('username', top_earned[i].user.get_username())
        items = list(top_users[i].items())
        items.append(username)
        try:
            image = ('image', top_earned[i].user.profile_image.url)
            items.append(image)
        except Exception:
            items.append(('image', ""))
        items.sort()
        top_users[i] = collections.OrderedDict(items)
    return Response(top_users)


def manage_site(request):
    return render(request, 'admin/manage_site.html')


def view_package(request, slug):
    queryset = Package.objects.get(slug=slug)
    context = {
        'package': queryset
    }
    return render(request, 'course/view_package.html', context)


def add_package(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        desc = request.POST.get('desc')

        package = Package.objects.create(name=name, price=price, image=image, description = desc)
        package.save()
        return redirect('manage-site')