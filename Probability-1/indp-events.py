'''
tossing a fair die , let A = {2,4,6} B={1,2,3,4}
show P(AB)=P(A).P(B) SINCE 1/2*2/3=1/3 ;=p(A^B={2,4})
'''
trails=10000
myList=[1,2,3,4,5,6]
A=[2,4,6]
B=[1,2,3,4]
AB=[2,4]
import random
count_A=0
count_B=0
count_AB=0
for trail in range(10000):
  choice=random.choice(myList)
  if choice in A:
    count_A+=1
  if choice in B:
    count_B+=1
  if choice in AB:
    count_AB+=1

result=round(count_A*count_B/(trails*trails),2)
print(f"the simulated prob of intersection is {round(count_AB/trails,2)}")
print("the theoretical Probability is 1/3 = 0.33")
print(f"the simulated probability using indp analysis is {result} ")



