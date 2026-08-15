#This is a full sunctional matrix which contains addition,subtraction,
# multiplication,revers, transpose and power Matrix.

matrix=input("enter the no of matrix : ")
if matrix=="1":
    m1 = int(input("Enter rows of first matrix: "))
    n1 = int(input("Enter columns of first matrix: "))
    print("Enter elements of first matrix:")
    A = [[int(input()) for _ in range(n1)] for _ in range(m1)]
    C = [[0 for _ in range(n1)] for _ in range(m1)]
    def sing():
        choice=input("select the option (rev/trp/pow): ")
        if choice=="rev":
            result=[row[::-1]for row in A[::-1]]
            return result
        elif choice=="trp":
            result=[[A[j][i] for i in range(m1)]for j in range(n1)]
            return result
        elif choice=="pow":
            x=int(input("Enter the power: "))
            result=[[A[i][j]**x for j in range(n1)]for i in range(m1)]
            return result
        else:
            print("Invalid!!!!:")
    c=sing()
elif matrix=="2":
    m1 = int(input("Enter rows of first matrix: "))
    n1 = int(input("Enter columns of first matrix: "))
    m2 = int(input("Enter rows of second matrix: "))
    n2 = int(input("Enter columns of second matrix: "))
    if n1 != m2:
        print("Matrix multiplication not possible!")
        exit()
        # Check if multiplication is possible

    # Input first matrix
    print("Enter elements of first matrix:")
    A = [[int(input()) for _ in range(n1)] for _ in range(m1)]

    # Input second matrix
    print("Enter elements of second matrix:")
    B = [[int(input()) for _ in range(n2)] for _ in range(m2)]

    # Initialize result matrix with zeros
    C = [[0 for _ in range(n2)] for _ in range(m1)]

    def sing():
        print("select the oppition (add,sub,mul)")
        choice=input("type: ").lower()
        if choice=="add":
            if m1 != m2 or n1 != n2:
                print("Matrix addition not possible!")
                return None
            result=[[A[i][j]+B[i][j] for j in range (n1) ]for i in range (m1)]
            return result
        elif choice=="sub":
            if m1 != m2 or n1 != n2:
                print("Matrix addition not possible!")
                return None
            result=[[A[i][j]-B[i][j] for j in range (n1) ]for i in range (m1)]
            return result
        elif choice=="mul":
            for i in range(m1):
                for j in range(n2):
                    for k in range(n1):
                        C[i][j] += A[i][k] * B[k][j]
            return C
        else:
            print("invalid !!!!!")
    c=sing()
else:
    print("error!!!!")
# Output result
if c:
    print("Resultant matrix:")
    for row in c:
        print(row)
