from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from django_server.settings import TEMPLATE_DIR
from user_manage import models
from user_manage.forms import UserForm, UserProfileForm, UserFolderForm, UserFilesForm, UserExtrasForm, ResultsForm, \
    UserPublicationsForm


def home(request):
    return render(request, f'{TEMPLATE_DIR}/_homepage.html', {})

@login_required(login_url='../user_login/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            # more?
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, f'{TEMPLATE_DIR}/pages/register.html',
                  {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered':registered
                   })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return  HttpResponse('Your account was inactive.')
        else:
            print('Failed login', f'on user:{username} pass:{password}')
            return HttpResponse('Invalid login')
    else:
        return render(request, f'{TEMPLATE_DIR}/pages/login.html')

@login_required(login_url='../user_login/')
def user_profile(request):
    user = request.user
    instance = models.UserProfile.objects.get(user=user)
    edited = False
    if request.method == 'POST':
        profile_form = UserProfileForm(data=request.POST, instance=instance)
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        edited = True
    else:
        profile_form = UserProfileForm(instance=instance)
    return render(request, f'{TEMPLATE_DIR}/pages/profile.html', {'profile_form':profile_form,
                                                                  'edited':edited})

@login_required(login_url='../user_login/')
def upload_files(request):
    user = request.user
    saved = False
    if request.method == 'POST':
        files_form = UserFilesForm(request.POST, request.FILES)
        if files_form.is_valid():
            files = files_form.save(commit=False)
            files.user = user
            files.save()
            saved = True
    else:
        files_form = UserFilesForm()
    return render(request, f'{TEMPLATE_DIR}/pages/upload_files.html', {'files_form':files_form,
                                                                       'saved':saved})

@login_required(login_url='../user_login/')
def create_folder(request):
    user = request.user
    saved = False
    if request.method == 'POST':
        folder_form = UserFolderForm(data=request.POST)
        if folder_form.is_valid():
            folder = folder_form.save(commit=False)
            folder.user = user
            folder.save()
            saved = True
    else:
        folder_form = UserFolderForm()
    return render(request, f'{TEMPLATE_DIR}/pages/create_folder.html', {'folder_form':folder_form,
                                                                       'saved':saved})

@login_required(login_url='../user_extras/')
def create_extras(request):
    user = request.user
    saved = False
    if request.method == 'POST':
        extras_form = UserExtrasForm(data=request.POST)
        if extras_form.is_valid():
            extras = extras_form.save(commit=False)
            extras.user = user
            extras.save()
            saved = True
    else:
        extras_form = UserExtrasForm()
    return render(request, f'{TEMPLATE_DIR}/pages/extras.html', {'extras_form':extras_form,
                                                                       'saved':saved})

@login_required(login_url='../exam_results/')
def upload_results(request):
    user = request.user
    saved = False
    if request.method == 'POST':
        results_form = ResultsForm(data=request.POST)
        if results_form.is_valid():
            results = results_form.save(commit=False)
            results.user = user
            results.save()
            saved = True
    else:
        results_form = ResultsForm()
    return render(request, f'{TEMPLATE_DIR}/pages/results.html', {'results_form':results_form,
                                                                       'saved':saved})

@login_required(login_url='../publications/')
def create_publications(request):
    user = request.user
    saved = False
    if request.method == 'POST':
        publications_form = UserPublicationsForm(data=request.POST)
        if publications_form.is_valid():
            publications = publications_form.save(commit=False)
            publications.user = user
            publications.save()
            saved = True
    else:
        publications_form = UserPublicationsForm()
    return render(request, f'{TEMPLATE_DIR}/pages/publications.html', {'publications_form':publications_form,
                                                                       'saved':saved})