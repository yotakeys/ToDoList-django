from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('taskdetail/<int:pk>/', TaskDetail.as_view(), name='taskdetail'),
    path('taskcreate/', TaskCreate.as_view(), name='taskcreate'),
    path('taskUpdate/<int:pk>/', TaskUpdate.as_view(), name='taskupdate'),
]
