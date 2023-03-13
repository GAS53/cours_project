from rest_framework.serializers import HyperlinkedModelSerializer
from .models import ShopUser


class ShopUserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShopUser
        fields = '__all__'