from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404,get_list_or_404

from .serializers import BookListSerializer, BookSerializer,CommentSerializer
from .models import Book,Comment

@api_view(['GET', 'POST','PUT','DELETE'])
def book_list(request):
    books = Book.objects.all()
    if request.method == 'GET':
        serializer = BookListSerializer(books,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        
        
  
  
@api_view(['DELETE','PUT','GET'])
def book_delete(request,book_id):
    book = Book.objects.get(pk=book_id)
    if request.method =='DELETE':
        book.delete()
        return Response(book,status=status.HTTP_204_NO_CONTENT)        
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        
    elif request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
        
   
@api_view(['POST','PUT','GET','DELETE'])       
def comment(request,book_id):
    book = get_object_or_404(Book,pk=book_id)
    if request.method == 'GET':
        comments = book.comments.all()
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data) # content만 있음,,
        if serializer.is_valid(raise_exception=True): # content 유효성 검사
            serializer.save(book=book) # content에대한 유효성검사는 끝,, 외래키에 대한 유효성 검사를 안했따, > 리드온리니까, > 
            return Response(serializer.data,status=status.HTTP_201_CREATED)

# 해당 게시글에 있는 댓글 id로 조회하기 ?

@api_view(['POST','PUT','GET','DELETE'])      
def comment_modify(request,comment_id):
    comment = get_object_or_404(Comment,pk=comment_id)
    if request.method == 'GET':
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2')
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # book = Book.objects.all()
    # if request.method == 'GET':
    #     serializer = BookListSerializer(book,many=True)
    #     return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = BookSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    

            
