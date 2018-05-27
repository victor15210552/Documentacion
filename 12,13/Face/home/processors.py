import django
import sys
from .models import Perfil

def user_image(request):
	try:
		img=None
		user = request.user
		up=Perfil.objects.get(user_perfil=user)
		img='http://localhost:8000/media/%s'%up.image
	except:
		img = 'http://127.0.0.1:8000/static/media/user.png'
	return img

def myprocessors(request):
	get_version_django = django.get_version()
	get_version_python = sys.version

	dic = { 'get_image_profile':user_image(request), 'django_version': get_version_django, 'python_version' : get_version_python}
	return dic