from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Idea, Feedback, JoinedUsers, LikesToIdeas


class IdeaModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Idea
        fields = '__all__'


class FeedbackModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class JoinedUsersModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = JoinedUsers
        fields = '__all__'


class LikesToIdeasModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = LikesToIdeas
        fields = '__all__'
