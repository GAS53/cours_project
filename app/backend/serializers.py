from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Idea, Feedback, JoinedUsers


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


