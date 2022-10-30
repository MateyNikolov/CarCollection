from django import forms

from CarCollection.car_app.models import Profile, Car


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields = ()

    def save(self, commit=True):
        if commit:
            Car.objects.all().delete()
            self.instance.delete()
        return self.instance

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password', 'first_name', 'last_name', 'profile_picture')


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class EditCarForm(BaseCarForm):
    pass


class DeleteCarForm(BaseCarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__make_fields_readonly()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __make_fields_readonly(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

