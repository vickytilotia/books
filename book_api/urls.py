from django.urls import path,include
# from .views import book_list,book_create,book
from .views import BookList,BookCreate,BookEdit

urlpatterns = [
    # path("", book_create),
    # path("list/", book_list),
    # path("<int:pk>", book),
    path("", BookCreate.as_view()),
    path("list/", BookList.as_view()),
    path("<int:pk>", BookEdit.as_view()),
    
]