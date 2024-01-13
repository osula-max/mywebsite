
from numpy import random
import simpy 
import pandas

for r in range(11):
    x = random.randint(100,200)
    x1 = random.randint(1,100)
    
    
costprice = 100

data = []

def example(env, data):    
    while True:
        x = random.randint(100,200)
        costprice = 100
        yield env.timeout(1)
        sellingprice = x
        data.append('profit: %.2f' % (sellingprice - costprice))
       


def example1(env,data):
    while True:
        x1 = random.randint(1,100)
        costprice = 100
        yield env.timeout(1)
        sellingprice = x1
        data.append('loss: %.2f' % (costprice - sellingprice))
        


env = simpy.Environment()
proc = env.process(example(env, data))
proc = env.process(example1(env, data))

env.run(until=11)

df = pandas.DataFrame(data)

print(df)



while True:
    pass




