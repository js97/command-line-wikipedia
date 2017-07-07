import wikipedia as wiki
import argparse


def wiki_search(word):
	search_result_list = wiki.search(word, results=5)
	count = 1
	print('\nWHICH ONE DID YOU MEAN? CHOOSE CORRESPONDING NUMBER:')
	for entry in search_result_list:
		print('   '+str(count)+')  '+entry)
		count = count+1
	user_choice = input('\n>>')
	try:
		str_to_print = (search_result_list[int(user_choice)-1]+
						":\n\n"+
						wiki.summary(search_result_list[int(user_choice)-1])+
						"\n\n")
		#set the above string to a variable before printing to allow for exception to be thrown before printing
		print(str_to_print)
	except wiki.exceptions.DisambiguationError as e:
		#this area still requires a fix. Some warnings about BeautifulSoup's html parser come up, as well as suggest() seems to always return None type
		#catches case where wiki returns a list rather than a single wiki page
		#will use wiki's best suggestion instead
		


		#wiki_page = wiki.suggest(search_result_list[int(user_choice)-1])
		#print(wiki.suggest(search_result_list[int(user_choice)-1]))
		#print(wiki_page)
		print('Something isn\'t working.')
		


def main():
	print('\n\n/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/==/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/')
	print('\n   WELCOME TO WIKI QUICK SEARCH. A COMMAND LINE TOOL FOR EASY WIKI SEARCH. ENTER A WORD TO GET THE SUMMARY. ENTER \'q\' TO EXIT.\n')
	print('/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/==/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/\n')
	user_input = input('>>')
	while(user_input is not 'q'):	
		wiki_search(user_input)
		user_input = input('\n>>')


if __name__ == '__main__':
	main()





