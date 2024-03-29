from django.urls import path
from .views import home, TodoDetail,TodoListCreate, TodoRetrieveUpdateDelete, TodoConcListCreate, TodoConcListUpdateDestroy
                    


urlpatterns = [
    path('', home),
    # path('todoList/', todoList),
    # path('todoListCreate/', todoListCreate),
    # path('toDo_list/', toDo_list),
    # path('todoListUpdate/<int:pk>/', todoListUpdate),
    # path('todoListDelete/<int:pk>/', todoListDelete),
    # path('toDo_detail/<int:pk>/', toDo_detail),
    # path('todo-list/', TodoList.as_view()),
    path('todo-list/', TodoListCreate.as_view()),
    path('todo-detail/<int:pk>', TodoDetail.as_view()),
    path('todoupdate/<int:pk>', TodoRetrieveUpdateDelete.as_view()),
    path('TodoConcListCreate/', TodoConcListCreate.as_view()),
    path('TodoConcListUpdateDestroy/<int:pk>', TodoConcListUpdateDestroy.as_view()),


]