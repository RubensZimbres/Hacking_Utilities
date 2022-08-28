import argparse
from typing import OrderedDict
from collections import OrderedDict

import pyfiglet
  
result = pyfiglet.figlet_format("PassGen - Interest")
print(result)


parser = argparse.ArgumentParser(description='')
parser.add_argument('--f', dest='file', type=str, default=0, help='Full path of input file')
parser.add_argument('--d', dest='output-dir', type=str, default=0, help='Full path of output directory')
parser.add_argument('--i', dest='interest', type=str, default=0, help='First name of person of interest')
args = vars(parser.parse_args())

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
print('\n')

person=args['interest']

x=0
outcome=[]
with open(args['file'],'r', encoding="latin-1") as f:
    my_list = list(f)
    my_list = [x.rstrip() for x in my_list]
    my_list=my_list[1:2000000] 
    print(colored(255,165,0,"[+] Length of input password dictionary:"),colored(255,165,0,len(my_list)),'\n')
    for word in my_list:
        try:
            x+=1
            if x % 100000 == 0:
                print(x)
            #print(word)
            #print(word[::-1])
            outcome.append(person.lower())
            outcome.append(person.title())
            outcome.append(person.lower()+word.replace("o","0"))
            outcome.append(person.lower()+word.replace("i","1"))
            outcome.append(person.lower()+word.replace("z","2"))
            outcome.append(person.lower()+word.replace("s","$"))
            outcome.append(person.lower()+word.replace("e","3"))
            outcome.append(person.lower()+word.replace("a","@"))
            outcome.append(person.lower()+word.replace("g","9"))
            outcome.append(person.lower()+word.replace("o","0").replace("i","1").replace("z","2").replace("s","$").replace("e","3").replace("a","@").replace("g","9"))

            outcome.append(person.title()+word.replace("o","0"))
            outcome.append(person.title()+word.replace("i","1"))
            outcome.append(person.title()+word.replace("z","2"))
            outcome.append(person.title()+word.replace("s","$"))
            outcome.append(person.title()+word.replace("e","3"))
            outcome.append(person.title()+word.replace("a","@"))
            outcome.append(person.title()+word.replace("g","9"))
            outcome.append(person.title()+word.replace("o","0").replace("i","1").replace("z","2").replace("s","$").replace("e","3").replace("a","@").replace("g","9"))

            outcome.append(person.lower()+word+'+')
            outcome.append(person.lower()+word+'!')
            outcome.append(person.lower()+word+'&')
            outcome.append(person.lower()+word+'#')
            outcome.append(person.lower()+word+'-')
            outcome.append(person.lower()+word+'%')
            outcome.append(person.title()+word)
            outcome.append(person.title()+word+'+')
            outcome.append(person.title()+word+'!')
            outcome.append(person.title()+word+'&')
            outcome.append(person.title()+word+'#')
            outcome.append(person.title()+word+'-')
            outcome.append(person.title()+word+'%')

            
        except:
            pass
print(colored(255,165,0,"[+] Length of enriched password dictionary:"),colored(255,165,0,len(outcome)),'\n')

print(colored(50,80,200,"[+] Saving output . . ."),'\n')

outcome=list(OrderedDict.fromkeys(outcome))

n=14000000  ## Number of lines of each txt file generated
for i in range(0, len(outcome), n):
    with open(args['output-dir']+"/"+"password_improved_{}.txt".format(int(i/n)), 'w') as f:
            f.write("\n".join(map(str, outcome[i:i + n]
        )))

print(colored(0,255,0,"[+] Variance generation for Person of Interest COMPLETED !"),'\n')
