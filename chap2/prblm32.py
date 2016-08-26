


az='abcdefghijklmnopqrstuvxwyz'
azlist=[az[i] for i in range(len(az))]


def mutate(word):
    
    print "----Insert----",'\n'
    insertword(word)
    print "----Delete----",'\n'
    deleteword(word)
    print "----Replece----",'\n'
    replaceword(word)
    print "----Swap----",'\n'
    swapword(word)


def insertword(word):
    
    l1=[]
    l2=[]
    wordlist=[word[i] for i in range(len(word))]
    for i in azlist:
        for j in range(len(wordlist)+1):
            l1.extend(word)
            l1.insert(j,i)
            tmp=''.join(l1)
            l2.append(tmp)
            l1=[]
    print l2        

def deleteword(word):
    
    l1=[]
    l2=[]
    wordlist=[word[i] for i in range(len(word))]
    for i in range(len(wordlist)):
        l1.extend(word)
        del wordlist[i]
        tmp=''.join(wordlist)
  	l2.append(tmp)
  	wordlist=l1
  	l1=[]
    print l2

def replaceword(word):
    
    l1=[]
    d=[]
    wordlist=[word[i] for i in range(len(word))]
    for j in azlist:
        for i in range(len(wordlist)):
            d.extend(wordlist)
 	    del d[i]
            d.insert(i,j)
	    s=''.join(d)
 	    l1.append(s)
	    d=[]
    print l1

def swapword(word):
    
    lst=[]
    d=[]
    wordlist=[word[i] for i in range(len(word))]
    for i in range(len(wordlist)):
        if i!=len(wordlist)-1:
            d.extend(wordlist)
	    d[i],d[i+1]=d[+1],d[i]
	    s=''.join(d)
 	    lst.append(s)
  	    d=[]
    

    print lst   


mutate('hello')
