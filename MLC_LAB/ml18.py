import numpy as np
rolls=np.random.randint(1,7,1000)
freq={i: np.sum(rolls == i)for i in range(1,7)}

print("dice frequencies : ",freq)