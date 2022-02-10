from operator import indexOf


heros=['spiderman','superman','batman','wonder','flash']
print(len(heros))
heros.append('blackpanther')
print(heros)
heros.remove('blackpanther')
print(heros)
heros.insert(2,'hulk')
print(heros)
print(indexOf(heros,'hulk'))
print(heros.index('hulk'))
heros.insert(2,'blackpanther')
print(heros)
for hero in heros:
    if hero=="hulk" or 'superman':
        hero='doctor strange'
        break
heros.sort()

max_num=input("Enter max number: ")
try:
    max_num=int(max_num)
except:
    print("Please enter a number")
odd_num=[]
for i in range(max_num):
    if i%2==1:
        odd_num.append(i)
        
print(odd_num)

print(3%2)