from django.shortcuts import render
from django.conf import settings
import requests
from django.http import JsonResponse
from rest_framework.response import Response
import pprint
from rest_framework.decorators import api_view
from django.db.models import Max
# Create your views here.

from rest_framework import status
from .models import DepositProducts, DepositOptions
from .serializers import DepositOptionsSerializer, DepositProductsSerializer

API_KEY = settings.API_KEY
BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'
response = requests.get(BASE_URL)
# print(response)

def api_test(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth' : API_KEY,
        'topFinGrpNo' : '020000',
        'pageNo' : 1,
    }
    response = requests.get(URL, params=params).json()
    return JsonResponse({'response':response})

@api_view(['GET'])
def save_deposit_products(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth' : API_KEY,
        'topFinGrpNo' : '020000',
        'pageNo' : 1
    }
    response = requests.get(URL, params=params).json()

    # for item in response['result']['baseList']:
    #     serializer = DepositProductsSerializer(data=item)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()

    for item in response['result']['optionList']:
        if item.get('fin_prdt_cd') is None:
            print(item)
        else:
            for key, value in item.items():
                if value is None:
                    item['intr_rate'] = -1
            serializer = DepositOptionsSerializer(data=item)
            product = DepositProducts.objects.get(fin_prdt_cd=item['fin_prdt_cd'])
            if serializer.is_valid(raise_exception=True):
                serializer.save(fin_prdt_cd=product)

    queryset = DepositProducts.objects.all()
    serializer = DepositProductsSerializer(queryset, many=True)
    return Response(serializer.data)
    
    
    
@api_view(['GET','POST'])
def deposit_products(request):
    if request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        deposits = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(deposits, many=True)
        return Response(serializer.data)
    
    
    # return Response(deposits)
@api_view(['GET'])
def deposit_product_options(request,fin_prdt_cd):   
    product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    print(product)
    options = product.options.all()
    serializers=DepositOptionsSerializer(options,many=True)
    return Response(serializers.data)



def top_rate(request):
    top_option = DepositOptions.objects.aggregate(top_rate=Max('intr_rate2'))
    option = DepositOptions.objects.get(intr_rate2=top_option['top_rate'])
    option2 = DepositOptionsSerializer(option)
    print(option)
    product = DepositProducts.objects.get(id = option2.data['fin_prdt_cd'])
    print(product)
    serializer_p = DepositOptionsSerializer(product)
    print(serializer_p)

    options = product.options.all()
    print(options)
    serializer_o = DepositOptionsSerializer(options,many=True)
    return Response({
        'deposit_product' : serializer_p.data,
        'options' : serializer_o.data,
    })
    
