# Write your code here
# Write your code here
inp = input()
inpf = list(map(int,inp.split()))
r = inpf[0]
h = inpf[1]
v = 3.14*(r**2)*h
a = v/1000
p = a*40
print(format(p, '.2f'))
