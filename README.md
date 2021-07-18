# Hacking Utilities  
<hr>    
# 1.Generator of Password Variance  
  
<img src=https://github.com/RubensZimbres/Hacking_Utilities/blob/main/screen.png>
  
<b>Description:</b>  
This <b>Python3</b> file enhances vocabulary for password crackers. It reads a password list from a text file and generates dozens of different samples for each given word, replacing letters by numbers, adding special characters and reversing the password. The idea is to leverage the effectiveness of password crackers by adding diverse vocabulary.  
  
<b>Speed:</b>  
You can generate variance in full ```rockyou.txt``` file in less than 10 minutes in a 32 vCPUs, 120 GB RAM machine in the cloud. Machines with less than 32 GB RAM may freeze with more than 1 million rows. Do it outside Kali Linux. 

This script works with any given password text file.  
  
<b>Usage:</b>  
  
```--f  path of input file.txt (password dictionary)```  
```--d  path of output directory ```

  
```
wget https://raw.githubusercontent.com/RubensZimbres/Hacking_Utilities/main/Generator_rockyou/passvar.py  

mkdir passwords

python3 passvar.py --f /path_of_input_file/rockyou.txt --d ./passwords
```  
  
Download of enriched ```rockyou.txt``` (compressed 1.2 GB - 59 files):  

<a href="https://drive.google.com/file/d/1ivEzir7FY3_LcPXwE7rNxEJ9xsFLmmwE/view?usp=sharing">enriched_rockyou.txt</a>  
  
<img src=https://github.com/RubensZimbres/Hacking_Utilities/blob/main/rockyou.png>  
  
# 2.OSINT Tools
  
This piece of Python code calls Google Cloud Vision API and returns text in images/pictures, web pages that refer o that image, labels (objects) and landmarks, sometimes including geolocation. Get your new Google Cloud account, 300 USD in credits and activate the Vision API.  
  
<hr>  
  
# 3.Password Generator for People of interest  
  
<b>Description:</b>  
This <b>Python3</b> file enhances vocabulary for password crackers, including the person of interest name in the rockyou.txt password list.  
  
<b>Speed:</b>  
You can generate variance in 2,000,000 words of ```rockyou.txt``` file in less than 2 minutes. Can be used inside Kali Linux. 

This script works with any given password text file.  
  
<b>Usage:</b>  
  
```--f  path of input file.txt (password dictionary)```  
```--d  path of output directory ```  
```--i  first name of person of interest ```  

  
```
wget https://raw.githubusercontent.com/RubensZimbres/Hacking_Utilities/main/Person_of_interest/passvar_person.py  

mkdir passwords

python3 passvar_person.py --f /path_of_input_file/rockyou.txt --d ./passwords --i Anna
```  
<hr>  
<b>About me</b>    
   
I'm a Senior Data Scientist in Brazil, working with Machine Learning, Deep Learning, Natural Language Processing and Computer Vision. I'm interested in ethical hacking, pursuing my PNPT Certification and loving this whole hacking thing.
