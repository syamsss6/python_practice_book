import zipfile

def zpfle(name,f1,f2,f3):
 zf=zipfile.ZipFile(name,'w')
 zf.write(f1)
 zf.write(f2)
 zf.write(f3)

ip=raw_input("enter destgination file name with .zip: ")
print "enter 3 files to be added."
ip1=raw_input("enter 1st file to be added: ")
ip2=raw_input("enter 2nd file to be added: ")
ip3=raw_input("enter 3rd file to be added: ")
zpfle(ip,ip1,ip2,ip3)
