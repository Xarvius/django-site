from django import forms
from user_manage.models import UserProfile, UserFolder, UserFiles
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'phone', 'date_begin', 'qualification', 'education', 'publications', 'extras')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['publications'].required = False
        self.fields['extras'].required = False

class UserFolderForm(forms.ModelForm):
    class Meta:
        model = UserFolder
        fields = ('name',)

class UserFilesForm(forms.ModelForm):
    class Meta:
        model = UserFiles
        fields = ('file', 'folder')

    def __init__(self, *args, **kwargs):
        super(UserFilesForm, self).__init__(*args, **kwargs)
        self.fields['folder'].label_from_instance = lambda obj: f"{obj.name}"
