arr = [1, 2, 3]

x = [0, 0, 0]

prex = x[0:]

done = False

def step(i):
    global x, arr, done, prex
    
    if x[-i] + 1 <= arr[-i]:
        x[-i] += 1
    else:
        if i == len(x):
            done = True
            x = prex[0:]
            return
        
        x[-i] = 0
        return step(i + 1)
        
def main():
    global prex, x, done
    
    while done != True:
        step(1)
        prex = x[0:]
        print(prex)

main()