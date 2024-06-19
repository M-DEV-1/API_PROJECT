from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name=""),
    path('register/', views.register, name="register"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # view stocks together
    path('stocks/', views.stock_list, name='stock-list'),
    # view stock individually
    path('stocks/<int:stock_id>/', views.stock_detail, name='stock-detail'),
    # create new stock
    path('stocks/create/', views.stock_create, name='stock-create'),
    # update certain stock
    path('stocks/<int:stock_id>/update/', views.stock_update, name='stock-update'),
    # delete certain stock
    path('stocks/<int:stock_id>/delete/', views.stock_delete, name='stock-delete'),
]