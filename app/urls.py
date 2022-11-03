from django.urls import path
from .views import TaskList, TaskCreate, TaskUpdate, TaskDelete, Login, Register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Login.as_view(), name="login"),
    path('register/', Register.as_view(), name="register"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('', TaskList.as_view(), name='tasks'),
    path('taskcreate/', TaskCreate.as_view(), name='taskcreate'),
    path('taskupdate/<int:pk>/', TaskUpdate.as_view(), name='taskupdate'),
    path('taskdelete/<int:pk>/', TaskDelete.as_view(), name='taskdelete'),
]
