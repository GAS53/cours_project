from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Idea, Feedback


class IdeaModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Idea
        fields = '__all__'


class FeedbackModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

