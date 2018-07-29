from django.shortcuts import render

def index(request):
	return render(request, 'personal/home.html')
def contact(request):
	return render(request, 'personal/contact.html', {'content':["If you want to contact me,dm me on my email:","shritakumarmund.98@gmail.com"]})