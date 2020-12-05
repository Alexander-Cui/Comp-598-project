import csv

nums=[1,2,3,4,5,6,7]
abrev = ['el','cov','trans','econ','inter','clim','bad']

def translate(st):
    for i in range(7):
        st = st.replace(abrev[i],str(nums[i]))
    return st

################
input_file = "./data/annotated.tsv"
output_file = "./data/annotated-3.tsv"
#################

tsv_file = open(input_file)
read_tsv = csv.reader(tsv_file, delimiter="\t")
tsv_write = open(output_file,'w')

for row in read_tsv:
    st = row[0]+'\t'+row[1]+'\t'
    st+=translate(row[2])+'\n'
    tsv_write.write(st)



tsv_file.close()
tsv_write.close()






