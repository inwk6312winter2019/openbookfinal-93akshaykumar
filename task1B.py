import operator
import string

def depunctuate(line):
	for repl in string.punctuation:
		line=line.replace(repl,"")
	return line






def book_dic(book):
    book_dic={}
    unique_word=[]
    for item in book:
        item.seek(0)
        #print(1)
        for line in item:
            #print(2)
            line=line.strip()
            ine=depunctuate(line)
            line=line.split()
            for word in line:
                #print(3)
                book_dic[word]=book_dic.get(word,0)+1
    sorted_dic = sorted(book_dic.items(), key=operator.itemgetter(1),reverse=True)
    for i in range(20):
        unique_word.append(sorted_dic[i][0])
        
    return unique_word
        

book1=open("Book1.txt",'r')
book2=open("Book1.txt",'r')
book3=open("Book1.txt",'r')
book_list=(book1,book2,book3)
unique_list=book_dic(book_list)
print("The List of 20 common words words in Three books::",unique_list)


