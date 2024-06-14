import random 

def objective_function(x,y,z):
    return 1*x + 2*y**2 + 3*z**3 - 36

def fitness(x,y,z):
    ans = objective_function(x,y,z)

    if ans == 0:
        return 99999
    else:
        return abs(1/ans)
    
#Generate Solutions
solutions = []
for s in range(1000):
    solutions.append(((random.uniform(0,1000)),
                     (random.uniform(0,1000)),
                     (random.uniform(0,1000))))


for i in range(10000):
    rankedsolutions = []
    for s in solutions:
        rankedsolutions.append((fitness(s[0],s[1],s[2]),s))
        rankedsolutions.sort()
        rankedsolutions.reverse()

    print(f"===Gen {i} Best Solutions ==")
    print(rankedsolutions[0])

    if rankedsolutions[0][0] > 9999:
        break

    bestsolutions = rankedsolutions[:100]

    elements = []
    for s in bestsolutions:
        for j in range(3):
            elements.append(s[1][j])


    New_Generation = []
    for _ in range(1000):
        e1 = random.choice(elements) * (random.uniform(0.99,1.01))
        e2 = random.choice(elements) * (random.uniform(0.99,1.01))
        e3 = random.choice(elements) * (random.uniform(0.99,1.01))


        New_Generation.append((e1,e2,e3))
    solutions = New_Generation