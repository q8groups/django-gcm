from django.conf.urls import patterns, url, include
from django.conf import settings
if(settings.INSTALLED_APPS.count('tastypie')>0):
    from tastypie.api import Api
    from gcm.resources import DeviceResource

    gcm_api = Api(api_name='v1')
    gcm_api.register(DeviceResource())
    urlpatterns = patterns('',url(r'^gcm/', include(gcm_api.urls)),)


if(settings.INSTALLED_APPS.count('rest_framework')>0):
    from .views import GCMListRegister,GCMListUnRegister
    urlpatterns = patterns('',url(r'^gcm/register/', GCMListRegister.as_view(),name='register-device'),url(r'^gcm/unregister/', GCMListUnRegister.as_view(),name='unregister-device'),)
