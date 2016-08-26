
az='abcdefghijklmnopqrstuvxwyz'
azlist=[az[i] for i in range(len(az))]	

def nearly_equal(word,check):
# insert word
    longlist=[]
    l1=[]
    lst1=[]
    wordlist=[word[i] for i in range(len(word))]
    for i in azlist:
        for j in range(len(wordlist)+1):
            l1.extend(word)
            l1.insert(j,i)
            tmp=''.join(l1)
            lst1.append(tmp)
            l1=[]
    #print lst1
    longlist.extend(lst1)

# delete word

    l11=[]
    lst2=[]
    #wordlist=[word[i] for i in range(len(word))]
    for i in range(len(wordlist)):
        l11.extend(word)
        del wordlist[i]
        tmp=''.join(wordlist)
        lst2.append(tmp)
        wordlist=l11
        l11=[]
    #print lst2
    longlist.extend(lst2)

    lst3=[]
    d=[]
    #wordlist=[word[i] for i in range(len(word))]
    for j in azlist:
        for i in range(len(wordlist)):
            d.extend(wordlist)
            del d[i]
            d.insert(i,j)
            s=''.join(d)
            lst3.append(s)
            d=[]
    #print lst3
    longlist.extend(lst3)

    lst4=[]
    d1=[]
    #wordlist=[word[i] for i in range(len(word))]
    for i in range(len(wordlist)):
        if i!=len(wordlist)-1:
            d1.extend(wordlist)
            d1[i],d1[i+1]=d1[+1],d1[i]
            s1=''.join(d1)
            lst4.append(s1)
            d1=[]
    #print lst4   
    longlist.extend(lst4)
    #print longlist
    if check in longlist:
      print "True"
    else:
      print "False"





nearly_equal('python','perl')
nearly_equal('perl','pearl')
nearly_equal('python','jython')
nearly_equal('man','woman')




