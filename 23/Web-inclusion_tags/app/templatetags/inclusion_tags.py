from django import template
from app.models import Autor

register = template.Library()
@register.inclusion_tag('app/inclusion.html')

def show_autores():
	p = Autor.objects.all()
	return {'autores': p}
