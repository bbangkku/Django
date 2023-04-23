from rest_framework import serializers
from .models import Book,Comment

# Q 1.
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('book',)
        
class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','title','content')



class BookSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True,read_only=True)
    class Meta:
        model = Book
        fields = '__all__'

