from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, Login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Login.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('', TaskList.as_view(), name='tasks'),
    path('taskdetail/<int:pk>/', TaskDetail.as_view(), name='taskdetail'),
    path('taskcreate/', TaskCreate.as_view(), name='taskcreate'),
    path('taskupdate/<int:pk>/', TaskUpdate.as_view(), name='taskupdate'),
    path('taskdelete/<int:pk>/', TaskDelete.as_view(), name='taskdelete'),
]
