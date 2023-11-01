from django.urls import path, include
from start.views import welcome, dice, dice_bag, tray

urlpatterns = [
    path('', welcome, name='inicio'),
    path('dados/', dice, name='dice'),
    path('bolsas/', dice_bag, name='bags'),
    path('bandejas/', tray, name='trays')
]
