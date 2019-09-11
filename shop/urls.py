from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

app_name = 'shop'

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    path('register/',views.register),
    path('see/<int:id>/',views.see),
    path('viewall/',views.viewimg),
    path('register/',views.register),
    path('login/',views.login),
    path('contact/',views.emailView),
    path('search/',views.search),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)