def ph(num):
 if len(num) == 10 and num.isdigit():
   print "Phone number is valid"
 else:
   print "Invalid phone number"


ip=raw_input('Enter the phone number :  ')
ph(ip)
