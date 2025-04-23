from rest_framework import serializers
from .models import Project, Page

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        exclude = ['project']
    
class GetPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'

class ProjectListWithPagesSerializer(serializers.ModelSerializer):
    pages = PageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'created_by', 'created_on', 'pages']

class NewProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['name', 'created_by']
        