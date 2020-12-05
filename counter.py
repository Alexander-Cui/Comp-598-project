import csv, json

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def plot(data):
    labels = ['Legitimacy of the election','COVID-19','Transition/Concession','Economy','International politics','Climate change','Trump bad','miscellaneous topic']

    sum1 = sum(data['trump'])
    sum2 = sum(data['biden'])
    datap ={}
    datap['trump'] = [(i*100)/sum1 for i in data['trump']]
    datap['biden'] = [(i * 100) / sum2 for i in data['biden']]

    trump_means = datap['trump']
    biden_means = datap['biden']
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, trump_means, width, label='Posts w/ Trump',color='orange')
    rects2 = ax.bar(x + width / 2, biden_means, width, label='Posts w/ Biden')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Percentage (rounded)')
    ax.set_title('Percent of engagement of topic')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 0),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)

    fig.tight_layout()

    plt.show()

# trump and biden, and respective occurrences of categories
def count(in_file):
    tsv_file = open(in_file)
    read_tsv = csv.reader(tsv_file, delimiter="\t")

    results = {}
    results['biden'] = [0] * 8
    results['trump'] = [0] * 8


    for row in read_tsv:
        for i in range(7):
            i += 1
            if 'biden' in row[1].lower():
                if str(i) in row[2]:
                    results['biden'][i - 1] += 1
                if 'u' in row[2] or '0' in row[2] or 'U' in row[2]:
                    results['biden'][7]+= 1/7
            if 'trump' in row[1].lower():
                if str(i) in row[2]:
                    results['trump'][i - 1] += 1
                if 'u' in row[2] or '0' in row[2] or 'U' in row[2]:
                    results['trump'][7] += 1.0/7
    tsv_file.close()

    results['trump'][7] = int(results['trump'][7])
    results['biden'][7] = int(results['biden'][7])
    return results


# r/politics and r/conservative engagement respective occurrences of categories
def count2():
    in_file = "best.tsv"
    tsv_file = open(in_file)
    read_tsv = csv.reader(tsv_file, delimiter="\t")

    results = {}
    results['liberal'] = [0] * 8
    results['conservative'] = [0] * 8


    for row in read_tsv:
        for i in range(7):
            i += 1
            if 'l' in row[4].lower():
                if str(i) in row[2]:
                    results['liberal'][i - 1] += 1
                if 'u' in row[2] or '0' in row[2] or 'U' in row[2]:
                    results['liberal'][7]+= 1/7
            if 'c' in row[4].lower():
                if str(i) in row[2]:
                    results['conservative'][i - 1] += 1
                if 'u' in row[2] or '0' in row[2] or 'U' in row[2]:
                    results['conservative'][7] += 1.0/7
    tsv_file.close()

    results['conservative'][7] = int(results['conservative'][7])
    results['liberal'][7] = int(results['liberal'][7])
    return results



def main():
    ################
    input_file="./all_posts/combined_annotated.tsv" #name of files with tsv data
    output_file = "./data/counted.json"
    #################

    results=count(input_file)
    #write to file
    tsv_write = open(output_file,'w')
    tsv_write.write(json.dumps(results))
    # topics=['Legitimacy of the election','COVID-19','Transition/Concession','Economy','International politics','Climate change','Trump bad','miscellaneous topic']
    # for i in range(8):
    #     tsv_write.write(topics[i]+'\t'+str(counter[i])+'\n')
    tsv_write.close()

    plot(results)




if __name__=='__main__':
    main()