from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'), #get and post req. for insert operation
    path('list/', views.employee_list, name='employee_list'), #get and post req. for update operation
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'), #delete operation
    path('<int:id>/', views.employee_form, name='employee_update'), #get req. to retrive and display all records
]
