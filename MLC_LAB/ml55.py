# training data

import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.ensemble import RandomForestClassifier


X=np.array([[1,2],        #0 
            [2,3],        #0
            [3,3],        #0   
            [6,5],        #1
            [7,7],        #1
            [8,6]         #1
            ])
y = np.array([0,0,0,1,1,1])

# taining knn model

k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X,y)

# predict class of a new sample

sample = np.array([[3,5]])
predicted_class = knn.predict(sample)[0]
print("predicted class for [3,5] : ",predicted_class)


#create version

step=0.1

#determine the x-range(min to max of feature 1)

x_min = X[:,0].min()-1
x_max = X[:,0].max()-1

#determine the y-range(min to max of feature 2)

y_min = X[:,0].min()-1
y_max = X[:,0].max()-1

#create evenly spaced x- and y-values within the above

xs = np.arange(x_min,x_max,step)
ys = np.arange(y_min,y_max,step)

#create a meshgrid from xs and ys

xx , yy = np.meshgrid(xs,ys)

#convert xx,yy into a long list of 20points

grid_points = np.c_[xx.ravel(),yy.ravel()]

#predict class label (0 or 1) for every grid point

Z = knn.predict(grid_points)


#reshape prdictions back ibnto grid shape

Z = Z.reshape(xx.shape)


# 5. plot the graph

plt.figure(figsize=(6,5))

#draw the bg decision regions
plt.contourf(
    xx,
    yy,
    Z,
    alpha = 0.3,
    cmap = plt.cm.Paired
    
)

# plot the original training points

plt.scatter(X[:,0],X[:,1],
            c=y,
            s=80,edgecolor='k',
            cmap=plt.cm.Paired)

#plot the new sample point as star marker

plt.scatter(sample[0,0],sample[0,1],
            c='red',
            s = 128,
            marker='*',
            edgecolor='black')

#add plot labels and title

plt.title(f"KNN Decision Boundary(k = {k})")
plt.xlabel("feature 1")
plt.ylabel("feature 2")

#add light grid lines

plt.grid(True,linestyle = '--',alpha = 0.4)

plt.show()


#step-1 - define trainig data

X = np.array([[1,2],[2,3],[3,3],[6,5],[7,7],[8,6]])
y = np.array([0,0,0,1,1,1])

#step- 2 - train decision tree and random forest

dt = DecisionTreeClassifier(max_depth=3,random_state=0)
rf = RandomForestClassifier(n_estimators=5,random_state=0)

df.fit()
rf.fit()

#step - 3 - compare feature importance and accuracy

print("decision tree acurracy : ",dt.score(X,y))
print("random forest acurracy : ",rf.score(X,y))
print("random forest feature importance : ",rf.feature_importances_)

#step -4 - decision boundary plot fn

def plot_decision_boundary(model,X,y,title):
    h=0.1
    x_min,x_max = X[:,0].min()-1,X[:,0].max()+1
    y_min,y_max = X[:,0].min()-1,X[:,0].max()+1
    xx,yy = np.meshgrid(np.arange(x_min,x_max,h),
                        np.arange(y_min,y_max,h))
    Z = model.predict(np.c_[xx.ravel(),y.ravel()])
    Z = Z.reshape(xx.shape)
    
    plt.contourf(xx,yyxZ,alpha=0.3)
    plt.scatter(X[;,0],X[:,1],c=y,edgecolors='k',s=80)
    plt.title(title)
    plt.xlabel("feature 1")
    plt.ylabel("feature 2")
    
#step - 5 - plot decision boundaries
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plot_decision_boundary(dt,X,y,"decicsion tree ")

plt.subplot(1,2,2)
plot_decision_boundary(rf,X,y,"random forest decision")
plt.tight_layout()
plt.show()


