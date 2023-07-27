from django.contrib import admin
from django.urls import path, include
from authentication.views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls.static import static


schema_view = get_schema_view(
   openapi.Info(
      title="E-Commerce API",
      default_version='v1',
      description="API for E-Commerce Telegram Bot",
      terms_of_service="",
      contact=openapi.Contact(email="info@quantumbot.in"),
      license=openapi.License(name="QB E-Commerce Bot"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', include('products.urls')),
    path('api/category/', include('category.urls')),
    path('api/cart/', include('carts.urls')),
    path('signup/', RegistrationView.as_view({'get': 'list', 'post': 'create'})),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),   name='schema-swagger-ui'),
    path('login/', Login),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)