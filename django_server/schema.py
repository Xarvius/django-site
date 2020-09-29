import graphene
from graphene_django.types import DjangoObjectType
from django.contrib.auth.models import User
from user_manage.models import UserProfile, UserFolder, UserFiles, UserExtras, Results, UserPublications

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', )

class UserProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile
        fields  = ('id', 'first_name', 'last_name', 'user', 'phone', 'email', 'qualification', 'USOSlink')

    # def resolve_repository_url(self, info):
    #     return self.repository_url

class UserFolderType(DjangoObjectType):
    repository_url = graphene.Field(graphene.String)

    class Meta:
        model = UserFolder
        fields = ('name', 'user')

    def resolve_repository_url(self, info):
        return self.repository_url

class UserFilesType(DjangoObjectType):
    repository_url = graphene.Field(graphene.String)

    class Meta:
        model = UserFiles
        fields = ('file', 'folder')

    def resolve_repository_url(self, info):
        return self.repository_url

class UserExtrasType(DjangoObjectType):
    repository_url = graphene.Field(graphene.String)

    class Meta:
        model = UserExtras
        fields = ('user', 'intro', 'extras', 'education', 'hobbies')

    def resolve_repository_url(self, info):
        return self.repository_url

class ResultsType(DjangoObjectType):
    repository_url = graphene.Field(graphene.String)

    class Meta:
        model = Results
        fields = ('user', 'file_name', 'file')

    def resolve_repository_url(self, info):
        return self.repository_url

class UserPublicationsType(DjangoObjectType):
    repository_url = graphene.Field(graphene.String)

    class Meta:
        model = UserPublications
        fields = ('user', 'info',)

    def resolve_repository_url(self, info):
        return self.repository_url

class Query(graphene.ObjectType):
    profile = graphene.Field(UserProfileType, id= graphene.ID())
    profiles = graphene.List(UserProfileType)
    folders = graphene.List(UserFolderType)
    files = graphene.List(UserFilesType)
    extras = graphene.List(UserExtrasType)
    results = graphene.List(ResultsType)
    publications = graphene.List(UserPublicationsType, id=graphene.ID())

    def resolve_profile(self, info, id):
        try:
            return UserProfile.objects.get(id=id)
        except UserProfile.DoesNotExist:
            return none

    def resolve_profiles(self, info, **kwargs):
        return UserProfile.objects.all()

    def resolve_folders(self, info, **kwargs):
        return UserFolder.objects.all()

    def resolve_files(self, info, **kwargs):
        return UserFiles.objects.all()

    def resolve_extras(self, info, **kwargs):
        return UserExtras.objects.all()

    def resolve_results(self, info, **kwargs):
        return Results.objects.all()

    def resolve_publications(self, info, id):
        return UserPublications.objects.filter(user_id=id)

schema = graphene.Schema(query=Query)
