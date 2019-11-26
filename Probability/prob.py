import numpy as np
import matplotlib.pyplot as plt; plt.ion()
from scipy import stats

def stat_chars(x):
    print('mean: {:4.2e}'.format(x.mean()))
    print('median: {:4.2e}'.format(np.median(x)))
    print('skewness, {:4.2e}'.format(stats.skew(x)))
    print('kurtosis, {:4.2e}'.format(stats.kurtosis(x, fisher=False)))


def hor_seg(ax, y, xmin, xmax):
    ax.plot([xmin, xmax], [y, y], color='red')

def vert_seg(ax, x, ymin, ymax):
    ax.plot([x, x], [ymin, ymax], color='red')
    
x = np.random.normal(0, 1, int(1e6))

print('******** normal ********')
stat_chars(x)


nbins=100
bins = np.linspace(x.min()-1e-6, x.max()+1e-6, nbins+1)
na = 60
nb = 70

fig, ax = plt.subplots(2,1,sharex=True)
n, bins, patches = ax[0].hist(x, density=True, bins=bins)
for patch in patches[na:nb]:
    patch.set_fc('r')
ax[0].set_ylabel('probability density function')
n, bins, patches = ax[1].hist(x, density=True, cumulative=True, bins=bins)
ax[1].set_ylabel('cumulative distribution function')
ax[1].set_xlabel('value of random variable X')

del x

print('******** chi^2 (df=4) ********')
chi2 = np.random.chisquare(4, int(1e4))
stat_chars(chi2)
print('******** Student\'s t (df=4) ********')
t = np.random.standard_t(4, int(1e4))
stat_chars(t)

fig,ax = plt.subplots(2,1)
ax[0].hist(chi2, density=True, bins=nbins, histtype='step')
ax[0].axvline(x=chi2.mean(), color='red', label="mean")
ax[0].axvline(x=np.median(chi2), color='blue', label="median")
ax[0].legend()
ax[1].hist(t, density=True, bins=nbins, histtype='step')
ax[1].axvline(x=t.mean(), color='red', label='mean')
ax[1].axvline(x=np.median(t), color='blue', label='median')
ax[1].legend()
ax[0].set_title('Chi-squared')
ax[1].set_title('Student\'s t')
for i in range(2):
    ax[i].set_ylabel('pdf')

