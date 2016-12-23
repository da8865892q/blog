from django.conf.urls import url
from book import views

urlpatterns = [
    url(r'^$', views.book, name='book'),
    url(r'^bookCreate/$', views.bookCreate, name='bookCreate'),

]