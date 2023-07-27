from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .custom_authorization import CustomPermission


class BookListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, CustomPermission]

    def get(self, request, *args, **kwargs):
        all_books = Book.objects.all() # all the books
        serializer = BookSerializer(all_books, many=True) #serialize all the books
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #create a book record
    
    def post(self, request, *args, **kwargs):
        data_from_postman = request.data
        serializer_information = BookSerializer(data=data_from_postman)
        if serializer_information.is_valid():
            # if all the data is correct, create a record in the database
            serializer_information.save()
            return Response(serializer_information.data, status=status.HTTP_201_CREATED)
        
        # if the data is incorrect reply to the user that something is wrong
        return Response(serializer_information.errors, status=status.HTTP_400_BAD_REQUEST)


# get a single book record.
class BookDetail(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            single_book_record = Book.objects.get(id=id) #
            serializer_information = BookSerializer(single_book_record)
            return Response(serializer_information.data)
        except:
            return Response({"message": "book does not exist"}, status=status.HTTP_400_BAD_REQUEST)