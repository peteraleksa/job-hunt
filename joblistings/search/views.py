from django.shortcuts import render, redirect

# Create your views here.
def home_page(request):
	return render(request, 'home.html', , {
		'skillset': request.POST.get('skillset', ''),
	})

# get rid of results page, make a single page app
def results_page(request):
	return render(request, 'results.html', {
		'skillset': request.POST.get('skillset', ''),
	})