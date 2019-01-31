# 0 < r = n - bC * X

n = int(input())
m = int(input())

bQ = []
bC = []

for i in range(m):
	bQ.append(int(input()))

for i in range(m):
	bC.append(int(input()))

X = []
upperX = []

done = False

for i in range(m):
	X.append(0)
	upperX.append(n // bC[i])

bestScore = 0
bestX = X[0:]
preX = X[0:]

def benchMark():
	global X, bQ

	return mxtMult(X, bQ)

def mutateX():
	global X, bC, n, bestScore, bestX, preX

	step(1)
	preX = X[0:]

	r = n - mxtMult(bC, X)
	if r >= 0 and benchMark() > bestScore:
		bestScore = benchMark()
		bestX = X[0:]

# would be naive GA if this was random insertion
# as of now, this is going thru all the possible ans
def step(i):
    global X, upperX, done, preX
    
    if X[-i] + 1 <= upperX[-i]:
        X[-i] += 1
    else:
        if i == len(X):
            done = True
            X = preX[0:]
            
            return
        
        X[-i] = 0
        return step(i + 1)

def mxtMult(A, B):
	tot = 0
	for i in range(len(A)):
		tot += A[i] * B[i]
	return tot

# pretty much main
def simulate():
	global done

	while done != True:
		mutateX()
		if done:
			break

	print(bestScore)
	print(bestX)

simulate()
