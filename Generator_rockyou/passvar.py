import argparse
import sys
from collections import OrderedDict

import pyfiglet
  
result = pyfiglet.figlet_format("Password Generator")
print(result)

parser = argparse.ArgumentParser(description='')
parser.add_argument('--f', dest='file', type=str, default=0, help='Path of input file')
parser.add_argument('--d', dest='output-dir', type=str, default=0, help='Path of output directory')
args = vars(parser.parse_args())

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
print('\n')
x=0
outcome=[]
try:
    with open(args['file'],'r', encoding="latin-1") as f:
        my_list = list(f)
        my_list = [x.rstrip() for x in my_list] 
        print(colored(255,165,0,"[+] Length of input password dictionary:"),colored(255,165,0,len(my_list)),'\n')
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

                word1 = word[::-1]     #### REVERSE WORD
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
except:
    print(colored(255,0,0,"[X]  Run the command using: python3 passvar.py . . . "))
    print("\n")
    sys.exit(1)


print(colored(255,165,0,"[+] Length of enriched password dictionary:"),colored(255,165,0,len(outcome)),'\n')

outcome=list(OrderedDict.fromkeys(outcome)) ## REMOVE DUPLICATES


print(colored(255,165,0,"[+] Saving output . . ."),'\n')


n=14000000  ## Number of lines of each txt file generated
for i in range(0, len(outcome), n):
    with open(args['output-dir']+"/"+"password_improved_{}.txt".format(int(i/n)), 'w') as f:
            f.write("\n".join(map(str, outcome[i:i + n]
        )))

print(colored(0,255,0,"[*] Variance generation COMPLETED !"),'\n')
