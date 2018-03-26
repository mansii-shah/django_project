from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
#def post_list(request):
	#return render(request,'blog/post_list.html',{})
class PostPageView(TemplateView):
	"""docstring for
	 PostPageView"""
	def get(self, request,**kwargs):
		return render(request,'post_list.html',context=None)

class AboutPageView(TemplateView):
	def get(self, request,**kwargs):
		return render(request,'about.html',context=None)

		
		
			
