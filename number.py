def noname(n):
    x=n%1000
    m=n//1000

    d={2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninty'}
    d2={0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twele',13:'thirteen',14:'forteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
    l=('hundred','thousand','lakh','crore','arab','kharab','padma')
    i=1
    v=str()
    while m!=0:
        h=m%100
        if h<20 and h!=0:
            w=(d2[h])+' '+(l[i])+' '
            v=w+v
        if h>19 and h!=0:
            a=h//10
            b=h%10
            w=(d[a])+' '+(d2[b])+' '+(l[i])+' '
            v=w+v
        m=m//100
        i=i+1
    print(v,end=' ')



    if x>99:
        f=x//100
        x=x%100
        print(d2[f],l[0],sep=' ',end=' ')
    if x<20:
        print(d2[x])
        
    if x>19:
        a=x//10
        b=x%10
        print(d[a],end=' ')
        print(d2[b],end=' ')
        