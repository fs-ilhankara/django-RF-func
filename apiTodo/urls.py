from django.urls import path
from .views import home, todoList, todoListCreate, toDo_list, todoListUpdate, todoListDelete, toDo_Detail, TodoListe, TodoDetail

urlpatterns = [
    
    path('', home),
    path('todoList/', todoList),
    path('todoListCreate/', todoListCreate),
    path('toDo_list/', toDo_list),
    path('todoListUpdate/<int:pk>', todoListUpdate),
    path('todoListDelete/<int:pk>', todoListDelete),
    path('toDo_Detail/<int:pk>', toDo_Detail),
    path('TodoListe/', TodoListe.as_view()),
    path('TodoDetail/<int:pk>', TodoDetail.as_view()),
   
]