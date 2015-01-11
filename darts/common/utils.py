def get_next_page(request):
	next = None
	if request.GET:
		next = request.GET['next']
	elif request.POST:
		next = request.POST['next']
	if not next:
		next = 'home:help'
	return next
