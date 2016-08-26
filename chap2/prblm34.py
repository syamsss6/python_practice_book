def sort_word(fle):
    frequency={}
    p=open(fle).read().split()
    for i in p:
        frequency[i]=frequency.get(i,0)+1
 
    for key,value in reversed(sorted(frequency.iteritems(),key= lambda (k,v):(v,k))):
        print "%s:%s" % (key,value) 
 



sort_word('she.txt')
