from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(
        required=True,
        label="book title",
        help_text="give your book a unique name"
    )
    owner = serializers.CharField()
    description = serializers.CharField()
    rating = serializers.IntegerField()

    def create(self, validated_information):
        # validated information is data from postman after we called is_valid method
        record = Book.objects.create(**validated_information)
        return record


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title", "owner"]