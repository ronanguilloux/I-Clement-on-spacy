import spacy
from spacy import displacy

import warnings
warnings.filterwarnings("ignore")

file_source = 'data/clement-i-greek.short.txt'
file = open(file_source, 'r')
text = file.read()
print(text)

nlp = spacy.load("grc_odycy_joint_trf")
doc = nlp(text)

def parse(token):
    print("\nINDEX", index, "\t",
        "TEXT:",token.text,"\t",
         "ORTH:",token.orth_,"\t",
         "LEMMA:",token.lemma_,"\n",
         
         "TAG:",token.tag_,"\t",
         "DEP:",token.dep_,"\t",
         "SHAPE:",token.shape_,"\t",
         "IS_ALPHA:",token.is_alpha,"\t",
         "IS_STOP:",token.is_stop,"\n",
         
         "POS:",token.pos_,"\t",
         "MORPH (full):",token.morph,"\n",
         "Case:",token.morph.get('Case'),"\t",
         "Gender:",token.morph.get('Gender'),"\t",
         "Number:",token.morph.get('Number'),"\t",
         "HEAD:",token.head)

index = 0
index_max = 3
print("Processing the first 4 words:")
for token in doc:
   parse(token)
   index+=1
   if (index>index_max):
    break

parse(doc[5]) # the first verb of that sentence: παροικοῦσα

sentence_spans = list(doc.sents)
print(sentence_spans)

lemmatizer = nlp.get_pipe("frequency_lemmatizer")
doc = nlp(text)
filtered_lemmas = [token for token in doc if (token.pos_ != "PUNCT" and token.is_stop == False)]
print(len(doc),"tokens in total, but only",len(filtered_lemmas),"are useful:")
print([token.lemma_ for token in filtered_lemmas])

def nounize(token):
    print(token.text, token.dep_, token.head.text, token.head.pos_, [child for child in token.children])
nounize(doc[2])

displacy.serve(sentence_spans[0], style="dep", host="localhost", auto_select_port=True)

