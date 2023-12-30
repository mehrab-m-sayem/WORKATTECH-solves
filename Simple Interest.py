# Write your code here
inp = input()
inpf = list(map(float, inp.split()))
p = inpf[0]
r = inpf[1]
t = inpf[2]

i = (p*r*t)/100
print(format(i,".6f")) # .6f means 6 floating points to show
