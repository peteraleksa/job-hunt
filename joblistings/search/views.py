from django.shortcuts import render, redirect
from search.models import JobPost

# Create your views here.
def home_page(request):

	if 'skillset' in request.GET.keys():

		skillset = request.GET.getlist('skillset')

		jobs = []
		job_ids = []
		db_skills = []

		for skill in skillset:
			db_skills.extend(Skill.objects.filter(skill__exact=skill.lower()))

		for dbs in db_skills:
			ids = JobSkills.objects.filter(skill_id__exact=dbs._id)
			for i in ids:
				if i.post_id not in job_ids:
					job_ids.extend(i)

		count = 0
		for jid in job_ids:
			if count < 10:
				jobs.extend(JobPosts.objects.filter(_id__exact=jid))
				count+=1
			else:
				break

		return render(request, 'home.html', {
			'skillset': skillset,
			'jobs': jobs,
		})

	return render(request, 'home.html')

# get rid of results page, make a single page app
def results_page(request):
	return render(request, 'results.html', {
		'skillset': dict(request.POST)['skillset']
	})