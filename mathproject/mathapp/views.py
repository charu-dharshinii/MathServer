from django.shortcuts import render
def surf_area(request):
    context={}
    context['surf_area'] = "0"
    context['r'] = "0"
    context['h'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        r = request.POST.get('radius','0')
        h = request.POST.get('height','0')
        print('request=',request)
        print('Radius=',r)
        print('Height=',h)
        surf_area = (2*3.14*int(r)*int(h)) + (2*3.14*int(r)*int(r))
        context['surf_area'] = surf_area
        context['r'] = r
        context['h'] = h
        print('Surface Area=',surf_area)
    return render(request,'mathapp/math.html',context)