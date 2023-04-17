from django.shortcuts import render

# Create your views here.

def calculation(request):
    return render(request,'myapp2/calculation.html')

def result(request):
    num1 = int(request.GET.get('num1'))
    num2 = int(request.GET.get('num2'))
    result1 = num1 + num2
    result2 = num1 * num2
    result3 = num1 - num2
    result4 = (num1 / num2) if num2 != 0 else "계산할 수 없습니다"
    
    context = {
        'num1' : num1,
        'num2' : num2,
        'result1' : result1,
        'result2' : result2,
        'result3' : result3,
        'result4' : result4,
    }
    return render(request,'myapp2/result.html',context)
    