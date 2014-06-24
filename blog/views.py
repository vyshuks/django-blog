from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from blog.models import Post, Tag
from django.views import generic
from django.views.generic import View
from django import forms

class CreatePost( CreateView ):
	model = Post

class CreateTag( CreateView ):
	model = Tag

class TagList( generic.ListView ):
	model =  Tag 

class PostList( generic.ListView ):
	model = Post

class PostView( generic.DetailView ):
	model = Post

class PostEdit( UpdateView ):
	model = Post

class PostDelete( DeleteView ):
	model = Post

class ContactForm(forms.Form):
	name = forms.CharField()
	message = forms.CharField(widget = forms.Textarea)

class ContactView( FormView ):
	template_name = 'blog/form_contact.html'
	form_class = ContactForm

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if  form.is_valid():
			pass
		return render(request, self.template_name, {'form': form})


