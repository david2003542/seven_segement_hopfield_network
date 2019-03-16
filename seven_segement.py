#for the submission uncomment the submission statements
#see submission.README

from math import *
import numpy as np
from submission import *

def initMatrix(vec):
    x_len = len(vec)
    w = np.zeros([x_len,x_len])
    for i in range(x_len):
        for j in range(x_len):
            if i == j:
                w[i,j] = 0
            else:
                w[i,j] = vec[i]*vec[j]
    return w

def energy(vec, total_weights):
    x_len = len(vec)
    Energy = 0
    for i in range(x_len):
       for j in range(x_len):
           Energy -= ((vec[i]*total_weights[i][j]*vec[j])/2.0)
    print('energy')
    print(Energy)
    return Energy

def update(test,Weight):
    result = []
    N = len(test)
    for i in range(N):
        m=0
        for j in range(N):
            m += Weight[i][j]*test[j]
        if m > 0:
            result.append(1)
        else:
            result.append(-1)
    # print(result)
    return result

def seven_segment(pattern):

    def to_bool(a):
        if a==1:
            return True
        return False
    

    def hor(d):
        if d:
            print(" _ ")
        else:
            print("   ")
    
    def vert(d1,d2,d3):
        word=""

        if d1:
            word="|"
        else:
            word=" "
        
        if d3:
            word+="_"
        else:
            word+=" "
        
        if d2:
            word+="|"
        else:
            word+=" "
        
        print(word)

    

    pattern_b=map(to_bool,pattern)
    print(pattern_b)

    hor(pattern_b[0])
    vert(pattern_b[1],pattern_b[2],pattern_b[3])
    vert(pattern_b[4],pattern_b[5],pattern_b[6])

    number=0
    for i in range(0,4):
        print(pattern_b[7+i])
        print(pow(2,i))
        if pattern_b[7+i]:
            number+=pow(2,i)
    print(int(number))
        
submission=Submission("Chen Ting Hung")
submission.header("Chen Ting Hung")

six=[1,1,-1,1,1,1,1,-1,1,1,-1]
three=[1,-1,1,1,-1,1,1,1,1,-1,-1]
one=[-1,-1,1,-1,-1,1,-1,1,-1,-1,-1]
test1=[1,-1,1,1,-1,1,1,-1,-1,-1,-1]
test2=[1,1,1,1,1,1,1,-1,-1,-1,-1]

total_weights = (initMatrix(one) + initMatrix(three) + initMatrix(six)) / 3.0

print("Energy pattern")
energy(one, total_weights)
energy(three, total_weights)
energy(six, total_weights)


##this assumes you have called your weight matrix "weight_matrix"
submission.section("weight matrix")
submission.matrix_print("W",total_weights)

print("test1")
submission.section("Test 1")
init_energy=energy(test1, total_weights)
submission.seven_segment(test1)
submission.qquad()
submission.print_number(init_energy)
old_energy = 0 
while(True):
    test1=update(test1, total_weights)
    updated_energy=energy(test1, total_weights)
    seven_segment(test1)
    
    if old_energy!=updated_energy:
        submission.seven_segment(test1)
        submission.qquad()
        submission.print_number(updated_energy)
        old_energy = updated_energy
    else:
        break




print("test2")
submission.section("Test 2")
init_energy=energy(test2, total_weights)
submission.seven_segment(test2)
submission.qquad()
submission.print_number(init_energy)
old_energy = 0 
while(True):
    test2=update(test2, total_weights)
    updated_energy=energy(test2, total_weights)
    seven_segment(test2)
    
    if not old_energy== updated_energy:
        submission.seven_segment(test2)
        submission.qquad()
        submission.print_number(updated_energy)
        old_energy = updated_energy
    else:
        break



submission.bottomer()