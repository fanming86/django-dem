
from django.urls import path

from . import views

urlpatterns = [
    path('index/',views.index,name='index1'),
    path('hello/<int:foo>',views.hello,{'foo':123}), #默认参数
    # path('2019/',views.numbers),
    # path('<int:yyy>/',views.numbers),
    path('page<int:yyy>',views.numbers),
    path('<int:x>/<int:y>',views.sum1),
    path('i/',views.i),
]