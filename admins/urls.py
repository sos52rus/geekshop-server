from django.urls import path


from admins.views import IndexTemplateView, AdminUserListView, AdminUserCreateView, AdminUserDeleteView, AdminUserUpdateView,  \
    AdminUserActivateView, admin_user_delete_is_staff, admin_user_is_staff, AdminProductListView, AdminProductCreateView, \
    AdminProductUpdateView, AdminProductDeleteView


app_name = 'admins'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('users/', AdminUserListView.as_view(), name='admin_user'),
    path('users/create/', AdminUserCreateView.as_view(), name='admin_user_create'),
    path('users/update/<int:pk>/', AdminUserUpdateView.as_view(), name='admin_user_update'),
    path('users/delete/<int:pk>/', AdminUserDeleteView.as_view(), name='admin_user_delete'),
    path('users/activate/<int:pk>/', AdminUserActivateView.as_view(), name='admin_user_activate'),
    path('users/is_staff/<int:id>/', admin_user_is_staff, name='admin_user_is_staff'),
    path('users/delete_is_staff/<int:id>/', admin_user_delete_is_staff, name='admin_user_delete_is_staff'),
    path('products/', AdminProductListView.as_view(), name='admin_product'),
    path('products/create/', AdminProductCreateView.as_view(), name='admin_product_create'),
    path('products/update/<int:pk>/', AdminProductUpdateView.as_view(), name='admin_product_update'),
    path('products/delete/<int:pk>/', AdminProductDeleteView.as_view(), name='admin_product_delete'),
]
