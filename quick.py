import wikipedia
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-t" "--type", 
	             required=True, 
	             help="type of search to use (wiki or word search)")
ap.add_argument("-w" "--word", 
	             required=True, 
	             help="the word you'd like to be searched")

args = vars(ap.parse_args())

search_engine = args['type']
word = args["word"]

def wiki_search(word):
	print(wikipedia.summary(word))

wiki_search(word)









