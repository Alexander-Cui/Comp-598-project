import argparse
import json
import os
import random
import csv

def convert_to_csv(subreddit):
    input_file_path = os.path.join('..','all_posts', f'200_{subreddit}.json')
    output_file_path = os.path.join('..','all_posts', f'200_{subreddit}.csv')
    json_file = open(input_file_path,'r')
    csv_file = open(output_file_path,'w',encoding='utf-8')
    csv_writer = csv.writer(csv_file, lineterminator = '\n')

    json_file_lines = json_file.readlines()
    for line in json_file_lines:
        line = line.strip('\n')
        json_data = json.loads(line)['data']
        json_csv = {
            'selftext':json_data['selftext'],
            'title':json_data['title']
        }
        csv_writer.writerow(json_csv.values())


def count_lines_of_type_and_write(input_filename, subreddit):
    count = 0
    #writes and counts for all files of type (politics or conservative)
    for filename in input_filename:
        input_file_path = os.path.join('..','all_posts', filename)
        output_file_path = os.path.join('..','all_posts', f'{subreddit}.json')
        count += write_file_count_lines(input_file_path,output_file_path)
    return count

def write_file_count_lines(input_file_location, output_file_location):
    #read file
    json_file = open(input_file_location,'r')
    json_file_lines = json_file.readlines()

    #write file
    with open(output_file_location,'a') as outfile:
        for line in json_file_lines:
            outfile.write(line)

    #return number of lines
    return len(json_file_lines)

def write_random_line(subreddit, num_lines, total_lines):

    random_lines = [random.randint(1,total_lines) for i in range(num_lines)]

    input_file_path = os.path.join('..','all_posts', f'{subreddit}.json')
    json_file = open(input_file_path,'r')
    json_file_lines = json_file.readlines()

    output_file_path = os.path.join('..','all_posts', f'200_{subreddit}.json')
    with open(output_file_path,'a') as outfile:
        for i, line in enumerate(json_file_lines):
            if i in random_lines:
                outfile.write(line)
    



def main():
    politics = ['20201122_politics.json','20201123_politics.json','20201124_politics.json']
    conservatives = ['20201122_conservative.json','20201123_conservative.json','20201124_conservative.json']

    num_politics = count_lines_of_type_and_write(politics,'politics')
    num_conservatives = count_lines_of_type_and_write(conservatives,'conservatives')

    total = num_politics + num_conservatives

    ratio_politics = num_politics/total 
    ratio_conservatives = num_conservatives/total 

    print(ratio_conservatives)
    print(ratio_politics)

    num_politics_to_pull = round(ratio_politics  * 200)
    num_conservatives_to_pull = round(ratio_conservatives * 200)

    write_random_line('politics',num_politics_to_pull,num_politics)
    write_random_line('conservatives',num_conservatives_to_pull,num_conservatives)

    convert_to_csv('politics')
    convert_to_csv('conservatives')
    
if __name__ == "__main__":
    main()
