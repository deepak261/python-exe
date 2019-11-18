'''
S07Q01

Get the user’s first name and last name. 
        Assume the user provides “Dharmender” and “Singh” as inputs, 
          then print the user’s name in the following order and format

        - Name : dharmender, Surname : singh 
        - DHARMENDER SINGH
          ---------------------  ---------
        - Singh, Dharmender
'''



fname = input("enter the name:")
lname = input("enter the name:")
name = fname+lname
a = len(fname)
b = len(lname)
print('- Name : '+fname.lower()+',','Surname : '+lname.lower())
print('-',fname.upper(),lname.upper())
print(' ',a*'-',b*'-')
print('-',lname.title()+',',fname.title())


 
