from django.urls import path, include
from .views import *
from django.views.generic import TemplateView

app_name = 'menu'

urlpatterns = [
    path('', TemplateView.as_view(template_name='menu/index.html'), name='index'),
    path('single/', TemplateView.as_view(template_name='menu/single.html'), name='single'),
    path('addMenu/', AddMenu.as_view(), name='addMenu'),
    path('showMenus/', ShowMenus.as_view(), name='showMenus'),
    path('addStore/', AddStore.as_view(), name='addStore'),
    path('showStores/', ShowStore.as_view(), name='showStores'),
    path('showStores/<str:store_name>', StoreDetail.as_view(), name='detail')
]