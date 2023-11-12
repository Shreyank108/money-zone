from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ImageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["profile_image"]