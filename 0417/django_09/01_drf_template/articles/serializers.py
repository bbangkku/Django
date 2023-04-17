from rest_framework import serializers
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields=('article')
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop('article', None)
        return rep

class ArticleListSerializer(serializers.ModelSerializer):
# 게시글의 댓글을 모두 조회 ? ? ?
# 1. CommentSerializer 를 포함 시키는 것 : Nested Serializer
#   - Article 모델이 알고 있는 필드만 사용 가능
#       즉, 참조 및 역참조 관계에 있는 데이터만 가져올 수 있다.

# 변수명 , field 추가 시 Article 모델이 알고있는 이름으로 사용할 것
    comment_set = CommentSerializer(many=True,read_only=True)
# 게시글에 포함된 댓글의 개수
    comment_count = serializers.IntegerField(source='comment_set.count',read_only=True)
    
# 스스로 찾아보기
# 2. 각 필드를 재정의
# 3. SerializerMethodField 활용


    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # read_only = True  > 입력받으면안된다는 뜻
    class Meta:
        model = Article
        # fields = ('id', 'title', 'content')
        fields ='__all__'
    # serializer 출력 시 호출되는 함수
    def to_representation(self, instance):
        # 원래있던 것들을 일단 모두 출력해야함
        rep = super().to_representation(instance)
        # comment_count 를 추가
        # repersen
        rep['comments'] = rep.pop('comment_set',[])
        return rep
    


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

