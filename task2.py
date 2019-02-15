log=open('access.log','r')
logget=open('get.log','a+')
logput=open('put.log','a+')
logpost=open('post.log','a+')
logdelete=open('delete.log','a+')


def sepratelogs(log):
        for line in log:
                line=line.strip()
                if 'get '.upper() in line.upper():
                        logget.write(line)
                elif 'post '.upper() in line.upper():
                        logpost.write(line)
                elif 'PUT '.upper() in line.upper():
                        logput.write(line)
                elif 'delete '.upper() in line.upper():
                        logdelete.write(line)


def getcommonip(file1,file2):
        file1.seek(0)
        file2.seek(0)
        file1_ip=[]
        common_ip=[]
        for line in file1:
                line.strip()
                temp=line.split(' - - ')
                file1_ip.append(temp[0])
        for line in file2:
                line.strip()
                temp=line.split(' - - ')
                if temp[0] in file1_ip:
                        common_ip.append(temp[0])
       
        return common_ip[:20]

def getcount(file1):
        file1.seek(0)
        count1=0
        count2=0
        count3=0
        for line in file1:
                if 'Chrome'.upper() in line.upper():
                        count1+=1
                elif 'firefox'.upper() in line.upper():
                        count2+=1
                else:
                        count3+=1

        return (count1,count2,count3)


#sepratelogs(log):
#print('The Common IP:::',getcommonip(logget,logpost))

ch,fr,no=getcount(log)
print('The Count of Chrome::',ch)
print('The Count of Firfox::',fr)
print('The Count of None::',no)



