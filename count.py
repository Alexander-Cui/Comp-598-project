import csv

def count(in_file):
    tsv_file = open(in_file)
    read_tsv = csv.reader(tsv_file, delimiter="\t")

    counter = [0] * 8

    for row in read_tsv:
        for i in range(7):
            i += 1
            if str(i) in row[2]:
                counter[i - 1] += 1
        if 'u' in row[2] or '0' in row[2] or 'U' in row[2]:
            counter[7] += 1
    tsv_file.close()
    return counter



def main():
    ################
    input_files=["./data/annotated-1.tsv","./data/annotated-2.tsv","./data/annotated-3.tsv"] #name of files with tsv data
    output_file = "./data/counted.tsv"
    #################


    counter=[0]*8

    for fname in input_files:
        temp=count(fname)
        for i in range(8):
            counter[i]+=temp[i]

    #write to file
    tsv_write = open(output_file,'w')
    topics=['Legitimacy of the election','COVID-19','Transition/Concession','Economy','International politics','Climate change','Trump bad','miscellaneous topic']
    for i in range(8):
        tsv_write.write(topics[i]+'\t'+str(counter[i])+'\n')
    tsv_write.close()





if __name__=='__main__':
    main()