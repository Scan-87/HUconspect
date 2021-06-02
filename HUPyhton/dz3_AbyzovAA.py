import os

dirname = input("Please enter the name of your dir\n>>> ")
os.chdir(dirname)
# print(os.listdir())

#Open files
result = open("result.txt", 'w')
log = open("result.log", 'w')

#You can apply filters here
usefulfiles = []
dirfiles = os.listdir()
for file in dirfiles:
    if file == 'result.txt':
        continue
    elif file[-4:] != '.txt':
        continue
    else:
        usefulfiles.append(file)

#Write number of files to log
log.write(str(len(usefulfiles)))
log.write("\n")

for filename in usefulfiles:
    file = open(filename)
    content = file.read()
    # print("*****************")
    # print(content)
    result.write("\n***************\n")
    result.write(content)
    log.write(filename)
    log.write(", ")
    file.close()

result.close()
log.close()