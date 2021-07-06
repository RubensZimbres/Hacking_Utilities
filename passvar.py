import numpy as np
from itertools import permutations
from collections import OrderedDict
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('--f', dest='file', type=str, default=0, help='Path of input file')
parser.add_argument('--d', dest='output-dir', type=str, default=0, help='Path of output directory')
args = vars(parser.parse_args())

x=0
outcome=[]
with open(args['file'],'r', encoding="latin-1") as f:
    my_list = list(f)
    my_list = [x.rstrip() for x in my_list] 
    for word in my_list:
        try:
            x+=1
            if x % 100000 == 0:
                print(x)
            #print(word)
            #print(word[::-1])
            outcome.append(word.replace("o","0"))
            outcome.append(word.replace("i","1"))
            outcome.append(word.replace("z","2"))
            outcome.append(word.replace("s","$"))
            outcome.append(word.replace("e","3"))
            outcome.append(word.replace("a","@"))
            outcome.append(word.replace("g","9"))
            outcome.append(word.replace("o","0").replace("i","1").replace("z","2").replace("s","$").replace("e","3").replace("a","@").replace("g","9"))

            outcome.append(word.title().replace("o","0"))
            outcome.append(word.title().replace("i","1"))
            outcome.append(word.title().replace("z","2"))
            outcome.append(word.title().replace("s","$"))
            outcome.append(word.title().replace("e","3"))
            outcome.append(word.title().replace("a","@"))
            outcome.append(word.title().replace("g","9"))
            outcome.append(word.title().replace("o","0").replace("i","1").replace("z","2").replace("s","$").replace("e","3").replace("a","@").replace("g","9"))

            outcome.append(word+'+')
            outcome.append(word+'!')
            outcome.append(word+'&')
            outcome.append(word+'#')
            outcome.append(word+'-')
            outcome.append(word+'%')
            outcome.append(word.title())
            outcome.append(word.title()+'+')
            outcome.append(word.title()+'!')
            outcome.append(word.title()+'&')
            outcome.append(word.title()+'#')
            outcome.append(word.title()+'-')
            outcome.append(word.title()+'%')

            word1 = word[::-1]
            outcome.append('+'+word1)
            outcome.append('!'+word1)
            outcome.append('&'+word1)
            outcome.append('#'+word1)
            outcome.append('-'+word1)
            outcome.append('%'+word1)
            outcome.append('+'+word1)
            outcome.append('!'+word1)
            outcome.append('&'+word1)
            outcome.append('#'+word1)
            outcome.append('-'+word1)
            outcome.append('%'+word1)
            outcome.append(word1.replace("o","0"))
            outcome.append(word1.replace("i","1"))
            outcome.append(word1.replace("z","2"))
            outcome.append(word1.replace("s","5"))
            outcome.append(word1.replace("e","3"))
            outcome.append(word1.replace("a","@"))
            outcome.append(word1.replace("g","9"))
            outcome.append(word1.replace("o","0").replace("i","1").replace("z","2").replace("s","$").replace("e","3").replace("a","@").replace("g","9"))

            outcome.append(word1.title().replace("o","0"))
            outcome.append(word1.title().replace("i","1"))
            outcome.append(word1.title().replace("z","2"))
            outcome.append(word1.title().replace("s","$"))
            outcome.append(word1.title().replace("e","3"))
            outcome.append(word1.title().replace("a","@"))
            outcome.append(word1.title().replace("g","9"))
            outcome.append(word1.title().replace("o","0").replace("i","1").replace("z","2").replace("s","$").replace("e","3").replace("a","@").replace("g","9"))
            
        except:
            pass

n=14000000  ## Number of lines of each txt file generated
for i in range(0, len(outcome), n):
    with open(args['output-dir']+"/"+"password_improved_{}.txt".format(int(i/n)), 'w') as f:
            f.write("\n".join(map(str, outcome[i:i + n]
        )))
