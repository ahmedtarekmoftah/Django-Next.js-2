from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('country/<int:pk>', views.country_detail_view),
    path('country', views.country_list_create_view),
    path('country/update/<int:pk>', views.country_update_view),
    path('country/destroy/<int:pk>', views.country_destroy_view),


]
