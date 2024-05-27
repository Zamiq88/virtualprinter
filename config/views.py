from django.shortcuts import render

def printer(request):
    data1=''
    count=''
    data2=''
    
    if request.method=='POST':
        data1=request.POST.get('input1')
        data2=request.POST.get('input2')
        data2=int(data2)
        count=list(range(1,(data2+1)))
        
    context={'data1':data1,'count':count}
    
    return render(request,'printer.html',context)