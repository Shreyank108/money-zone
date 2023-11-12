from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.shortcuts import render, HttpResponse, redirect
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.http import require_POST
from money_zone import settings
from .tokens import generate_token

User = get_user_model()

# Create your views here.


@require_POST
def signup(request):
    username = request.POST.get('username')
    fname, lname = request.POST.get('name').split()
    email = request.POST.get('email')
    type = request.POST.get('type')
    passw = request.POST.get('passw')
    con_passw = request.POST.get('con_passw')

    if len(User.objects.filter(username=username)) > 0:
        messages.error(
            request, "Username already exist. Please try other username.")
        return HttpResponse('Username already exist. Please try other username.')

    if len(User.objects.filter(email=email)) > 0:
        messages.error(
            request, "Email already Registered. Please try other username.")
        return HttpResponse('Email already Registered. Please try other username.')

    if passw != con_passw:
        messages.error(request, "Passwords didn't match")
        return HttpResponse("Passwords do not match")

    if not username.isalnum():
        messages.error(request, "Username must be alpha numberic.")
        return HttpResponse('Username must be alpha numberic.')

    user = User.objects.create(
        username=username,
        phone_number=None,
        profile_image=None,
        email=email,
        type=int(type)
    )

    user.set_password(passw)
    user.first_name = fname
    user.last_name = lname
    user.is_active = False
    user.save()
    messages.success(
        request, "Your account has been successfully created.")

    # Welcome email

    subject = "Welcome to Money Zone"
    message = "Hello " + user.first_name + "!! \n" + \
        "Welcome to Money Zone!! \n Thanks you for visiting our website \n We have also sent you a confirmation email, please confirm your email address in order to confirm your account. \n\n Thanking you\n"
    from_email = settings.EMAIL_HOST_USER
    to_list = [user.email]
    send_mail(subject, message, from_email, to_list, fail_silently=True)

    # Confirmation email
    current_site = get_current_site(request)
    email_subject = "Confirm your email @ Money Zone - Login"
    message2 = render_to_string("auth/email_confirmation.html", {
        'name': user.first_name,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })
    email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [user.email],
    )

    email.fail_silently = True
    email.send()

    return redirect('home')


@require_POST
def signin(request):
    username = request.POST.get('username')
    passw = request.POST.get('passw')

    user = authenticate(username=username, password=passw)

    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        messages.error(request, "Bad Creadentials")
        return redirect('home')


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('home')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and generate_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'auth/activation_failed.html')
