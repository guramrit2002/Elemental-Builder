from rest_framework.response import Response
from rest_framework import status

from .handlers.html_handler import HTMLhandler
from .utils import get_error_html, get_saved_html, get_published_url
from .serializers import NewProjectSerializer,GetPageSerializer
from .models import Page, Project

class ProjectHandler:
    
    @classmethod
    def create_project(cls, data: dict) -> None:
        try:
            page_obj = NewProjectSerializer(data = data)
            
            if page_obj.is_valid():
                print("******** New Project Is Created ********")
                page_obj.save()
                return {"project":page_obj.data}, status.HTTP_201_CREATED
            else:
                if page_obj.errors.get("name"):
                    return {"errors":\
                        str(page_obj.errors.get("name")[0].string)}
                return {"errors":page_obj.errors}, status.HTTP_201_CREATED
        except Exception as e:
            import traceback
            traceback.print_exc()
            return {"errors": str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR
    
    @classmethod
    def publish_project(cls, project_id: int, data: dict, page_id = None) -> None:
        try:            
            project = Project.objects.get(id=project_id)
            
            if project:
                
                if page_id:
                    page, status = PageHandler.create_page(data.\
                        get("json_data"))
                
                project.is_published = True
                project.save()
                return ({"message": "Project published successfully",
                        "published_url":get_published_url(project.id)}, 
                        status.HTTP_200_OK)
            else:
                return ({"errors": "Project not found"}, 
                        status.HTTP_404_NOT_FOUND)

        except Exception as e:
            import traceback
            traceback.print_exc()
            return {"errors": str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR
    
    @classmethod
    def unpublish_project(cls, project_id: int) -> None:
        try:
            project = Project.objects.get(id=project_id)
            
            if project:
                project.is_published = False
                project.save()
                return ({"message": "Project unpublished successfully"},
                        status.HTTP_200_OK)
            else:
                return ({"errors": "Project not found"},
                        status.HTTP_404_NOT_FOUND)

        except Exception as e:
            import traceback
            traceback.print_exc()
            return {"errors": str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR
   
    @classmethod
    def delete_project(cls, project_id: int) -> None:
        try:
            project = Project.objects.get(id=project_id)
            
            if project:
                project.delete()
                return ({"message": "Project deleted successfully"}, 
                        status.HTTP_200_OK)
            else:
                return ({"errors": "Project not found"}, 
                        status.HTTP_404_NOT_FOUND)

        except Exception as e:
            import traceback
            traceback.print_exc()
            return {"errors": str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR
        
class PageHandler:
    
    @classmethod
    def create_page(cls, data: dict) -> None:
        try:
            serializer = GetPageSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return serializer.data, status.HTTP_201_CREATED

            return {"errors": serializer.errors}, status.HTTP_400_BAD_REQUEST

        except Exception as e:
            import traceback
            traceback.print_exc()
            return {"errors": str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR
    
    @classmethod
    def get_html_linked(self, page_id):
        try:
            print("********* Page ID *********",page_id)
            is_html,html = get_saved_html(page_id)
            print("********* HTML is fetched *********",is_html)
            return is_html, html
        except Exception as e:
            print("********* Error in Get HTML *********")
            print(e)
            import traceback
            traceback.print_exc()
            return get_error_html(str(e))
    
    @classmethod
    def update_page(cls, page_id: int, data: dict) -> None:
        try:
            page = Page.objects.get(id=page_id)
            
            if page:
                html_obj = HTMLhandler()
                page.content = data
                page.html = html_obj.get_html(data)
                page.save()
                page_obj = GetPageSerializer(page)
                return page_obj.data, status.HTTP_200_OK
            else:
                return {"errors": "Page not found"}, status.HTTP_404_NOT_FOUND

        except Exception as e:
            print("********* Error in Update Page *********")
            print(e)
            import traceback
            traceback.print_exc()
            return {"errors": str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR
        
    @classmethod
    def delete_page(cls, page_id: int) -> None:
        try:
            page = Page.objects.get(id=page_id)
            
            if page:
                page.delete()
                return({"message": "Page deleted successfully"},
                    status.HTTP_200_OK)
            else:
                return {"errors": "Page not found"}, status.HTTP_404_NOT_FOUND

        except Exception as e:
            print("********* Error in Delete Page *********")
            print(e)
            import traceback
            traceback.print_exc()
            return {"errors": str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR