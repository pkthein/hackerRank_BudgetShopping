# BudgetShopping Soln
# All credit goes to UFOScout
# Link: https://github.com/ufoscout/HackerRank_Java/blob/master/src/main/java/ufo/hackerrank/job/numbrs/budget_shopping/Solution.java

n = int(input())
m = int(input())

bQ = []
bC = []

for i in range(m):
	bQ.append(int(input()))

for i in range(m):
	bC.append(int(input()))

tot = 0

# @param n = total budget
# @param bQ = bundle quantities
# @param bC = bundel cost
def budgetShopping(n, bQ, bC):
    global tot
    if n <= 0 or bC == [] or bQ == [] or len(bC) != len(bQ):
        return 0

    calculateRecursive(n, bC, bQ, 0, 0)

    return tot

def calculateRecursive(n, cost, quantity, pos, count):
    global tot
    if n == 0 or pos == len(cost):
        if count > tot:
            tot = count
        return tot

    for i in range(int(n/cost[pos]) + 1):
        calculateRecursive(n - i * cost[pos], cost, quantity, pos + 1, count + i * quantity[pos])
    if count > tot:
        tot = count
    return tot

print(budgetShopping(n, bQ, bC))
