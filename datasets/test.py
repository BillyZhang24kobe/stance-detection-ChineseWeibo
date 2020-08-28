import codecs

with codecs.open("train-3000-raw.txt", 'r', 'utf-8') as f:
    for line in f:
        if len(line.split('\t')) != 4: continue
        if line.split("\t")[3] == 'AGAINST':
            print(line)
        # try:
        #     print(line.split('\t')[3])
        # except Exception:
        #     print(len(line.split('\t')))
        #     exit()
