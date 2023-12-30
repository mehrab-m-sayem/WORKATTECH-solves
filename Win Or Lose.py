# Write your code here
n  = int(input())
inpf = list(map(int, input().split()))

maxi = 0
for j in range(1,len(inpf)):
	maxi = max(inpf)
if (maxi%2==0):
	print("WON")
else:
	print("LOST")
