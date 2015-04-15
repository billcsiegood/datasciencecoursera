import sys
from nltk.util import ngrams

clean_list = "abcdefghijklmnopqrstuvwxyz 123456789'"
def cleanString(line,clean_list) :
    sentence = ""
    line = line.lower()
    for word in line :
        if word in clean_list :
            sentence += word
        elif sentence != '':
            sentence += " "
            
    return sentence

try :
    fh = open (sys.argv[1],'r',encoding="utf-8")
    n = int(sys.argv[2])
except:
    print ("Please input like this :python ng4.py  apple.txt 1")
    quit()

i = 0
mydict={}

while True:
    line = fh.readline()
    if line =='':
        break
    else:

        i += 1
        line = cleanString(line,clean_list)
        sixgrams = ngrams(line.split(), n)
        for grams in sixgrams:
#       print grams
            if grams in mydict:
                mydict[grams][0] += 1
                mydict[grams].append(i) 
            else:
                mydict[grams]=[1, i]
fh.close()

sortlist = sorted(mydict.items(), key=lambda x: x[1][0] ,reverse = True)

# print mydict[('Reed',)]
#print (mydict[('I','was')])
for item in sortlist[:5] :
    print ("{} has {} times in {}".format(item[0],item[1][0],item[1][1:]))
