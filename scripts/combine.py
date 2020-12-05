import os
import csv 
import json


def write_posts(post_posts,output_file_path):
    csv_writer = csv.writer(open(output_file_path, 'w',encoding='utf-8'), delimiter='\t',lineterminator='\n')

    for post in post_posts:
        csv_writer.writerow(post.values())
    

def add_posts(file_path, post_posts, post_keys):
    post_file = open(file_path,'r')
    file_lines = post_file.readlines()
    num_duplicates = 0
    for post in file_lines:
        line = json.loads(post)
        name = line['data']['name']
        if name not in post_keys:
            post_keys.add(name)
            post_dict = {
                'name':name,
                'title':line['data']['title']
            }
            post_posts.append(post_dict)
        else:
            num_duplicates+=1
    return num_duplicates


def main():

    file_paths = []
    base_path = os.path.join('..','all_posts')
    for i in range(2,5):
        politics_name = f'raw_2020112{i}_politics.json'
        file_paths.append(os.path.join(base_path, politics_name))

        conservatives_name = f'raw_2020112{i}_conservative.json'
        file_paths.append(os.path.join(base_path, conservatives_name))
        

    post_keys = set()
    post_posts = []
    num_duplicates =0 

    for file_path in file_paths:
        num_duplicates += add_posts(file_path,post_posts,post_keys)

    output_file_path = os.path.join(base_path,'combined.tsv')
    print(len(post_posts))
    print(num_duplicates)

    write_posts(post_posts, output_file_path)

    # conservative_lines = conservatives_file.readlines()
    # politics_lines = politics_file.readlines()

    # num_duplicates += add_posts(conservative_lines, post_posts, post_keys)
    # num_duplicates += add_posts(politics_lines,post_posts,post_keys)




if __name__ == '__main__':
    main()