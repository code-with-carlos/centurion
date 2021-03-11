from django import forms
from MainDirectories import models as main_models


class SignupForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = main_models.UserProfile
        fields = ['user_type']

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        user_type = self.cleaned_data['user_type']
        main_models.UserProfile.objects.create(user=user, user_type=user_type)
        