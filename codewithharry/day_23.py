# list method in py 23 day

l = [89,54,25,1,2,1,3,4,6]
print(l)
l.append(9)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
print(l.index(1))
print(l)
print(l.count(1))
print(l)
m = l.copy()
m[0] = 0
print(l)
l.insert(1,6969)
print(l)

m =[900,1000,1500]
l.extend(m)
print(l)