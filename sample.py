import pandas as pd
from keybert import KeyBERT
df = pd.read_csv( r'C:\Users\safwa\Desktop\Safwan\Final year project\history.csv')
doc = """
         Supervised learning is the machine learning task of learning a function that
         maps an input to an output based on example input-output pairs. 
      """
kw_model = KeyBERT()
keywords = kw_model.extract_keywords(doc)
#for x in range( 1016 ) :
#  print( "Title : " , df['title'][x] ) 
  

from keybert import KeyBERT
import pandas as pd 
df = pd.read_csv('history.csv')
for x in range(1016) :
  doc = df['title'][x]
  kw_model = KeyBERT()
  key = kw_model.extract_keywords(doc, keyphrase_ngram_range=(1, 3) , top_n=1 )
 
  print ( "Title : " , df['title'][x] , "    Keyword : " , key )

