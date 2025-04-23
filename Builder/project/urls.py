from django.urls import path
from project.views import ProjectViewSet,PageViewSet

urlpatterns = [
    path('get/all/',ProjectViewSet.as_view({'get':'list'}),
        name='get-all-projects'),
    path('create/',ProjectViewSet.as_view({'post':'create'}),
        name='create3-projects'),
    path('page/create/',PageViewSet.as_view({'post':'create'}),
        name='create_page'),
    path('page/<page_id>',PageViewSet.as_view({'get':'list'}), name="Get-page"),
    path('page/update/<page_id>',PageViewSet.as_view({'put':'update'}),
        name="Update-page"),
    path('publish/<project_id>',ProjectViewSet.as_view({'post':'publish'}),
        name="Publish-project"),
    path('unpublish/<project_id>',ProjectViewSet.as_view({'post':'unpublish'}),
        name="Unpublish-project"),
    path('delete/<project_id>',ProjectViewSet.as_view({'delete':'delete'}),
        name="Delete-project"),
    
]
