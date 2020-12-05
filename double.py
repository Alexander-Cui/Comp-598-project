import csv
from difflib import SequenceMatcher

#returns value between 0 and 1. closer the match, higher the number
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


################
input_file = "some.tsv"
output_file = "some_new.tsv"
#################

tsv_file = open(input_file)
read_tsv = csv.reader(tsv_file, delimiter="\t")

tsv_write = open(output_file,'w')

l=[]
occured=[]
count=0
count2=0
for row in read_tsv:
    l.append(row)
tsv_file.close()

for row in l:
    if row[0] in occured:
        continue
    else:
        occured.append(row[0])

    if row[2]!='':
        tsv_write.write(row[0]+'\t'+row[1]+'\t'+row[2]+'\n')
        continue
    else:
        str = row[0]+'\t'+row[1]+'\t'
        s=''
        for j in l:
            if j[0]!=row[0] and j[1]==row[1] and j[2]!='':
                count+=1
                s=j[2]

                break
            elif j[0]!=row[0] and j[2]!='' and abs(len(j[1])-len(row[1]))<25:
                n = similar(j[1], row[1])
                if n>0.65:
                    count2+=1
                    s=j[2]
                    if n<0.75: #posts that are just similar enough
                        print(j[1])
                        print(row[1])
                        print(n,'\n')
                    break
        str+=s+'\n'
        tsv_write.write(str)
tsv_write.close()

print("\n number of exact matches: ",count)
print("number of close matches: ",count2)
print("total number of posts matched: ",count+count2)
