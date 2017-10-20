# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Word
from .forms import WordForm
from .forms import SearchForm
from .forms import ParagraphForm
from django.http import Http404  
from suk import extract_words

import random
# Create your views here.

def main_page(request):
	print ("in main view")
	all_words = Word.objects.all()
	list_of_words = []
	indexes = []

	if len(all_words) is 0:
		return render(request,'words/show_words.html',{"home":True,"list":list_of_words})

	for i in range(len(all_words)):
		indexes.append(i)

	for i in range(100):
		# suffle the words
		i1 = random.randint(1,len(all_words)) - 1
		i2 = random.randint(1,len(all_words)) - 1
		temp = indexes[i1]
		indexes[i1] = indexes[i2]
		indexes[i2] = temp

	if len(all_words) < 10:
		y = len(all_words)
	else:
		y = 10;
	for x in range(y):
		list_of_words.append(all_words[indexes[x]])

	# select random 10 words from database
	return render(request,'words/show_words.html',{"home":True,"list":list_of_words})

# views redirecting to pages
def new_word_page(request):
	return render(request,'words/new_word.html')

def all_words_page(request,message=None):
	all_words = Word.objects.all()
	for x in all_words:
		print (x.word + " "+ x.meaning)
	if message is None:
		return render(request,'words/show_words.html',{"list":all_words})
	else:
		return render(request,'words/show_words.html',{"list":all_words,'show_message':True,'message':message})

def update_word_page(request,word):
	print (word + "is parameter to delete_word view")
	try:
		word_obj = Word.objects.get(word=word)
		return render(request,'words/new_word.html',{"word":word_obj.word,"meaning":word_obj.meaning,
													"sentence":word_obj.sentence,"punjabi":word_obj.punjabi,
													"hindi":word_obj.hindi,"tags":word_obj.tags,'edit':True})
	except:
		return render(request,'words/new_word.html',{'show_message':True,"message":'word not found'})

# insertion views

def save_word(request):
	print ("saving a word into database")

	if request.method == 'POST':

		form = WordForm(request.POST)
		if len(form["word"].value()) is not 0:
			word = request.POST.get('word')
			print ("going to save "+word)
			try:
				word = word.lower();
				word_obj = Word.objects.get(word=word)
				print (word + " word already exists")
				return render(request,'words/new_word.html',{'show_message':True,'message':'Already Exists'})
			except:
				print (word + " word desn't exitsts")
				word = request.POST.get('word')
				word = word.lower()
				meaning = request.POST.get('meaning','')
				sentence = request.POST.get('sentence','')
				hindi = request.POST.get('hindi','')
				punjabi = request.POST.get('punjabi','')
				tags = request.POST.get('tags','')

				if meaning == "":
					meaning = "not defined"

				if sentence == "":
					sentence = "not defined"

				word_obj = Word(word = word,meaning = meaning, sentence = sentence,hindi=hindi,punjabi=punjabi,tags =tags)
				word_obj.save()
				print(word+" is successfully saved in database.")
				return render(request,'words/new_word.html',{'show_message':True,'message':'Sucessfully Saved.'})

		else:
			print("form is invalid")
			return render(request,'words/new_word.html',{'show_message':True,'message':'Saving Failed'})

# deletion views

def delete_word(request,word):
	print (word + "is parameter to delete_word view")
	Word.objects.filter(word=word).delete()
	return all_words_page(request,word+' is successfully deleted.')

# updation views

def update_word(request,word):
	print ("updating a word in database")
	
	if request.method == 'POST':

		form = WordForm(request.POST)
		if len(form["word"].value()) is not 0:
			delete_word(request,word);
			word = request.POST.get('word')
			meaning = request.POST.get('meaning','')
			sentence = request.POST.get('sentence','')
			hindi = request.POST.get('hindi','')
			punjabi = request.POST.get('punjabi','')
			tags = request.POST.get('tags','')
			word_obj = Word(word = word,meaning = meaning, sentence = sentence,hindi=hindi,punjabi=punjabi,tags=tags)
			word_obj.save()
			print(word+" is successfully updated in database.")
			return render(request,'words/new_word.html',{"word":word_obj.word,"meaning":word_obj.meaning,"hindi":word_obj.hindi,"punjabi":word_obj.punjabi,
													"sentence":word_obj.sentence,"tags":word_obj.tags,"edit":'true','show_message':True,'message':'Sucessfully Updated'})

		else:
			print("form is invalid")
			return render(request,'words/new_word.html',{'show_message':True,'message':'Updation Failed'})


# other views


# for searching
def search(request):
	if request.method == 'POST':

		form = SearchForm(request.POST)
		if len(form["search_field"].value()) is not 0:
			word = request.POST.get('search_field')

			if word == "":
				return render(request,'words/home.html')
			x = []
			word = word.lower()
			try:
				word_obj = Word.objects.get(word=word)
			except:
				try:
					word_obj = Word.objects.get(hindi=word)
				except:
					try:
						word_obj = Word.objects.get(punjabi=word)
					except:
						return all_words_page(request,"not found") 
			x.append(word_obj)
			print(word_obj.word+" is successfully found in database.")
			return render(request,'words/show_words.html',{"list":x})

		else:
			print("search form is invalid")
			return all_words_page(request)
	return all_words_page(request,"not found")

