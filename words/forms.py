from django import forms

class WordForm(forms.Form):
	word = forms.CharField(max_length = 30)
	meaning = forms.CharField(max_length= 500)
	hindi = forms.CharField(max_length= 500)
	punjabi = forms.CharField(max_length= 500)
	sentence = forms.CharField(max_length = 300)

class SearchForm(forms.Form):
	search_field = forms.CharField(max_length=1000)

class ParagraphForm(forms.Form):
	paragraph_field = forms.CharField(widget=forms.Textarea)