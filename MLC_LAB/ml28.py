import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#x=np.arange(-5,6) #-5 to 5
x=np.linspace(0,2*np.pi,200)
y=x**2
s=np.sin(x)
c=np.cos(x)
plt.figure()
#plt.plot(x,y) #default line
#plt.plot(x, y, marker="*", linestyle=":")
plt.plot(x, s, label="sin(x)")
plt.plot(x, c, label="cos(x)")
plt.xlabel("x (radians)")
plt.ylabel("value")
#plt.xlabel("x")
#plt.ylabel("y = x^2")
#plt.title("basic line plot")
#plt.title("markers and line style")
plt.title("multiple lines with legend")
plt.grid(True)
plt.legend()
plt.show()
