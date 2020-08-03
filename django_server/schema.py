from user_manage.models import UserProfile, UserFolder, UserFiles
import graphene
from graphene_django.types import DjangoObjectType


class UserProfileType(DjangoObjectType):
    repository_url = graphene.Field(graphene.String)
    class Meta:
        model = UserProfile
        fields = (
            'first_name', 'last_name', 'phone', 'date_begin', 'qualification', 'education', 'publications', 'extras')

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

class Query(graphene.ObjectType):
    profile = graphene.List(UserProfileType)
    folders = graphene.List(UserFolderType)
    files = graphene.List(UserFilesType)

    def resolve_profile(self, info, **kwargs):
        return UserProfile.objects.all()

    def resolve_folders(self, info, **kwargs):
        return UserFolder.objects.all()

    def resolve_files(self, info, **kwargs):
        return UserFiles.objects.all()

schema = graphene.Schema(query=Query)
