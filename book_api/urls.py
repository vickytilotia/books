from django.urls import path,include
# from .views import book_list,book_create,book
from .views import BookList,BookCreate,BookEdit

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # path("", book_create),
    # path("list/", book_list),
    # path("<int:pk>", book),
    path("", BookCreate.as_view()),
    path("list/", BookList.as_view()),
    path("<int:pk>", BookEdit.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]