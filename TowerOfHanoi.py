
def display(A,B,C):
    print("A:",A,"B:",B,"C:",C)

def move(A,B,C,source,destination):
    rods ={"A":A,"B":B,"C":C}
    disk = rods[source].pop()
    rods[destination].append(disk)
    display(A,B,C)

def hanoi(n,A,B,C,source,auxiliary,destination):
    if n == 1:
        move(A,B,C,source,destination)
        return
    hanoi(n-1,A,B,C,source,destination,auxiliary)
    move(A,B,C,source,destination)
    hanoi(n-1,A,B,C,auxiliary,source,destination)

A = [4,3,2,1]
B = []
C = []
n = 4

print("STARTING POSITION")
display(A,B,C)

hanoi(n,A,B,C,"A","B","C")

print("FINAL POSITION")
display(A,B,C)
