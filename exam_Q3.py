def file(x):
    with open(x) as fl:
        FH = fl.read()
        return FH



def Oliver_Twist():
    a = "oliver Twist.txt"
    lst = ['H','Y','W','T','h','y','w','t']
    fh = file(a)
    fh = fh.split()
    data = []
    data_1 = {}
    data_2 = {}
    print("The top most frequently occuring words in the book :")
    for i in fh:
        strp = i.strip(',')
        strp_1 = strp.strip('.')
        strp_2 = strp_1.strip("'")
        data.append(strp_2.strip())
    
    for i in data:
        if i not in data_1:
            data_1[i] = data.count(i)
    for i in sorted(data_1,key = data_1.get,reverse = 1):
        data_2[i] = data_1[i]
    c = 0
    
    for i,j in data_2.items():
        k = i[0]
        if c != 50: 
            if len(i) > 4 and k not in lst :
                c += 1
                print(str(c)+'.',i,data_2[i])

        else:
            break 


#main starts from here
Oliver_Twist()
