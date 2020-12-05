import csv, json



def main():
    ################
    input_file = "./all_posts/combined_annotated.tsv"
    output_file = "best.tsv"
    #################

    jfile = open("info.json")
    info = json.load(jfile)

    tsv_file = open(input_file)
    read_tsv = csv.reader(tsv_file, delimiter="\t")

    tsv_write = open(output_file,'w')

    error_count = 0
    for row in read_tsv:
        stringy = ""
        for i in row:
            stringy+=i+'\t'
        if row[0] in info['liberal']:
            stringy+='l'
        elif row[0] in info['conservative']:
            stringy+='c'
        else:
            error_count+=1
        stringy+='\n'
        tsv_write.write(stringy)
    tsv_write.close()

    print("errors/unfound matches",error_count)




if __name__=='__main__':
    main()