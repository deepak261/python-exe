"""

S17Q02

Read passwd file and list all users mentioned in that file in ascending order of their user id. 
Also mention the user’s real name and home directory in the output. 
A sample passwd file is shown below :


"""

def sec(x):
    return int(x[2])



with open ("password.txt") as file:
    FH = file.readlines()
    user = {}
    user_id = []
    
    for i in FH:
        line = i.strip()
        line_1 = line.split(':')
        user_id.append(line_1)
    user_id.sort(key=sec)
    
    for j in user_id:
        lst = ':'+j[2]+':'+j[4]+':'+j[5]+':'+j[6]
        user[j[0]]= lst
    print("user name:user_id:realname:home_directory")
    for i in user:
        print(i,user[i])
        
        
        
    
       
    
