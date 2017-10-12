import wikipedia as wiki
import argparse
import summary_tool

parser = argparse.ArgumentParser()
parser.add_argument('--term',
	                dest='term', 
	                type=str)

search_term = parser.parse_args()
search_term = search_term.term


def wiki_search(word):
	search_result = wiki.page(word)
	st = summary_tool.SummaryTool()
	summary = st.get_summary(search_result.title, 
									   search_result.content, 
									   st.get_sentences_ranks(search_result.content))
	print(summary)
def main():
	wiki_search(search_term)


if __name__ == '__main__':
	main()





