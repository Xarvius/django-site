import graphene
from graphene_django.types import DjangoObjectType

from user_manage.models import UserProfile, UserFolder, UserFiles, UserExtras, Results, UserPublications


class UserProfileType(DjangoObjectType):
    repository_url = graphene.Field(graphene.String)
    class Meta:
        model = UserProfile
        fields  = ('first_name', 'last_name', 'phone', 'email', 'qualification', 'USOSlink')

    def resolve_repository_url(self, info):
        return self.repository_url

class UserFolderType(DjangoObjectType):
    repository_url = graphene.Field(graphene.String)

    class Meta:
        model = UserFolder
        fields = ('name',)

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
        fields = ('intro', 'extras', 'education', 'hobbies')

    def resolve_repository_url(self, info):
        return self.repository_url

class ResultsType(DjangoObjectType):
    repository_url = graphene.Field(graphene.String)

    class Meta:
        model = Results
        fields = ('file_name', 'file')

    def resolve_repository_url(self, info):
        return self.repository_url

class UserPublicationsType(DjangoObjectType):
    repository_url = graphene.Field(graphene.String)

    class Meta:
        model = UserPublications
        fields = ('info',)

    def resolve_repository_url(self, info):
        return self.repository_url

class Query(graphene.ObjectType):
    profile = graphene.Field(UserProfileType, last_name=graphene.String(required=True))
    folders = graphene.List(UserFolderType)
    files = graphene.List(UserFilesType)
    extras = graphene.List(UserExtrasType)
    results = graphene.List(ResultsType)
    publications = graphene.List(UserPublicationsType)

    def resolve_profile(self, info, last_name):
        try:
            return UserProfile.objects.get(last_name=last_name)
        except UserProfile.DoesNotExist:
            return none

    def resolve_folders(self, info, **kwargs):
        return UserFolder.objects.all()

    def resolve_files(self, info, **kwargs):
        return UserFiles.objects.all()

    def resolve_extras(self, info, **kwargs):
        return UserExtras.objects.all()

    def resolve_results(self, info, **kwargs):
        return Results.objects.all()

    def resolve_publications(self, info, **kwargs):
        return UserPublications.objects.all()

schema = graphene.Schema(query=Query)
