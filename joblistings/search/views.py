from django.shortcuts import render, redirect
from search.models import JobPost

# Create your views here.
def home_page(request):

	if 'skillset' in request.GET.keys():

		skillset = request.GET.getlist('skillset')

		#jobs = JobPost.objects(skills__in=skillset)[0:15]

		return render(request, 'home.html', {
			'skillset': skillset,
		})

	return render(request, 'home.html')

# get rid of results page, make a single page app
def results_page(request):
	return render(request, 'results.html', {
		'skillset': dict(request.POST)['skillset']
	})