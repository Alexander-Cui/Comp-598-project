import csv, json

def main():
    ################
    input_lib = ["./all_posts/20201122_politics.json","./all_posts/20201123_politics.json","./all_posts/20201124_politics.json"]
    input_con = ["./all_posts/20201122_conservative.json","./all_posts/20201123_conservative.json","./all_posts/20201124_conservative.json"]
    output_file = "info.json"
    #################
    results = {}
    results['lib'] = []
    results['con'] = []
    #open every file and
    for fname in input_lib:
        file = open(fname)
        # read_tsv = csv.reader(tsv_file, delimiter="\t")
        reader = file.readlines()
        for row in reader:
            row = json.loads(row)
            try:
                results['liberal'].append(row['data']['name'])
            except:
                print("name not foun???")
        file.close()

    for fname in input_con:
        file = open(fname)
        reader = file.readlines()

        for row in reader:
            json.loads(row)
            try:
                results['conservative'].append(row['data']['name'])
            except:
                print("name not foun???")

        file.close()




    tsv_write = open(output_file,'w')
    tsv_write.write(json.dumps(results))
    tsv_write.close()





if __name__=='__main__':
    main()