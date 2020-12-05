import json

with open("all_posts/200_conservatives.json",'r') as fd:
    # data = json.load(fd)
    lines = fd.readlines()
    count = 0
    f = open("out_c.csv",'w')
    f.write('title	topics\n')
    for line in lines:
        count+=1
        if count<39:
            continue
        data = json.loads(line)
        title = data['data']['title']
        # with open('data/title_pol_1.csv') as f:
        #     f.write(title)
        #
        str = data['data']['title']+'\n'
        str = str.replace("'","")
        f.write(str)
        print(data['data']['title'])
    f.close()

