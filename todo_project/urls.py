"""todo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import todolist.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolist.views.home, name='home'),
    path('todo', todolist.views.todo, name='todo'),
    path('signup/', accounts.views.signup, name='signup'),
    path('login/', accounts.views.login, name='login'),
    path('logout/', accounts.views.logout, name='logout'),
    path('todo/new/', todolist.views.create, name='new'),
    path('todo/edit/<int:todo_id>', todolist.views.edit, name='edit'),
    path('todo/destroy/<int:todo_id>', todolist.views.destroy, name='destroy'),
]
