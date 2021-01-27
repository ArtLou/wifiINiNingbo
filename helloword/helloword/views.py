from django.http import HttpResponse
 
def hello(request):
    return HttpResponse("Hello world ! ")

def arthurlou(request):
	context = {}
	context['ArthurLou']='ArthurLouNoteMe'
	return render(request,'arthurlou.html',context)
