from django.urls import path, include
from .views import *

app_name = 'menu'

urlpatterns = [
    path('addMenu/', AddMenu.as_view(), name='addMenu'),
    path('showMenus/', ShowMenus.as_view(), name='showMenus'),
    path('addStore/', AddStore.as_view(), name='addStore'),
    path('showStores/', ShowStore.as_view(), name='showStores'),
    path('showStores/<str:store_name>', StoreDetail.as_view(), name='detail')
]