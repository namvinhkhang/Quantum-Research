from matplotlib import pyplot
import random

class Link:
    def __init__(self) -> None:
        self.val = 1
        self.exist = False
    
if __name__ == "__main__":
    final_lambda = []
    time = []
    for i in range (1000):
        t = 0
        l1 = Link()
        l2 = Link()
        while not l1.exist and l2.exist:
            r1 = random.randint(0,100)
            r2 = random.randint(0,100)
            if l1.exist:
                l1.val *= 0.98
            elif r1 >= 50:
                l1.exist = True
            if l2.exist:
                l2.val *= 0.98
            elif r2 >= 50:
                l2.exist = True
            t += 1
        
        l3 = Link()
        l4 = Link()
        while not (l3.exist or l4.exist):
            r3 = random.randint(0,100)
            r4 = random.randint(0,100)
            if l3.exist:
                l3.val *= 0.98
            elif r3 >= 50:
                l3.exist = True
            if l4.exist:
                l4.val *= 0.98
            elif r4 >= 50:
                l4.exist = True
            l1.val *= 0.98
            l2.val *= 0.98
            t += 1
        
        if l3.exist:
            final_lambda.append(l1.val * l2.val * l3.val)
        else:
            final_lambda.append(l1.val * l2.val * l4.val)
        time.append(t)
    pyplot.scatter(time, final_lambda)
    pyplot.show()