from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        #Se pone todos los campos del modelo de Project
        read_only_field = ('created_at',)
        #Indico cuál campo no se puede hacer operación de actualizar o eliminar.