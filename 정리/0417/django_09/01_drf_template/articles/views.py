from django.shortcuts import get_list_or_404,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer,CommentSerializer
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from drf_yasg.utils import swagger_auto_schema
# PageNumberPagination : page_size 기반의 pagination
# LimitOffsetPagination : limit 와 offset 기반으로 pagination

# Create your views here.
# @api_view(['GET'])
# def article_list(request):
#     articles = Article.objects.all()
#     serializer = ArticleListSerializer(articles, many=True)
#     return Response(serializer.data)

# DRF에서 api_view 데코레이터는 필수로 작성해야함
# -> DRF view 함수가 응답해야하는 HTTP 메서드 목록을받음
# -> 기본적으로 GET 메서드만 허용되며 다른 메서드 요청에 대해서는 405 Method Not Allowed로 응답
# @swagger_auto_schema(method=['POST'],request_body=ArticleListSerializer)
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        # get _@@@ 하면 해당 객체목록이 없으면 http404를 raise함
        # 데이터가없는게아니라 니가 잘못친거다 라고 말하는거
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data = request.data)
        print('>>>>>>>>>>>>>>>>>>>>')
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article,pk=article_pk)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        # 삭제는 따로 반환할 데이터가 없기 때문에
        # 204 : 요청 완료 + 반환할 데이터 없음
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        # 기존의 article에 데이터 넣고(수정)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET','DELETE','PUT'])
def comment_detail(request,comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        # 기존의 article에 데이터 넣고(수정)
        serializer = ArticleSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
@api_view(['GET','POST'])
def comment_list(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    if request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
     
        return Response(serializer.data)
    elif request.method == "GET":
        comments = article.comment_set.all()
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)


## 추가 수업
# @api_view(['POST'])
# def comment_create(request, article_pk):
#     article = Article.objects.get(pk=article_pk)
#     serializer = CommentSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(article=article)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     articles = Article.objects.all()
#     paginator = PageNumberPagination()
#     paginator.page_size = 5
#     # pagination을 한 쿼리셋으로 변경
#     paginated_articles = paginator.paginate_queryset(articles, request)
#     # 해당 쿼리셋을 기준으로 serializer를 만듦
#     serializer = ArticleListSerializer(paginated_articles,many=True)
#     # paginator 를 이용하여, pagination이 완료된 결과 반환
#     # return Response(serializer.data)
#     return paginator.get_paginated_response(serializer.data+)