from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView, TemplateView
from .models import Perfil, Publication, Comment
from django.urls import reverse_lazy
from .forms import User_form
from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
class Perfil_View(TemplateView):
	template_name = 'home/perfil_detail.html'

	def get_context_data(self, **kwargs):
		context = super(Perfil_View, self).get_context_data(**kwargs)
		user = User.objects.get(username=self.request.user.username)
		context['object_list'] = Perfil.objects.filter(user_perfil=user)
		return context

class SignUp(CreateView):
	template_name = 'home/signup.html'
	form_class = User_form
	success_url = reverse_lazy('login')

	def form_valid(self, form):
		user = form.save()
		p = Perfil()
		p.user_perfil = user
		p.email = form.cleaned_data['email']
		p.image = form.cleaned_data['image']
		#p.is_staff=True
		p.save()
		return super(SignUp, self).form_valid(form)

class Perfil_Detail(DetailView):
	model = Perfil
	template_name = 'home/perfil_detail.html'

class Perfil_Update(UpdateView):
	model = Perfil
	fields = ['email','image']
	template_name = 'home/perfil_update.html'
	success_url = reverse_lazy('perfil_view')

class Friend_List(ListView):
	model = Perfil
	template_name = 'home/list_friends.html'

	def get_context_data(self, **kwargs):
		context = super(Friend_List, self).get_context_data(**kwargs)
		user = User.objects.get(username=self.request.user.username)
		context['object_list'] = Perfil.objects.filter(user_perfil=user)
		return context

class Community_List(ListView):
	model = Perfil
	template_name = 'home/list_community.html'

	def get_context_data(self, **kwargs):
		context = super(Community_List, self).get_context_data(**kwargs)
		user = User.objects.get(username=self.request.user.username)
		number = Perfil.objects.all().exclude(user_perfil=user).count()
		user_id = Perfil.objects.get(user_perfil=user)
		object_list = Perfil.objects.all().exclude(user_perfil=user)
		friend_list = Perfil.objects.filter(user_perfil=user)
		friendsExc = []
		communityExc = []
		nofriends = []

		for fr in friend_list:
			for f in fr.friends.all():
				friendsExc.append(f.user_perfil)

		for co in object_list:
			communityExc.append(co.user_perfil)

		for i in communityExc:
			if i in friendsExc:
				print ('%s in both sets!' %(i))
			else:
				print ('%s does not match!' %(i))
				nofriends.append(i)

		print (nofriends)
		return {'nofriends':nofriends,'number':number,'object_list':object_list, 'user_id':user_id}
# def Add_Friend(self, person, status):

def Add_Friend(request, pk, friend):
	if pk:
		p = Perfil.objects.get(id=pk)
		p.save()
		f = Perfil.objects.get(id=friend)
		p.friends.add(f)
	return HttpResponseRedirect('/friend_list/')

def Delete_Friend(request, pk, friend):
	if pk:
		p = Perfil.objects.get(id=pk)
		p.save()
		f = Perfil.objects.get(id=friend)
		p.friends.remove(f)
	return HttpResponseRedirect('/friend_list/')

class Register_Publication(CreateView):
	template_name = 'home/register_publication.html'
	model = Publication
	fields = ['title', 'body', 'user']
	success_url = reverse_lazy('report_publication')

class Report_Publication(ListView):
	template_name = 'home/report_publication.html'
	model = Publication

def Score_Publication(request, pk):
	if pk:
		p = Publication.objects.get(id=pk)
		counter = p.score
		if counter == None:
			counter = 0
		counter += 1
		p.score = counter
		p.save()

	return HttpResponseRedirect('/detail_publication/%s'%pk)

def Unscored_Publication(request, pk):
	if pk:
		p = Publication.objects.get(id=pk)
		counter = p.unscored
		if counter == None:
			counter = 0
		counter += 1
		p.unscored = counter
		p.save()

	return HttpResponseRedirect('/detail_publication/%s'%pk)

def Score_Comment(request, publication, comment):
	if publication and comment:
		c = Comment.objects.get(id=comment)
		counter = c.score
		if counter == None:
			counter = 0
		counter += 1
		c.score = counter
		c.save()

	return HttpResponseRedirect('/detail_publication/%s'%publication)

class Register_Comment(CreateView):
	template_name = 'home/detail_publication.html'
	model = Comment
	fields = ['comment', 'user', 'publication']
	success_url = reverse_lazy('report_publication')

	def get_context_data(self, **kwargs):
		context = super(Register_Comment, self).get_context_data(**kwargs)
		context['object'] = Publication.objects.get(id=self.kwargs['pk'])
		context['comment_list'] = Comment.objects.filter(publication=self.kwargs['pk'])
		return context
