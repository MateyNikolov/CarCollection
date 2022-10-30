from django.shortcuts import render, redirect

from CarCollection.car_app.forms import BaseProfileForm, BaseCarForm, EditCarForm, DeleteCarForm, EditProfileForm, \
    DeleteProfileForm
from CarCollection.car_app.models import Profile, Car


def get_profile():
    try:
        profile = Profile.objects.get()
        return profile
    except Profile.DoesNotExist as ex:
        return None


def show_home_page(request):

    if not get_profile():
        return redirect('create profile')

    context = {
        'profile': get_profile(),
    }

    return render(
        request,
        'home/index.html',
        context,
    )


def profile_create(request):
    if request.method == 'GET':
        form = BaseProfileForm()
    else:
        form = BaseProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')

    context = {
        'profile': get_profile(),
        'form': form,
    }

    return render(
        request,
        'profile/profile-create.html',
        context
    )


def profile_details(request):
    if not get_profile():
        return redirect('create profile')
    profile = get_profile()
    all_cars = Car.objects.all()
    total_price = 0
    if all_cars:
        for car in all_cars:
            total_price += car.price
    full_name = None
    if profile.first_name and profile.last_name:
        full_name = f"{profile.first_name} {profile.last_name}"

    context = {
        'profile': profile,
        'total_price': total_price,
        'full_name': full_name,
    }
    return render(request,
                  'profile/profile-details.html',
                  context
                  )


def profile_edit(request):
    if not get_profile():
        return redirect('create profile')
    profile = get_profile()
    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(
        request,
        'profile/profile-edit.html',
        context
    )


def profile_delete(request):
    if not get_profile():
        return redirect('create profile')

    profile = get_profile()

    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(
        request,
        'profile/profile-delete.html',
        context)


def show_catalogue(request):
    if not get_profile():
        return redirect('create profile')

    current_cars = Car.objects.all()
    current_cars_count = Car.objects.count()

    context = {
        'profile': get_profile(),
        'cars': current_cars,
        'cars_count': current_cars_count,
    }

    return render(
        request,
        'home/catalogue.html',
        context
    )


def car_create(request):
    if not get_profile():
        return redirect('create profile')
    if request.method == 'GET':
        form = BaseCarForm()
    else:
        form = BaseCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')

    context = {
        'profile': get_profile(),
        'form': form,
    }

    return render(
        request,
        'car/car-create.html',
        context
    )


def car_details(request, pk):
    if not get_profile():
        return redirect('create profile')

    current_car = Car.objects.get(pk=pk)

    context = {
        'profile': get_profile(),
        'car': current_car
    }

    return render(
        request,
        'car/car-details.html',
        context
    )


def car_edit(request, pk):
    if not get_profile():
        return redirect('create profile')

    current_car = Car.objects.get(pk=pk)

    if request.method == 'GET':
        form = EditCarForm(instance=current_car)
    else:
        form = EditCarForm(request.POST, instance=current_car)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')

    context = {
        'profile': get_profile(),
        'car': current_car,
        'form': form,
    }

    return render(
        request,
        'car/car-edit.html',
        context
    )


def car_delete(request, pk):
    if not get_profile():
        return redirect('create profile')

    current_car = Car.objects.get(pk=pk)

    if request.method == 'GET':
        form = DeleteCarForm(instance=current_car)
    else:
        form = DeleteCarForm(request.POST, instance=current_car)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')

    context = {
        'profile': get_profile(),
        'car': current_car,
        'form': form,
    }

    return render(
        request,
        'car/car-delete.html',
        context
    )

