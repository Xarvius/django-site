from django import forms
from user_manage.models import UserProfile, UserFolder, UserFiles, UserExtras, Results, UserPublications
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'phone', 'email', 'alias', 'qualification', 'USOSlink')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

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

class UserExtrasForm(forms.ModelForm):
    class Meta:
        model = UserExtras
        fields = ('intro', 'extras', 'education', 'hobbies')

class ResultsForm(forms.ModelForm):
    class Meta:
        model = Results
        fields = ('file_name', 'file')

class UserPublicationsForm(forms.ModelForm):
    class Meta:
        model = UserPublications
        fields = ('info',)