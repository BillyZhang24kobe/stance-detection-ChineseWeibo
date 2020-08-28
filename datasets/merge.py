# check file encoding format
# import chardet
# f = open('test-1000.txt', 'rb')
# result = chardet.detect(f.read())
# print(result)

import codecs
f = codecs.open("dev-1000.txt", 'r', 'GB18030')
ff = f.read()
file_object = codecs.open('dev-1000-new.txt', 'w', 'utf-8')
file_object.write(ff)

# with open("test-1000.txt", 'r') as file:
#     for line in file.readlines():
#         print(line)
# count = 3001
# with codecs.open("train-3000.txt", "a", "utf-8") as train:
#     with codecs.open("test-1000.txt", "r", "utf-8") as test:
#         train.write(test.read())
        # for line in test.readlines():
        #     new_line = ""
        #     new_line += str(count) + '\t'
        #     for s in range(1, len(line.strip('\t'))):
        #         if s == len(line.strip("\t")) - 1:
        #             new_line += line.strip("\t")[s] + '\n'
        #         else:
        #             new_line += line.strip("\t")[s] + "\t"
        #     train.write(new_line)
        #     count += 1
