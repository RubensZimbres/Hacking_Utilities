# Hacking Utilities  
<hr>
<b>1. Generator of Password Variance</b>  
  
<img src=https://github.com/RubensZimbres/Hacking_Utilities/blob/main/output.png>
  
<b>Description:</b>  
This <b><p style="color:red;">Python3</p></b> file reads a password list from a text file and generates dozens of different samples for each given word, replacing letters by numbers, adding special characters and reverting the password. The idea is to leverage the effectiveness of password crackers by adding vocabulary.  
  
<b>Speed:</b>  
You can generate variance in full ```rockyou.txt``` file in less than 10 minutes in a 32 vCPUs, 120 GB RAM machine in the cloud. Machines with less than 32 GB RAM may freeze with more than 1 million rows. Do it outside Kali Linux. 

This script works with any given password text file.  
  
<b>Usage:</b>  
  
```--f  path of input file.txt (password dictionary)```  
```--d  path of output directory ```

  
```
wget https://raw.githubusercontent.com/RubensZimbres/Hacking_Utilities/main/passvar.py  

python3 passvar.py --f /path_of_input_file/rockyou.txt --d /path_of_directory_output
```  
  
Download of enriched ```rockyou.txt``` (compressed 1.2 GB - 59 files):  

<a href="https://drive.google.com/file/d/1ivEzir7FY3_LcPXwE7rNxEJ9xsFLmmwE/view?usp=sharing">enriched_rockyou.txt</a>
<hr>
<b>About me</b>  
  
I'm a Senior Data Scientist in Brazil, working with Machine Learning, Deep Learning, Natural Language Processing and Computer Vision. I'm interested in ethical hacking, pursuing my PNPT Certification and loving this whole hacking thing.
