from django.urls import path

from basket.views import basket_add, basket_remove, basket_edit

app_name = 'basket'

urlpatterns = [
    path('add/<int:product_id>/', basket_add, name='basket_add'),
    path('remove/<int:id>/', basket_remove, name='basket_remove'),
    path('edit/<int:id>/<int:quantity>/', basket_edit, name='basket_edit'),
]