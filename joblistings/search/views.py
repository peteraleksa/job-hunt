from django.shortcuts import render, redirect

# Create your views here.
def home_page(request):

	if 'skillset' in request.GET.keys():

		return render(request, 'home.html', {
			'skillset': request.GET.getlist('skillset'),
		})

	return render(request, 'home.html')

# get rid of results page, make a single page app
def results_page(request):
	return render(request, 'results.html', {
		'skillset': dict(request.POST)['skillset']
	})