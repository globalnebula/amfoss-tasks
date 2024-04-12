# Bandit
## Level 1
I used this for connecting to bandit using ssh
```ssh bandit0@bandit.labs.overthewire.org -p 2220```  
I gave the password bandit0  
Then used ```ls```,which showed a readme file  
```cat readme```  
used this for reading the text inside it.  
password : NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL  

## Level 2
Used the same ssh but changed the bandit0 to bandit1,for every level.  
used ```cat ./-``` for reading the "-" file.  
password : rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi

## Level 3
used ```cat spaces\ in\ this\ filename``` after using ```ls```  
password : aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG  
[Found out that i can use ```exit``` command instead of closing the terminal everytime to get out of the bandit server]  

## Level 4
Used ``ls``  
then used ``cd inhere`` to go into that directory  
used ``ls`` again to check if that directory has any files.  
Turned out it contains a hidden file.  
used ``ls -a``  
found a file named .hidden  
used ``cat .hidden``  
password : 2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe  

## Level 5
used ``ls``  
``cd inhere``  
used ``ls`` inside ``inhere`` directory  
There existed 10 files inside it  
used cat ./-file0x for every file  
9 of them are not readable,the 8th file named file07 is of ASCII text which contained the password   
password : lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR

## Level 6
``ls``  
``cd inhere``  
used ``ls`` inside ``inhere`` directory  
we get 20 directories,checking all of them would obviously be a stupid thing to do.  
they gave few hints like it is of 1033 bytes in size and human readable,not executable  
googled about it and found the appropriate command for searching the desired file is  
``find -size 1033c``  
So filtering out the files which are not of 1033 bytes in size,we are left only with one file,which is the file2 inside maybehere07  
using ``cat`` we can read the text inside it,which is out password.  
password : P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU

## Level 7
used ``ls`` first but didn't find any files or directories  
So went to root directory using ``cd /`` command  
Using the hints given in the question  
used ``find -user bandit7 -group bandit6 -size 33c`` this command for finding a file which owned by bandit7 user and bandit 6 group,which is of 33 bytes in size.  
we get a list of "Permission denied" errors except for one line which shows like  
``./var/lib/dpkg/info/bandit7.password``  
I used ``cat ./var/lib/dpkg/info/bandit7.password`` to get the password.  
password : z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S

## Level 8
used ``ls`` command as usual  
saw that there exists a data.txt file and tried to open it using ``cat data.txt``  
resulted in crash of terminal since there was so much data in it for it to display in the terminal  
used ``ctrl+c`` to stop the process and read the question again.Read about grep a bit and then tried  
``cat data.txt | grep "millionth"``  
grep finds patterns in text files,now in this case the pattern is "millionth".It prints the entire line which has that word.  
``|`` This is called a pipe,which allows us to combine multiple commands.  
password : TESKZC0XvTetK0S9xNwm25STk5iWrBvP

## Level 9
used ``ls``  
according to the instructions given,I used  
``sort data.txt | uniq -u`` which sorts data and filters the duplicate files and prints only the line which is unique  
password : EN632PlfYiZbn3PhVK3XOGSlNInNE00t

## Level 10
used ``ls``
again same data.txt  
obviously should use the same grep command since we have to print all the lines which are preceded by several equals to symbols  
used ``strings data.txt | grep "======"`` to print all the lines preceded by equals to symbols  
resulted in  
``========== the
========== password
========== is=
F========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s``  
so,the password : G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
