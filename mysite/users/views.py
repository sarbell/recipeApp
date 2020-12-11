from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm, UpdateProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Profile


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Welcome {username}!')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile_page(request):
    return render(request, 'users/profile.html')


@login_required()
def profile_update(request):
    user = get_object_or_404(User, id=request.user.id)

    if request.method== 'POST':
        image = request.FILES.got('image', )

        updated_profile = Profile(user=user, image=image)
        updated_profile.save()
        return redirect('recipeApp:profile_page')

    return render(request, 'users/profile_update.html', {'user':user})
