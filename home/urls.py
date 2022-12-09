from django.urls import path
from .views import home
from home import views


urlpatterns = [  
    path("", home, name="home"),
    path('app', views.app),  
    path('app/show',views.show),  
    path('app/edit/<int:id>', views.edit),  
    path('app/update/<int:id>', views.update),  
    path('app/delete/<int:id>', views.destroy),  
    path('plans', views.plans), 
    path('plan', views.plan), 
    path('subs', views.subs),
    path('subs/add', views.addSubs),  
    path('subs/edit/<int:id>', views.editSubs), 
    path('subs/update/<int:id>', views.updateSubs),  
]  