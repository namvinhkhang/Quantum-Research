import random
import numpy
from matplotlib import pyplot

class Link:
    def __init__(self, val_lambda = 1) -> None:
        self.val = val_lambda
        self.exist = False

if __name__ == "__main__":

    probability = float(input("Enter probability between 0 and 1: "))
    decoherence = float(input("Enter decoherence: "))
    num_of_simulation = int(input("Enter number of simulations in integer: "))
    final_lambda = []
    time, time_p1, time_p2 = [], [], []

    #DOING SIMULATION
    for i in range (num_of_simulation):
        t = 0
        
        #PHASE 1
        l1 = Link()
        l2 = Link()
        while not (l1.exist and l2.exist):
            r1 = random.random()
            r2 = random.random()
            if l1.exist:
                l1.val *= decoherence
            elif r1 <= probability:
                l1.exist = True
            if l2.exist:
                l2.val *= decoherence
            elif r2 <= probability:
                l2.exist = True
            t += 1
        time_p1.append(t)
        
        
        #PHASE 2
        l3 = Link()
        l4 = Link()
        while not (l3.exist or l4.exist):
            r3 = random.random()
            r4 = random.random()
            if l3.exist:
                l3.val *= decoherence
            elif r3 <= probability:
                l3.exist = True
            if l4.exist:
                l4.val *= decoherence
            elif r4 <= probability:
                l4.exist = True
            l1.val *= decoherence
            l2.val *= decoherence
            t += 1
        time_p2.append(t - time_p1[-1])
        
        #CALCULATING THE FINAL LAMBDA
        if l3.exist:
            final_lambda.append(l1.val * l2.val * l3.val)
        else:
            final_lambda.append(l1.val * l2.val * l4.val)
        time.append(t)
        
    #PLOTING
    fig_1 = pyplot.figure(1, figsize=(20,10))
    
    #LAMBDA DISTRIBUTION
    chart_1 = fig_1.add_subplot(221)
    lambda_val, lambda_val_count = numpy.unique(final_lambda, return_counts=True)
    chart_1.plot(lambda_val, lambda_val_count)
    #NAMING
    chart_1.set_title("The distribution of Lambda Parameter")
    chart_1.set_xlabel("Lambda Value")
    chart_1.set_ylabel("Count of Lambda Value")
    
    #TIME DISTRIBUTION
    chart_2 = fig_1.add_subplot(222)
    time_val, time_val_count = numpy.unique(time, return_counts=True)
    chart_2.plot(time_val, time_val_count)
    #NAMING
    chart_2.set_title("The distribution of the Time Until Success")
    chart_2.set_xlabel("Time to complete")
    chart_2.set_ylabel("Count of Completion Time")
    
    #The average lambda parameter, given that we succeed at a given time t
    chart_3 = fig_1.add_subplot(223)
    lambda_at_time_t = {}
    for i, e in enumerate(time):
        lambda_at_time_t[e] = lambda_at_time_t.get(e, []) + [final_lambda[i]]
    lambda_at_time_t = dict(sorted(lambda_at_time_t.items()))
    
    chart_3_time = list(lambda_at_time_t.keys())
    chart_3_avr_lambda = [(sum(lambda_at_time_t[k]) / len(lambda_at_time_t[k])) for k in lambda_at_time_t]
    chart_3.plot(chart_3_time, chart_3_avr_lambda)
    #NAMING
    chart_3.set_title("The average lambda parameter at time t")
    chart_3.set_xlabel("Time to complete")
    chart_3.set_ylabel("Average Lambda Value")
    
    #The distribution of lambda given at time t
    chart_4 = fig_1.add_subplot(224)
    time_values = list(lambda_at_time_t.keys())
    lambda_lists = list(lambda_at_time_t.values())
    chart_4.boxplot(lambda_lists, labels=time_values)
    #NAMING
    chart_4.set_title("Distribution of lambda at time t")
    chart_4.set_xlabel("Time to complete")
    chart_4.set_ylabel("Lambda Value")
    
    pyplot.show()
