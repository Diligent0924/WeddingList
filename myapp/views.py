from django.shortcuts import render, redirect
from myapp.models import Person

def index(request):
    searchname = request.GET.get("my_param", "")
    if searchname == "":
        w = Person.objects.filter(is_wedding = 0).order_by("-price")
        m = Person.objects.filter(is_wedding = 1).order_by("-price")
    else:
        w = Person.objects.filter(is_wedding = 0).filter(name__contains = searchname).order_by("-price")
        m = Person.objects.filter(is_wedding = 0).filter(name__contains = searchname).order_by("-price")
    
    sum_price = 0
    women = [("없음", 0)]
    w_total = 0
    men = [("없음", 0)]
    m_total = 0
    for i in w:
        women.append((i.name, i.price))
        w_total += i.price

    for i in m:
        men.append((i.name, i.price))
        m_total += i.price
    women.sort(key=lambda x: x[0])
    men.sort(key=lambda x:x[0])
    print(women[0], men[0])
    context = {'my_data_w' : w, 'my_data_m' : m,'sum_data' : w_total + m_total, 'women_MVP' : women[0][0], 'women_price' : women[0][1], 'men_MVP' : men[0][0], 'men_price': men[0][1], 'w_count' : len(women), 'm_count' : len(men)}
    return render(request, 'index.html', context)

def plus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        is_wedding = request.POST.get('women')
        print(111111)
        if is_wedding == "option1": 
            is_wedding = 1
        else:
            is_wedding = 0
        person = Person(name=name, price=price, is_wedding=is_wedding)
        person.save()
        return redirect("myapp:index")

