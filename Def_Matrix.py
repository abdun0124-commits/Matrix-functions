def input_matrix():
    print("enter the no.of matrix ('1','2'):")
    op=int(input("enter your choice: "))
    if op==1:
        r=int(input("enter the no. of rows: "))
        cl=int(input("enter the no. of columns: "))
        print("enter the elements of a matrix:")
        a = [[int(input()) for _ in range(cl)] for _ in range(r)]
        return a,r,cl
    elif op==2:
        r=int(input("enter the no. of rows: "))
        cl=int(input("enter the no. of columns: "))
        r2=int(input("enter the no. of rows: "))
        cl2=int(input("enter the no. of columns: "))
        print("enter the elements of a matrix:")
        a = [[int(input()) for _ in range(cl)] for _ in range(r)]
        print("enter the elements of b matrix:")
        b = [[int(input()) for _ in range(cl2)] for _ in range(r2)]
        return a,b,r,cl,cl2,r2
    else:
        print("Invalid choice:")

def add_matrix(input_matrix):
    a,b,r,cl=input_matrix()
    c=[]
    for i in range(r):
        row=[]
        for j in range(cl):
            result=a[i][j]+b[i][j]
            row.append(result)
        c.append(row)
    for row in c:
        print(row)
    return c

def mul_matrix(input_matrix):
    
    a,b,r,cl,cl2=input_matrix()
    c = [[0 for _ in range(cl)] for _ in range(r)]
    for i in range(r):
        row=[]
        for j in range(cl):
            for k in range(cl2):
                c[i][j]+=a[i][k]*b[k][j]
    for row in c:
        print(row)
               
    return c

def sub_matrix(input_matrix):
    a,b,r,cl=input_matrix()
    c=[]
    for i in range(r):
        row=[]
        for j in range(cl):
            result=a[i][j]-b[i][j]
            row.append(result)
        c.append(row)
    for row in c:
        print(row)
    return c    

def square_matrix(input_matrix):
    a,r,cl=input_matrix()
    c = [[0 for _ in range(cl)] for _ in range(r)]
    for i in range(r):
        for j in range(cl):
            for k in range(cl):
                c[i][j]+=a[i][k]*a[k][j]
    for  row in c:
        print(row)
    return c


print("1.Addition||2.Multiplication||3.Subtraction||4.Square")
o=int(input("Enter the option: "))
if o==1:
    add_matrix(input_matrix)
elif o==2:
    mul_matrix(input_matrix)
elif o==3:
    sub_matrix(input_matrix)
elif o==4:
    square_matrix(input_matrix)
