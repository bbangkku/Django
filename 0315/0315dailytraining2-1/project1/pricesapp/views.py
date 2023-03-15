from django.shortcuts import render

# Create your views here.
def index(request,name1,num):
    price_list = {"라면":980, "홈런볼":1500, "칙촉":2300, "식빵":1800}
    if name1 in price_list:
        context = {
        'name1' : name1,
        'num' : num,
        'price' : price_list[name1],
        'result' : num* price_list[name1],
        }
    else:
        context = {
        'name1' : name1,
        'num' : num,
        'price' : -1
        }

    return render(request,'pricesapp/index.html',context)