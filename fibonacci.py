# @Author: Your name
# @Date:   2020-03-30 15:57:20
# @Last Modified by:   Your name
# @Last Modified time: 2021-04-24 17:25:34
def fibonaci(n):
	a0 = 0
	a1 = 1
	ax = 1
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		for i in range(2,n):
			a0 = a1
			a1 = ax
			ax = a1 + a0
	return ax
dayso = ""
for i in range(20):
	dayso = dayso + f"{fibonaci(i)}, "
print(dayso)
	