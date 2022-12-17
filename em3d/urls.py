from django.contrib import admin
from django.urls import path, include
from design.views import (Save_Design, Retrieve_Designs_List, 
                        Retrieve_Design, Trending_Design, Add_Item, Retrieve_Item_List, Disike_Design, Like_Design)
# from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# api_documentation_schema_view = get_swagger_view(title = "Embedded3D API Endpoints Documentation")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', include("search.urls")),
    # path('documentation/', api_documentation_schema_view, name = "documentation"),
    path('save/design/', Save_Design.as_view(), name='save'),
    path('designs/', Retrieve_Designs_List.as_view(), name='designs'),
    path('designs/like/<id:design>/', Like_Design.as_view(), name='like'),
    path('designs/dislike/<id:design>/', Disike_Design.as_view(), name='dislike'),
    path('design/<str:name>/', Retrieve_Design.as_view(), name='design'),
    path('trending/', Trending_Design.as_view(), name='trending'),
    path('save/item/', Add_Item.as_view(), name='save-item'),
    path('items/', Retrieve_Item_List.as_view(), name='items'),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
