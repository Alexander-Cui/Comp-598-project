import argparse
import os
import csv 
import json
import string
import math
import pprint


def compute_top_ten(tfidf, max_tfidf):

    for key, value in tfidf.items():
        top_ten =  sorted(value, key=value.get, reverse=True)[:10]
        for word in top_ten:
            max_tfidf[key][word] = tfidf[key][word]
     


def compute_tfidf(word_freq,topic_freq,idf_freq,total_words, tfidf):

    for key, value in topic_freq.items():
        for word, count in value.items():
            if word not in word_freq or word not in idf_freq:
                continue
            word_in_doc = idf_freq[word]
            tfidf[key][word] = (count ) * math.log( (total_words / idf_freq[word] ) )    

def count_total_words():
    count = 0
    combined_file_path = os.path.join('..','all_posts','combined.tsv')
    combined_file = open(combined_file_path,'r', encoding='utf-8')
    tsv_reader = csv.reader(combined_file, delimiter="\t") 

    for line in tsv_reader:
        name=line[0]
        title=line[1]
        count += len(title.split())
    return count

def count_document_words(word_freq, idf_freq):
    combined_file_path = os.path.join('..','all_posts','combined.tsv')
    combined_file = open(combined_file_path,'r',encoding='utf-8')

    tsv_reader = csv.reader(combined_file, delimiter="\t")
    for line in tsv_reader:
        title=line[1]
        for word in title.split():
            word = word.lower()
            word = word.translate(str.maketrans('', '', string.punctuation))

            if word in idf_freq:
                idf_freq[word] += 1
            else:
                idf_freq[word] = 1
    

def compute_word_in_topic(word_freq, topic_freq):
    annotated_file_path = os.path.join('..','all_posts','combined_annotated.tsv')
    annotated_file = open(annotated_file_path,'r',encoding='utf-8')
    tsv_reader = csv.reader(annotated_file, delimiter="\t")
    for line in tsv_reader:
        if line[0]=='Name':
            continue
        name=line[0]
        title=line[1]
        topic = line[2]
        for word in title.split():
            word = word.lower()
            word = word.translate(str.maketrans('', '', string.punctuation))
            if word in word_freq:
                word_freq[word]+=1
            else:
                word_freq[word] = 1
            for top in topic.split(','):
                if top == 'u' or top == 'U':
                    topic_key = '8'
                else:
                    topic_key = top
                if word in topic_freq[topic_key]:
                    topic_freq[topic_key][word] +=1
                else:
                    topic_freq[topic_key][word] = 1



def main ():

    document_total_words = count_total_words()

    word_freq = {
    }
    topic_freq = {
        '1':{},
        '2':{},
        '3':{},
        '4':{},
        '5':{},
        '6':{},
        '7':{},
        '8':{}
    }
    idf_freq = {
    }

    tfidf= {
        '1':{},
        '2':{},
        '3':{},
        '4':{},
        '5':{},
        '6':{},
        '7':{},
        '8':{}
    }



    compute_word_in_topic(word_freq, topic_freq)
    count_document_words(word_freq,idf_freq)

    compute_tfidf(word_freq,topic_freq,idf_freq,document_total_words,tfidf)

    max_tfidf = {
        '1':{},
        '2':{},
        '3':{},
        '4':{},
        '5':{},
        '6':{},
        '7':{},
        '8':{}
    }

    compute_top_ten(tfidf, max_tfidf)
    print(max_tfidf)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(max_tfidf)


if __name__ == '__main__':
    main()