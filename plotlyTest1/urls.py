from django.urls import path

from . import views

urlpatterns = [
    path('', views.chart, name='chart'),
    #path('media', views.Command.handle),
#    path('book/<int:book_id>', views.book_by_id, name='book_by_id'),
]