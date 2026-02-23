#binomial example(n,p)
n,p=10,0.4
k=np.arange(0,n+1)
pmf_binom=stats.binom.pmf(k,n,p)

print('binomial theoritical mean,var:' ,stats.binom.mean(n,p),stats.binom.var(n,p))

#poisson example
lam=3.0
k_p=np.arange(0,15)
pmf_plots=stats.piosson.pmf(k_p,lam)
print('poisson theoritical mean,var:', stats.poisson.var(lam))

#plot PMFs
fig,ax=plt.subplots(1,2,figsize=(10,4))
ax[0].stem(k,pmf_binom)
ax[0].set_title('binomial pmfs(n=10,p=0.4)')
ax[0].stem(k,pmf_pois)
ax[0].set_title('position pmfs(lambda=0.3)')
plt.tight_layout()
plt.show()
