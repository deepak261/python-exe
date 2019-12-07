def file(x):
    with open(x) as fl:
        FH = fl.readlines()
        return FH

def supper_market():
    a = "bill.txt"
    b = "items.txt"
    f = file(a)
    item = file(b)
    bill = {}
    grad_total = 0
    for i in f[4:20]:
        c = i.strip()
        line = c.split(':')
        line_1 = line[1].split()
        line_2 = line[0].split('.')
        line_3 = line_2[1].split()
        bill[line_3[0]] = line_1[0]
        grad_total = grad_total + int(line_1[0])
    for i in item:
        i = i.strip()
        if i in bill:
            del bill[i]
    bill_total = 0
    count = 1
    print("# Your Super Market Itemised Bill")
    print("="*25)
    print("Sl. Item      :  Amount")
    print("="*25)
    for i,j in bill.items():
        string = i.center(12)
        just = str(count)+'  '+i
        center = ':'
        nu = str(count)+'.'
        bill_total = bill_total+int(j)
        if len(just) != 16 and len(nu) != 4:
            ln = 12 - len(just)
            ln = ' '*ln
            numl = 4 - len(nu)
            numl = ' ' * numl
            total = nu+numl+i+ln
            if len(total) != 16:
                tl = 14 - len(total)
                tl = (tl*' ')
                print(total+tl+':'+j.rjust(8))
        count += 1
    saved_rs = grad_total - bill_total
    print()
    print("="*25)
    print("TOTAL         :   ",bill_total)
    print("="*25)
    print("** Saved Rs.",str(saved_rs)+'.00/- **')
    print("# All amounts include GST")
    print("# Please visit again")

            
#main starts from here
supper_market()
