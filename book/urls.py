from django.urls import path
from .api_views import BookListView, BookDetail
from .views import book_home, book_list, book_detail, create_book_record


app_name = 'book' 

urlpatterns = [
    path("", book_home, name="home_url_for_book"),
    path("all_books", book_list, name="list_of_books"),
    path("create_book", create_book_record, name="create_book_record"),
    path("book/<int:book_id>", book_detail, name="single_book_information"),
    path("api/all_books", BookListView.as_view(), name="lost_of_all_books"),
    path("api/book/<int:id>", BookDetail.as_view(), name="detail_of_a_book"),

]