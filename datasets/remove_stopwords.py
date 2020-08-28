# remove weibo stop words in files
from data_utils import write_samples

# stopwords file
f_stopwords = open('weibo_stopwords.txt', 'r', encoding='utf-8')
sw = f_stopwords.readlines()
f_stopwords.close()

stopwords = []
for line in sw:
    line = line.replace('\n', '')
    stopwords.append(line)

# train file or dev file
fin = open('dev-1000-seg.txt', 'r', encoding='utf-8')
lines = fin.readlines()
fin.close()

for i in range(0, len(lines), 3):
    lines[i] = lines[i].replace('\n', '')
    new_line = ""
    for w in lines[i].split(' '):
        if w not in stopwords:
            new_line += w + ' '
    new_line += '\n'
    lines[i] = new_line

with open('dev-1000-seg-rmstopwords.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        file.write(line)
