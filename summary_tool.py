#Original algorithm taken from shlomibabluki on github, modified for personal use, and ported from v2 to v3

from __future__ import division
import re

# This is a naive text summarization algorithm
# Created by Shlomi Babluki
# April, 2013


class SummaryTool(object):

    # Naive method for splitting a text into sentences
    def split_content_to_sentences(self, content):
        content = content.replace("\n", ". ")
        return content.split(". ")

    # Naive method for splitting a text into paragraphs
    def split_content_to_paragraphs(self, content):
        return content.split("\n\n")

    # Caculate the intersection between 2 sentences
    def sentences_intersection(self, sent1, sent2):

        # split the sentence into words/tokens
        s1 = set(sent1.split(" "))
        s2 = set(sent2.split(" "))

        # If there is not intersection, just return 0
        if (len(s1) + len(s2)) == 0:
            return 0

        # We normalize the result by the average number of words
        return len(s1.intersection(s2)) / ((len(s1) + len(s2)) / 2)

    # Format a sentence - remove all non-alphbetic chars from the sentence
    # We'll use the formatted sentence as a key in our sentences dictionary
    def format_sentence(self, sentence):
        sentence = re.sub(r'\W+', '', sentence)
        return sentence

    # Convert the content into a dictionary <K, V>
    # k = The formatted sentence
    # V = The rank of the sentence
    def get_sentences_ranks(self, content):

        # Split the content into sentences
        sentences = self.split_content_to_sentences(content)

        # Calculate the intersection of every two sentences
        n = len(sentences)
        values = [[0 for x in range(n)] for x in range(n)]
        for i in range(0, n):
            for j in range(0, n):
                values[i][j] = self.sentences_intersection(sentences[i], sentences[j])

        # Build the sentences dictionary
        # The score of a sentences is the sum of all its intersection
        sentences_dic = {}
        for i in range(0, n):
            score = 0
            for j in range(0, n):
                if i == j:
                    continue
                score += values[i][j]
            sentences_dic[self.format_sentence(sentences[i])] = score
        return sentences_dic

    # Return the best sentence in a paragraph
    def get_best_sentence(self, paragraph, sentences_dic):

        # Split the paragraph into sentences
        sentences = self.split_content_to_sentences(paragraph)

        # Ignore short paragraphs
        if len(sentences) < 2:
            return ""

        # Get the best sentence according to the sentences dictionary
        best_sentence = ""
        max_value = 0
        for s in sentences:
            strip_s = self.format_sentence(s)
            if strip_s:
                if sentences_dic[strip_s] > max_value:
                    max_value = sentences_dic[strip_s]
                    best_sentence = s

        return best_sentence

    # Build the summary
    def get_summary(self, title, content, sentences_dic):

        # Split the content into paragraphs
        paragraphs = self.split_content_to_paragraphs(content)

        # Add the title
        summary = []
        summary.append(title.strip())
        summary.append("")

        # Add the best sentence from each paragraph
        for p in paragraphs:
            sentence = self.get_best_sentence(p, sentences_dic).strip()
            if sentence:
                summary.append(sentence)

        return ("\n").join(summary)

def main():

    # Demo
    # Content from: "http://thenextweb.com/apps/2013/03/21/swayy-discover-curate-content/"

    title = """
    Charles Barkley
    """

    content = """
    Charles Wade Barkley (born February 20, 1963) is an American retired professional basketball player and current analyst on the television program Inside the NBA. Nicknamed "Chuck", "Sir Charles", and "The Round Mound of Rebound", Barkley established himself as one of the National Basketball Association's dominant power forwards.[1] An All-American center at Auburn, he was drafted as a junior by the Philadelphia 76ers with the 5th pick of the 1984 NBA draft. He was selected to the All-NBA First Team five times, the All-NBA Second Team five times, and once to the All-NBA Third Team. He earned eleven NBA All-Star Game appearances and was named the All-Star MVP in 1991. In 1993, he was voted the league's Most Valuable Player and during the NBA's 50th anniversary, named one of the 50 Greatest Players in NBA History. He competed in the 1992 and 1996 Olympic Games and won two gold medals as a member of the United States' "Dream Team". Barkley is a two-time inductee into the Naismith Memorial Basketball Hall of Fame, being inducted in 2006 for his individual career, and in 2010 as a member of the "Dream Team".[2][3]

Barkley was popular with the fans and media and made the NBA's All-Interview Team for his last 13 seasons in the league.[1] He was frequently involved in on- and off-court fights and sometimes stirred national controversy, as in March 1991 when he spat on a young girl while attempting to spit at a heckler,[4] and as in 1993 when he declared that sports figures should not be considered role models. Short for a power forward, Barkley used his strength and aggressiveness to become one of the NBA's most dominant rebounders. He was a versatile player who had the ability to score, create plays, and defend. In 2000, he retired as the fourth player in NBA history to achieve 20,000 points, 10,000 rebounds and 4,000 assists.[5]

Since retiring as a player, Barkley has had a successful career as a television NBA analyst. He works with Turner Network Television (TNT) alongside of Shaquille O'Neal, Kenny Smith, and Ernie Johnson as a studio pundit for its coverage of NBA games[6] and is a spokesman for CDW. In addition, Barkley has written several books and has shown an interest in politics; in October 2008, he announced that he would run for Governor of Alabama in 2014,[7] but he changed his mind in 2010.
    """

    # Create a SummaryTool object
    st = SummaryTool()

    # Build the sentences dictionary
    sentences_dic = st.get_sentences_ranks(content)

    # Build the summary with the sentences dictionary
    summary = st.get_summary(title, content, sentences_dic)

    # Print the summary
    print (summary)

    # Print the ratio between the summary length and the original length
    print("")
    print("Original Length %s" % (len(title) + len(content)))
    print ("Summary Length %s" % len(summary))
    print ("Summary Ratio: %s" % (100 - (100 * (len(summary) / (len(title) + len(content))))))

if __name__ == '__main__':
    main()


