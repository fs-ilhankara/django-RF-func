from django.urls import path
from .views import home, todoList, todoListCreate, toDo_list

urlpatterns = [
    
    path('', home),
    path('todoList/', todoList),
    path('todoListCreate/', todoListCreate),
    path('toDo_list/', toDo_list),
   
]