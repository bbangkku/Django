from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'calculators_app/index.html')

def detail(request, number1, number2):
    # URL 파라미터를 템플릿으로 전달
    result1 = number1 + number2
    result2 = number1 * number2
    result3 = number1 - number2
    result4 = (number1 / number2) if number2 != 0 else "계산할 수 없습니다"

    context = {
        'number1' : number1,
        'number2' : number2,
        'result1' : result1,
        'result2' : result2,
        'result3' : result3,
        'result4' : result4,
    }
    return render(request, 'calculators_app/index.html', context)
    
