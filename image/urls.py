from django.conf.urls import url
from image.views import uploadimg, hots, photowall
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', uploadimg, name='imaguploading'),
    url(r'explore', hots, name='hotsexplore'),
    url(r'photowall', photowall, name='photowall'),
]
