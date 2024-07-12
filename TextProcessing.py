import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data files
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Initialize lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
all_stopwords = stopwords.words('english')

# Specify words to remove from stopwords
words_to_remove_from_stopwords = [
    'not','in',"can't",'no','nor','a','b','c','d','with','but','don', "don't",'ain',
    'aren', "aren't", 'couldn', "couldn't",'didn', "didn't", 'doesn', "doesn't",'won',
    "won't", 'wouldn', "wouldn't","why"
]

# Remove specified words from stopwords
for word in words_to_remove_from_stopwords:
    if word in all_stopwords:
        all_stopwords.remove(word)


class TextPreprocessing():
    
    @staticmethod
    def text_processing(text):
        corpus = []
        review = re.sub('[^a-zA-Z\']', ' ', text)
        review = review.lower()
        review = review.split()
        review = [lemmatizer.lemmatize(word) for word in review if not word in set(all_stopwords)]
        review = ' '.join(review)
        corpus.append(review)
        return corpus
