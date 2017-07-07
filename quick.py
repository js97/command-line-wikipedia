import wikipedia as wiki
import argparse


def wiki_search(word):
	search_result_list = wiki.search(word, results=5)
	count = 1
	print('\nWhich result did you mean? Choose corresponding number:')
	for entry in search_result_list:
		print(str(count)+')'+entry)
		count = count+1
	user_choice = input('\n>>')
	print(
		search_result_list[int(user_choice)-1]+
		":\n\n"+
		wiki.summary(search_result_list[int(user_choice)-1])+
		"\n\n")

def main():
	print('\n\nWelcome to Quick Wiki Search. A command line tool for easy wikipedia search. Enter a word to get the summary. Enter \'q\' to exit.')
	user_input = input('>>')
	while(user_input is not 'q'):	
		wiki_search(user_input)
		user_input = input('\n>>')

if __name__ == '__main__':
	main()





