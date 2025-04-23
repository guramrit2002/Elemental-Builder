from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .models import Project
from .utils import get_data, get_error_html
from .serializers import (ProjectListWithPagesSerializer, 
                                NewProjectSerializer,GetPageSerializer)
from .handler import ProjectHandler,PageHandler
# Create your views here.

class ProjectViewSet(ViewSet):
    
    def list(self,request):
        try:
            projects = Project.objects.filter(created_by = \
                request.user_data.get("id"))
            page_obj = ProjectListWithPagesSerializer(projects,many=True)
            return Response(page_obj.data)
        except Exception as e:
            import traceback
            traceback.print_exc()
            return Response({"errors" : str(e)})

    def create(self,request):
        data = request.data
        data.update({"created_by":request.user_data.get("id")})
        project, status= ProjectHandler.create_project(data)
        return Response(project,status=status)
    
    def publish(self,request,project_id):
        data = get_data(data=request.data)
        project, status = ProjectHandler.publish_project(project_id,data)
        return Response(project,status=status)
    
    def unpublish(self,request,project_id):
        data = get_data(data=request.data)
        message, status = ProjectHandler.unpublish_project(project_id)
        return Response(message,status=status)
    
    def delete(self,request,project_id):
        data = get_data(data=request.data)
        message, status = ProjectHandler.delete_project(project_id)
        return Response(message,status=status)
    
        
class PageViewSet(ViewSet):
    
    def create(self, request):
        data = get_data(data=request.data)
        page, status = PageHandler.create_page(data)
        return Response(page,status=status)
        
    def list(self,request,page_id):
        print("********* Page ID *********",page_id)
        is_html,html = PageHandler.get_html_linked(page_id)
        if not is_html:
            return HttpResponse(get_error_html(html))
        return HttpResponse(html)
    
    def update(self,request,page_id):
        data = get_data(data=request.data)
        updated_page, status = PageHandler.update_page(page_id,data)
        return Response({"message":"updated successfully","page":updated_page},
                        status=status)

    def delete(self,request,page_id):
        data = get_data(data=request.data)
        message, status = ProjectHandler.delete_page(page_id)
        return Response(message,status=status)
        