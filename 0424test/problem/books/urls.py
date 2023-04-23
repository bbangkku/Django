from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/',views.book_delete),
    path('books/<int:book_id>/comment/',views.comment),    
    path('comment/<int:comment_id>/',views.comment_modify),    
        
]
