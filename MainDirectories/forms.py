from django import forms
from MainDirectories import models as main_models
from Crypto.PublicKey import RSA


class SignupForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = main_models.UserProfile
        fields = []

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        key = RSA.generate(2048)
        pubkey = key.public_key()

        main_models.UserProfile.objects.create(user=user, publickeygen=pubkey.export_key() , privatekeygen=key.export_key())
        