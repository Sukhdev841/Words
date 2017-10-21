# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Word
from .models import Quote

from .forms import WordForm
from .forms import SearchForm
from .forms import QuoteForm

from django.http import Http404  
import random

# Create your views here.

def main_page(request):
	print ("in main view")
	all_words = Word.objects.all()
	list_of_words = []
	indexes = []

	if len(all_words) is 0:
		return render(request,'words/show_words.html',{"home":True,"list":list_of_words,'words':True})

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
	return render(request,'words/show_words.html',{"home":True,"list":list_of_words,'page_header':'Random 10 Words'})

# views redirecting to pages
def new_word_page(request):
	return render(request,'words/new_word.html',{"new_word":True})

def new_quote_page(request):
	return render(request,'words/new_word.html',{"new_quote":True})

def new_reading_page(request):
	return render(request,'words/new_word.html',{'new_reading':True})

def all_words_page(request,message=None):
	all_words = Word.objects.all()
	if message is None:
		return render(request,'words/show_words.html',{'list':all_words,'words':True,'page_header':'All Words'})
	else:
		return render(request,'words/show_words.html',{'list':all_words,'show_message':True,'message':message,'words':True,'page_header':'All Words'})

def all_quotes_page(request,message=None):
	all_quotes = Quote.objects.all()
	if message is None:
		return render(request,'words/show_words.html',{"list":all_quotes,'quotes':True})
	else:
		return render(request,'words/show_words.html',{"list":all_quotes,'show_message':True,'message':message,'quotes':True,'page_header':'All Quotes'})


def update_word_page(request,word):
	print (word + "is parameter to delete_word view")
	try:
		word_obj = Word.objects.get(word=word)
		return render(request,'words/new_word.html',{"word":word_obj.word,"meaning":word_obj.meaning,
													"sentence":word_obj.sentence,"punjabi":word_obj.punjabi,
													"hindi":word_obj.hindi,"tags":word_obj.tags,'edit_word':True})
	except:
		return render(request,'words/new_word.html',{'show_message':True,"message":'word not found',"edit_word":True})

def update_quote_page(request,quote):
	print (quote + " is found ")
	try:
		quote_obj = Quote.objects.get(quote=quote)
		return render(request,'words/new_word.html',{'quote':quote_obj.quote,'author':quote_obj.author,'language':quote_obj.language,
						'tags':quote_obj.tags,'edit_quote':True})
	except:
		return render(request,'words/new_word.html',{'show_message':True,"message":'quote not found',"edit_quote":True})



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
				return render(request,'words/new_word.html',{'show_message':True,'message':'Already Exists','new_word':True})
			except:
				print (word + " word desn't exitsts")
				word = request.POST.get('word')
				word = word.lower()
				meaning = request.POST.get('meaning','')
				sentence = request.POST.get('sentence','')
				hindi = request.POST.get('hindi','')
				punjabi = request.POST.get('punjabi','')
				tags = request.POST.get('tags','')

				word_obj = Word(word = word,meaning = meaning, sentence = sentence,hindi=hindi,punjabi=punjabi,tags =tags)
				word_obj.save()
				print(word+" is successfully saved in database.")
				return render(request,'words/new_word.html',{'show_message':True,'message':'Sucessfully Saved.','new_word':True})

		else:
			print("form is invalid")
			return render(request,'words/new_word.html',{'show_message':True,'message':'Saving Failed','new_word':True})

def save_quote(request):

	if request.method == 'POST':

		form = QuoteForm(request.POST)
		if len(form["quote"].value()) is not 0:
			quote = request.POST.get('quote')
			
			try:
				quote = quote.lower();
				quote_obj = Quote.objects.get(quote = quote)
				return render(request,'words/new_word.html',{'show_message':True,'message':'Already Exists','new_quote':True})
			except:
				quote = request.POST.get('quote')
				quote = quote.lower()
				author = request.POST.get('author','')
				tags = request.POST.get('tags','')
				language = request.POST.get('language','')

				quote_obj = Quote(quote = quote,author=author,tags =tags)
				quote_obj.save()
				return render(request,'words/new_word.html',{'show_message':True,'message':'Sucessfully Saved.','new_quote':True})

		else:
			print("form is invalid")
			return render(request,'words/new_word.html',{'show_message':True,'message':'Saving Failed','new_quote':True})



# deletion views

def delete_word(request,word):
	print (word + "is parameter to delete_word view")
	Word.objects.filter(word=word).delete()
	all_words = get_all_words()
	return render(request,'words/show_words.html',{'list':all_words,'show_message':True,'message':word+' successfully Deleted', 'words':True, 'page_header':'All Words'})
	

def delete_quote(request,quote):
	Quote.objects.filter(quote=quote).delete()
	all_quotes = get_all_quotes()
	return render(request,'words/show_words.html',{'list':all_quotes,'show_message':True,'message':quote+' successfully Deleted', 'quotes':True, 'page_header':'All Quotes'})

# updation views

def update_word(request,word):
	
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
													"sentence":word_obj.sentence,"tags":word_obj.tags,'show_message':True,'message':'Sucessfully Updated','edit_word':True})

		else:
			print("form is invalid")
			return render(request,'words/new_word.html',{'show_message':True,'message':'Updation Failed','edit_word':True})

def update_quote(request,quote):
	if request.method == 'POST':

		form = QuoteForm(request.POST)
		if len(form["quote"].value()) is not 0:
			delete_quote(request,quote);
			quote = request.POST.get('quote')
			author = request.POST.get('author','')
			tags = request.POST.get('tags','')
			language = request.POST.get('language','')
			quote_obj = Quote(quote= quote,author=author,tags=tags,language=language)
			quote_obj.save()
			
			return render(request,'words/new_word.html',{'quote':quote_obj.quote,'author':quote_obj.author,
									'language':quote_obj.language,'tags':quote_obj.tags,'show_message':True,'message':'Sucessfully Updated','edit_quote':True})

		else:
			print("form is invalid")
			return render(request,'words/new_word.html',{'show_message':True,'message':'Updation Failed','edit_quote':True})



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
			return render(request,'words/show_words.html',{"list":x,'words':True,'page_header':'Search Results'})

		else:
			print("search form is invalid")
			return all_words_page(request)
	return all_words_page(request,"not found",{'page_header':'Search Results'})

def get_all_words():
	return Word.objects.all()

def get_all_quotes():
	return Quote.objects.all()

