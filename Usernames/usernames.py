import argparse
from typing import OrderedDict
from collections import OrderedDict
import numpy as np

import pyfiglet
  
result = pyfiglet.figlet_format("U - Gen")
print(result)

parser = argparse.ArgumentParser(description='')
parser.add_argument('--o', dest='output-dir', type=str, default=0, help='Full path of output directory')
parser.add_argument('--n', dest='name', type=str, default=0, help='First name of person of interest')
parser.add_argument('--s', dest='surname', type=str, default=0, help='Surname of person of interest')
parser.add_argument('--d', dest='domain', type=str, default=0, help='Business domain')
args = vars(parser.parse_args())

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
print('\n')

name=args['name'].lower()
surname=args['surname'].lower()
domain=args["domain"]

#name="sarah"
#surname="connor"
#domain="www.intel.com"

output=[]
output.append(name)
output.append(surname)
output.append(name+'.'+surname)
output.append(name[0]+'.'+surname)
output.append(name[0]+surname)
output.append(name+surname[0])
output.append(name+'.'+surname[0])

#print(colored(255,165,0,"[+] Length of input password dictionary:"),colored(255,165,0,len(my_list)),'\n')

year="""00,01,02,03,04,05,  06,  07,  08,  09, 10, 11, 12, 13, 14, 15, 16,17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98"""

lista=year.replace(" ","").split(',')

for i in range(0,len(output)):
    for j in lista:
        output.append(output[i]+j+'@'+domain[4:])

output

print(colored(255,165,0,"[+] Length of usernames generated:"),colored(255,165,0,len(output)),'\n')

print(colored(50,80,200,"[+] Saving output . . ."),'\n')

with open(args['output-dir']+"/"+"username_generated_{}.txt".format(name+surname), 'w') as f:
    for line in output[7:]:
        f.write("%s\n" % line)

print(colored(0,255,0,"[+] Username generation for Person of Interest COMPLETED !"),'\n')
