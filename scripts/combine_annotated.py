import os
import csv 
import json
from combine import write_posts

def add_posts(file_path, post_posts, post_keys):
    num_duplicates =0
    post_file = open(file_path,'r',encoding='utf-8')
    tsv_reader = csv.reader(post_file,delimiter="\t")
    for line in tsv_reader:
        
        name=line[0]
        title=line[1]
        if len(line) == 3:
            topic=line[2]
        else:
            topic = ''
        if name not in post_keys:
            post = {
                'name':name,
                'title':title,
                'coding': topic
            }
            post_keys.add(name)
            post_posts.append(post)
        else:
            num_duplicates +=1
    return num_duplicates

def main():

    file_list = ['annotated-1.tsv','annotated-3.tsv']
    base_path = os.path.join('..','data')

    path_list = []
    for path in file_list:
        file_path = os.path.join(base_path,path)
        path_list.append(file_path)

    post_posts = []
    post_keys = set()
    num_duplicates = 0
    
    for file_path in path_list:
        num_duplicates +=add_posts(file_path, post_posts, post_keys)
    
    output_file_path = os.path.join('..','all_posts','combined_annotated.tsv')
    write_posts(post_posts, output_file_path)

if __name__ == '__main__':
    main()