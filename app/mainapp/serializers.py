from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Idea


class IdeaModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Idea
        fields = '__all__'
