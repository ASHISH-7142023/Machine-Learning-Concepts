import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#days=['mon','tue','wed','thrus','fri','sat','sun']
#week1=[5,6,4,6,1,23,85]
#week2=[89,56,23,74,12,56,19]
#week3=[12,54,78,23,48,53,46]
#df = pd.DataFrame({"Day":days,"Week1":week1,"Week2":week2,"Week3":week3})
plt.figure()
#df.set_index("Day")[["Week1","Week2","Week3"]].plot()
#plt.title("weekly sales(pa)")
#plt.xlabel("Day")
plt.plot(np.arange(5),np.arange(5)**2,market="*")plt.ylabel("Sales")
plt.title("saved figure example")
plt.grid()
plt.savefig("example_plot.png",dpi=150,bbox_inches="tight")
plt.show()
