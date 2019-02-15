import operator
import string

def depunctuate(line):
	for repl in string.punctuation:
		line=line.replace(repl,"")
	return line


def unique_words(book):
    unique_list=[]
    for item in book:
        #print(1)
        for line in item:
            #print(2)
            line=line.strip()
            line=depunctuate(line) 
            line=line.split()
            for word in line:
                #print(3)
                unique_list.append(word)
    unique_list=set(unique_list)
    return tuple(unique_list)


def sorted_words(book_dic):
    
    #sorted_dic = sorted(book_dic.items(), key=operator.itemgetter(1),reverse=True)
    #for item in sorted_dic
    return list(sorted(book_dic,reverse=True))


def character_word_count(book):
    book_dic={}
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
                book_dic[word]=len(word)

    return book_dic

def count_the_article(unique_list,check_list):
    count=0
    for item in check_list:
        if item in unique_list:
            count+=1

    return count


def starts_with_vow(book,vow=("a", "e", "i", "o", "u")):
    book.seek(0)
    count=0
    for line in book:
        line=line.strip()
        ine=depunctuate(line)
        line=line.split()
        for word in line:
            word=word.strip("'")
            if word[0].lower() in vow:
                count+=0

    return count

book1=open("Book1.txt",'r')
book2=open("Book1.txt",'r')
book3=open("Book1.txt",'r')
book_list=(book1,book2,book3)
unique_list=unique_words(book_list)
print("The List of unique words in Three books::",unique_list)
print("The count of list variables in books::",count_the_article(unique_list,["a", "the", "at", "run", "to","and","are","or","for","an","this"]))
book_dic=character_word_count(book_list)
print("list containing the words in the book in descending order based on character count.",sorted_words(book_dic))
print(" A Dicionary containing words in the book as key and the character count as the values. :::",character_word_count(book_list))
print('An Integer In each book count the total number of words that start with this following collection tuple =>  ("a", "e", "i", "o", "u").',starts_with_vow(book1),starts_with_vow(book2),starts_with_vow(book3))



