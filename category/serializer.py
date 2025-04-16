from rest_framework import routers, serializers, viewsets

from category.models import Categorie

# Serializers define the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id','name', 'status', 'created_at']