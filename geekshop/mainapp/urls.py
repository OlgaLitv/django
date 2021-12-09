from django.urls import path
from mainapp.views import products, details


app_name = 'mainapp'

urlpatterns = [
    path('', products, name='products'),
    path('details/<int:product_id>', details, name='details'),
    path('category/<int:id_category>/<int:page>', products, name='category'),

]
