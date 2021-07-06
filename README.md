# Hacking Utilities  

<b>Generator of Password Variance</b>  
  
<img src=https://github.com/RubensZimbres/Hacking_Utilities/blob/main/enhance.png>
  
Description:  
This Python (3) file reads a password list from a text file and generates dozens of different samples for each given word, replacing letters by numbers, adding special characters and reverting the password. The idea is to leverage the effectiveness of password crackers.  
  
Speed:  
You can generate variance in full ```rockyou.txt``` file in less than 10 minutes. This script also works with any given password text file.  
  
Usage:  
  
```--f```  path of input file.txt (password dictionary)  
```--d```  path of output directory 

  
```
wget https://raw.githubusercontent.com/RubensZimbres/Hacking_Utilities/main/passvar.py  

python passvar.py --f /path_of_input_file/rockyou.txt --d /path_of_directory_output
```  
  
Download of enriched rockyou.txt compressed (1.2 GB):  

https://drive.google.com/file/d/1ivEzir7FY3_LcPXwE7rNxEJ9xsFLmmwE/view?usp=sharing
