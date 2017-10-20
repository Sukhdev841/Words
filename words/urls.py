from django.conf.urls import url,include

from . import views

app_name = 'words'

urlpatterns = [
	# redirecting to home page
	url(r'^$',views.main,name="main"),

	# ####################################################
	# #		 all main pages 

	# url(r'^all-words/$',views.all_words,name="all_words_page"),
	# url(r'^all-quotes/$',views.all_quotes,name="all_quotes_page"),
	# url(r'^all-readings/$',views.all_readings,name="all_readings_page"),


	# ######################################################
	# #    redirecting to new insertion pages

	# url(r'^new-word/$',views.new_word,name="new_word_page"),
	# url(r'^new-quote/$',views.new_quote,name = "new_quote_page"),
	# url(r'^new_reading/$',views.new_reading,name="new_reading_page"),


	# ##########################################################
	# # saving data from new insertion pages
	# url(r'^save-word/$',views.save_word,name="save_word_page"),
	# url(r'^save-quote/$',views.save_quote,name="save_quote_page"),
	# url(r'^save-reading/$',views.save_reading,name="save_reading_page"),

	# #########################################################
	# ##     updating data pages

	# url(r'^update-word/(?P<word>\w+)/$',views.update_word,name="update_word_page"),
	# url(r'^update-quote/(?P<quote_id>\w+)/$',views.update_quote,name="update_quote_page"),
	# url(r'^update-reading/(?P<reading_id>\w+)/$',views.update_reading,name="update_reading_page"),

	# ##########################################################
	# ##        deleting data pages

	# url(r'^delete-word/(?P<word>\w+)/$',views.delete_word,name="delete_word_page"),
	# url(r'^delete-quote/(?P<quote_id>\w+)/$',views.delete_quote,name="delete_quote_page"),
	# url(r'^delete-reading/(?P<reading_id>\w+)/$',views.delete_reading,name="delete_reading_page"),

	# saves word from form into database
	url(r'^save/$',views.save_word,name="save"),
	# updates word from form into database
	url(r'^edit_commit/(?P<word>\w+)/$',views.edit_commit_word,name="edit"),
	# redirecting to edit word form
	url(r'^edit/(?P<word>\w+)/$',views.edit_word,name='edit_word'),
	# redirecting to save word page
	url(r'^save_a_word/$',views.save_word_page,name="save_word_page"),
	# this page shows all word
	url(r'^all-words/$',views.show_all_words,name="show_all_words"),
	# for searching a particular word
	url(r'^all-words/search-result/$',views.search,name='search'),
	# for redirecting to somewhere (don't know where used)
	url(r'^$',views.redirect,name="redirect"),
	# deletes the word from the database
	url(r'^delete/(?P<word>\w+)/$',views.delete_word,name='delete_word'),
	# going to paragraph read page
	url(r'^paragraph/$',views.paragraph_reading,name='paragraph_reading'),
	# submitting the paragraph read form
	url(r'^paragraph/submit/$',views.paragraph_reading_submition,name='paragraph_reading_submition'),
	# saving a  word from paragraph
	url(r'^paragraph/save-new-word/(?P<word>\w+)/$',views.save_word_paragraph,name="save_word_para"),

	# # save a quote in database
	# url(r'^new_quote/$',views.show_quote_form,name="new_quote"),
]