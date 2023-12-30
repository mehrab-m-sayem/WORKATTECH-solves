# Write your code here
inp = input()
inpf = list(map(int,inp.split()))
c = inpf[0]
m = inpf[1]
if c%m==0:
	print("YES")
else:
	print("NO")
