from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="CRM API",
        default_version='v1',
        description="This API is for the CRM App for Ekşioğlu Hukuk",
        contact=openapi.Contact(email="ibrahimoncelerwork@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
