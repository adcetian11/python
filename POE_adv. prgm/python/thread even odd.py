import threading
def even (n):
    for i in n:
        if i%2==0:
            print(i,"is even")
       
def odd(n):
    for i in n:
        if i%2!=0:
            print(i,"is odd")

list=[2,6,8,11,13]
obj=threading.Thread(target=even,args=(list,))
obj2=threading.Thread(target=odd,args=(list,))
obj.start()
obj2.start()
obj.join()
obj2.join()
