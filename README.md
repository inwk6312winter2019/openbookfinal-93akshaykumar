# Inwk6312- Winter2019 - Final Open Book 

# Programming Task 

Welcome to your final programming quiz

  - You have to clone this repo to your account, you should be seeing this on your account, if someone elses name is listed call an instructor for help.
  - Use the Ubuntu VM / Your PC / Or Python anywhere to write the program.
  - Ensure that you have logged out others from github classroom and github website and you are the only person logged in.
  - Use git add, commit and push to send the code back. 
  - Don't forget to add user name and email on git. 
  - You are allowed to use any form of searching and documentation reading and book reading is promoted
  - Each task is to be saved as a individual python file with the name task0A.py, where A is the sub-tasknumber and 0 is the tasknumber.
  - You cannot talk to your other people or ask for help!


# Task 1A - Basic Functions

### Objectives

The books are Book1.txt, Book2.txt, Book3.txt they are found in your repo.
Open the book in python and write the following functions to perform the following operations on each of the book. Pass the book as a argument to the functions and return the requested data structure / type.
  
1. Function name: unique_words - Returns: A list containing only one copy of the words. (for example, if the word "it" appears 50 times in the book, there should be only one "it" in the tuple)

2. Function name: count_the_article - Returns: An Integer that counts the total number of words that are in the list. => ["a", "the", "at", "run", "to","and","are","or","for","an","this"]

3. Function name: sorted_words - Returns: A list containing the words in the book in descending order based on character count.

4. Function name: character_word_count - Returns: A Dicionary containing words in the book as key and the character count as the values. 

5. Function name: starts_with_vow - Returns: An Integer In each book count the total number of words that start with this following collection tuple =>  ("a", "e", "i", "o", "u").

# Task 1B - Top 20 common words 

### Objectives

Given three books find the top 20 words that are common in all the books. [Ignore spacing and puntuation]
The books are Book1.txt, Book2.txt, Book3.txt.
Return this as a python dict. 


# Task 2 - Log file manipulation. 

You are given a large file "access.log". Use linux commands to explore the file and become familiar with its formatting. 
Write a program in python to do the following:

1. Create 4 different log files each contaning seperated requests for "GET", "POST", "PUT" and "DELETE" from the "access.log" file. Call them get.log, put.log and so on. 

2. List the top 20 most common IP addresses for "GET" requests and "POST" requests. 

3. How many of the requests are from firefox and how many are from chrome? How many are not from either of these?



# Task 3 - APIC-EM API
You are given a code to talk to the APIC-EM sandbox controller in the files, create-ticket.py and get-network-hosts.py through RESI. 
The API-DOCS can be found at https://developer.cisco.com/site/apic-em/docs/api.gsp

### Objectives
Modify get-network-hosts.py to display all the hosts with their names IP Addresses and MAC Addresses. [This should be done on the same file]
Write a new function called getnetworkdevicecount that gets the count of network devices. (The API can be found under Inventory -> network-device -> count)
[Create a newfile called task03.py and import create-ticket.py to achive this]

Use the controller at: https://sandboxapic.cisco.com/

### Max time: 3 hours!

