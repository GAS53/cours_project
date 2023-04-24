from rest_framework import viewsets, status, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework import filters

import frontend.serializers as fr_serializers
import backend.models as bk_models



class AbstractViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated', 'created']
    ordering = ['-updated']


class MakeNewUeser(AbstractViewSet):
    http_method_names = ('post')
    permission_classes = (AllowAny,)
    serializer_class = fr_serializers.NewUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class MinIdeasViewSet(AbstractViewSet):
    http_method_names = ('get')
    permission_classes = (AllowAny,) 
    serializer_class = fr_serializers.MinIdesSerializer


    def get_queryset(self):
        return bk_models.Idea.objects.all() 



class LoginViewSet(AbstractViewSet):
    serializer_class = fr_serializers.LoginSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class GetIdeaViewSet(AbstractViewSet):
    serializer_class = fr_serializers.GetIdeaSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']

    def get_object(self):
        obj = bk_models.Idea.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    

class PostIdeaViewSet(AbstractViewSet):
    serializer_class = fr_serializers.PostIdeaSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    
    def post(self, request):
        serializer = fr_serializers.PostIdeaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JoinToIdea(AbstractViewSet):
    serializer_class = fr_serializers.JoinedUserSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']


    def create(self, request, *args, **kwargs):
        serializer = fr_serializers.JoinedUserSerializer(data=request.data)
        if serializer.is_valid():
            obj = bk_models.JoinedUser.objects.filter(idea_id=request.data['idea'], user_id=request.data['user'])
            if obj:
                obj.delete()
                return Response(serializer.data, status=status.HTTP_423_LOCKED)
            else:
                serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LikesViewSet(AbstractViewSet):
    http_method_names = ('post')
    permission_classes = (AllowAny,)
    serializer_class = fr_serializers.LikesSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = fr_serializers.LikesSerializer(data=request.data)
        if serializer.is_valid():
            obj = bk_models.LikesToIdea.objects.filter(idea=request.data['idea'], autor=request.data['autor'])
            if obj:
                obj.delete()
                return Response(serializer.data, status=status.HTTP_423_LOCKED)
            else:
                serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class RefreshViewSet(viewsets.ViewSet, TokenRefreshView):
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return Response(serializer.validated_data, status=status.HTTP_200_OK)



class RegisterViewSet(viewsets.ViewSet):
    serializer_class = fr_serializers.RegisterSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = { "refresh": str(refresh),
        "access": str(refresh.access_token), }
        return Response({
            "user": serializer.data,
            "refresh": res["refresh"],
            "token": res["access"]},
            status=status.HTTP_201_CREATED)




class NewRubricViewSet(AbstractViewSet):
    http_method_names = ('post',)
    permission_classes = (IsAuthenticated,)
    serializer_class = fr_serializers.RubricSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = self.perform_create(serializer)
        if res:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_304_NOT_MODIFIED)

    def perform_create(self, serializer):
        new_rubric = self.request.data.get("rubirc_name", None) # read data from request
        preparate_qs =[val[-1] for val in bk_models.Rubric.objects.all().values_list()]
        if new_rubric in preparate_qs:
            return False
        else:
            serializer.save()
            return True


class AllRubricsViewSet(AbstractViewSet):
    http_method_names = ('get',)
    permission_classes = (IsAuthenticated,)
    serializer_class = fr_serializers.RubricSerializer


    def get_queryset(self):
        return bk_models.Rubric.objects.all()



