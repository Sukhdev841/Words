# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from .models import Word
from .models import Quote
from .models import Reading

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

def all_readings_page(request,message=None):
	all_readings = Reading.objects.all()
	if message is None:
		return render(request,'words/show_words.html',{"list":all_readings,'reading':True,'page_header':'All Readings'})
	else:
		return render(request,'words/show_words.html',{"list":all_readings,'reading':True,'show_message':True,'message':message})

def update_word_page(request,word_id):
	word_x = Word.objects.get(id=word_id)
	print (word_x.word + "is parameter to delete_word view")
	try:
		word_obj = Word.objects.get(id=word_id)
		return render(request,'words/new_word.html',{"word":word_obj.word,"meaning":word_obj.meaning,
													"sentence":word_obj.sentence,"punjabi":word_obj.punjabi,
													"hindi":word_obj.hindi,"tags":word_obj.tags,'edit_word':True})
	except:
		return render(request,'words/new_word.html',{'show_message':True,"message":'word not found',"edit_word":True})

def update_quote_page(request,quote_id):
	print (Quote.objects.get(id=quote_id).quote + " is found ")
	try:
		quote_obj = Quote.objects.get(id=quote_id)
		return render(request,'words/new_word.html',{'id':quote_obj.id,'quote':quote_obj.quote,'author':quote_obj.author,'language':quote_obj.language,
						'tags':quote_obj.tags,'edit_quote':True})
	except:
		return render(request,'words/new_word.html',{'show_message':True,"message":'quote not found',"edit_quote":True})

def update_reading_page(request,id):
	#r_o = Reading.objects.get(id=id)
	#print(r_o+ " is passage id")
	print(" id of reading is "+id)
	try:
		print("in try block of update_reading_page ")
		reading_obj = Reading.objects.filter(id=id)
		print("object is found in update_reading_page "+reading_obj[0].author)
		
		return render(request,'words/new_word.html',{'id':reading_obj[0].id,'title':reading_obj[0].heading,'passage':reading_obj[0].passage,
						'author':reading_obj[0].author,'tags':reading_obj[0].tags,'language':reading_obj[0].language,'edit_reading':True})
	except Exception as e:
		print '%s (%s)' % (e.message, type(e))
		print ("in exception block of update_reading_page")
		return render(request,'words/new_word.html',{'show_message':True,'message':"Reading not found"})



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

def save_reading(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		passage = request.POST.get('passage')
		author = request.POST.get('author')
		tags = request.POST.get('tags')
		language = request.POST.get('language')
		reading_obj = Reading(heading=title,passage=passage,author=author,tags=tags,language=language)
		reading_obj.save()
		print(" new reading is saved successfully ")
		return main_page(request)
	else :
		return main_page(request)

# deletion views

def delete_word(request,word):
	print (word + "is parameter to delete_word view")
	Word.objects.filter(word=word).delete()
	all_words = get_all_words()
	return render(request,'words/show_words.html',{'list':all_words,'show_message':True,'message':word+' successfully Deleted', 'words':True, 'page_header':'All Words'})
	
def delete_quote(request,id):
	Quote.objects.filter(id=id).delete()
	all_quotes = get_all_quotes()
	return render(request,'words/show_words.html',{'list':all_quotes,'show_message':True,'message':id+' quote successfully Deleted', 'quotes':True, 'page_header':'All Quotes'})

def delete_reading(request,id):
	Reading.objects.filter(id=id).delete()
	all_readings = Reading.objects.all()
	return render(request,'words/show_words.html',{'list':all_readings,'show_message':True,'message':id+' reading succefully deleted','readings':True,'page_header':'All Readings'})

# updation views

def update_word(request,word):
	
	if request.method == 'POST':

		form = WordForm(request.POST)
		if len(form["word"].value()) is not 0:
			#delete_word(request,word);
			word = request.POST.get('word')
			meaning = request.POST.get('meaning','')
			sentence = request.POST.get('sentence','')
			hindi = request.POST.get('hindi','')
			punjabi = request.POST.get('punjabi','')
			tags = request.POST.get('tags','')
			Word.objects.filter(word=word).update(meaning = meaning, sentence = sentence,hindi=hindi,punjabi=punjabi,tags=tags)
			word_obj = Word.objects.get(word = word)
			#word_obj.save()
			print(word+" is successfully updated in database.")
			return render(request,'words/new_word.html',{"word":word_obj.word,"meaning":word_obj.meaning,"hindi":word_obj.hindi,"punjabi":word_obj.punjabi,
													"sentence":word_obj.sentence,"tags":word_obj.tags,'show_message':True,'message':'Sucessfully Updated','edit_word':True})

		else:
			print("form is invalid")
			return render(request,'words/new_word.html',{'show_message':True,'message':'Updation Failed','edit_word':True})

def update_quote(request,id):
	if request.method == 'POST':

		form = QuoteForm(request.POST)
		if len(form["quote"].value()) is not 0:
			quote = request.POST.get('quote')
			author = request.POST.get('author','')
			tags = request.POST.get('tags','')
			language = request.POST.get('language','')
			print(quote+" "+author+" "+language)
			Quote.objects.filter(id=id).update(quote= quote,author=author,tags=tags,language=language)
			quote_obj = Quote.objects.get(id=id)
			
			#return main_page(request)
			return render(request,'words/new_word.html',{'id':quote_obj.id,'quote':quote_obj.quote,'author':quote_obj.author,
									'language':quote_obj.language,'tags':quote_obj.tags,'show_message':True,'message':'Sucessfully Updated','edit_quote':True})

		else:
			print("form is invalid")
			return main_page(request)
			return render(request,'words/new_word.html',{'show_message':True,'message':'Updation Failed','edit_quote':True})

def update_reading(request,id):
	if request.method == 'POST':
		heading = request.POST.get('title',' ')
		author = request.POST.get('author',' ')
		tags = request.POST.get('tags',' ')
		language = request.POST.get('language',' ')
		passage = request.POST.get('passage',' ')
		Reading.objects.filter(id=id).update(heading=heading,author=author,tags=tags,language=language,passage=passage)
		reading_obj = Reading.objects.get(id=id)
		return render(request,'words/new_word.html',{'id':reading_obj.id,'title':reading_obj.heading,'passage':reading_obj.passage,
						'author':reading_obj.author,'tags':reading_obj.tags,'language':reading_obj.language,'edit_reading':True,'show_message':True,'message':"Reading successfully updated."})



# other views

def full_reading(request,id):
	read = Reading.objects.get(id=id)
	return render(request,'words/reading.html',{"obj":read})

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


###########################################################
########              test views

def test(request,id):
	print (id + " is id of quote")
	print("came in test view")
	return main_page(request)
