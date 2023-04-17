from django.urls import path
from articles import views

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    # path('articles/<int:articels_pk>/comments/',views.comment_create),
    path('articles/<int:articels_pk>/comments/',views.comment_list), # 클라이언트입장에서 
# 게시판의 댓글을 조회 > article_detail에서 정의
# 댓글 생성
# 특정 댓글 삭제, 수정

    # path('comments/',views.comment_list), # 클라이언ㄴ트가 이거 필요없다고함
    path('comments/<int:comment_pk>/',views.comment_detail),
]
