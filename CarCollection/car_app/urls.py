from django.urls import path, include

from CarCollection.car_app.views import show_home_page, profile_create, profile_details, profile_edit, profile_delete, \
    show_catalogue, car_create, car_details, car_edit, car_delete

urlpatterns = [
    path('', show_home_page, name='index'),
    path('profile/', include([
        path('create/', profile_create, name='create profile'),
        path('details/', profile_details, name='details profile'),
        path('edit/', profile_edit, name='edit profile'),
        path('delete/', profile_delete, name='delete profile'),
    ])),
    path('catalogue/', show_catalogue, name='catalogue page'),
    path('car/create/', car_create, name='create car'),
    path('car/<int:pk>/', include([
        path('details/', car_details, name='details car'),
        path('edit/', car_edit, name='car edit'),
        path('delete/', car_delete, name='delete car'),
    ]))
]