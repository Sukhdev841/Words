from django.conf.urls import url,include

from . import views

app_name = 'words'

urlpatterns = [
	# redirecting to home page
	url(r'^$',views.main_page,name="main_page"),

	####################################################
	#		 all main pages 

	url(r'^all-words-page/$',views.all_words_page,name="all_words_page"),
	url(r'^all-quotes/$',views.all_quotes_page,name="all_quotes_page"),
	url(r'^all-readings/$',views.all_readings_page,name="all_readings_page"),


	######################################################
	#    redirecting to new insertion pages

	url(r'^new-word-page/$',views.new_word_page,name="new_word_page"),
	url(r'^new-quote-page/$',views.new_quote_page,name = "new_quote_page"),
	url(r'^new-reading/$',views.new_reading_page,name="new_reading_page"),
	url(r'^new-passage-word-page/(?P<word>\w+)/$',views.new_passage_word_page,name="new_passage_word_page"),

	url(r'^update-word-page/(?P<word_id>\w+)/$',views.update_word_page,name="update_word_page"),
	url(r'^update-quote-page/(?P<quote_id>\w+)/$',views.update_quote_page,name="update_quote_page"),
	url(r'^update-reading-page/(?P<id>\w+)/$',views.update_reading_page,name="update_reading_page"),


	##########################################################
	# saving data from new insertion pages
	url(r'^save-word/$',views.save_word,name="save_word"),
	url(r'^save-quote/$',views.save_quote,name="save_quote"),
	url(r'^save-reading/$',views.save_reading,name="save_reading"),
	url(r'^save-passage-word/$',views.save_passage_word,name="save_passage_word"),

	#########################################################
	##     updating data pages

	url(r'^update-word/(?P<word>\w+)/$',views.update_word,name="update_word"),
	url(r'^update-quote/(?P<id>\w+)/$',views.update_quote,name="update_quote"),
	url(r'^update-reading/(?P<id>\w+)/$',views.update_reading,name="update_reading"),

	##########################################################
	##        deleting data pages

	url(r'^delete-word/(?P<word>\w+)/$',views.delete_word,name="delete_word"),
	url(r'^delete-quote/(?P<id>\w+)/$',views.delete_quote,name="delete_quote"),
	url(r'^delete-reading/(?P<id>\w+)/$',views.delete_reading,name="delete_reading"),

	##########################################################
	##                   next and previous words urls
	url(r'^next-words/$',views.next_words,name="next_words"),
	url(r'^prev-words/$',views.prev_words,name="prev_words"),

	#########################################################
	###                  passage urls
	url(r'^process-passage/$',views.process_passage,name="process_passage_page"),
	url(r'^passage-words-page/$',views.passage_words_page,name="passage-words-page"),
	url(r'^add-passage-words-page/(?P<word>\w+)/$',views.add_passage_words_page,name="add-passage-word-page"),

	###########################################################
	########               javascript views
	url(r'^save-new-passage-word/$',views.save_new_passage_word,name="save_new_passage_word"),
	url(r'^save-new-exception-word/$',views.save_new_exception_word,name="save-new-exception-word"),

	##########################################################
	# 							other urls

	url(r'^search/$',views.search,name="search"),
	url(r'^full_reading/(?P<id>\w+)/$',views.full_reading,name="full_reading"),


	############################################################
	##############                Test urls
	url(r'^test/(?P<id>\w+)/$',views.test,name="test"),
	url(r'^test_/$',views.test_,name="test_"),

]