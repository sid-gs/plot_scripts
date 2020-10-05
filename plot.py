import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
from scipy.interpolate import interp1d as intp1
from scipy.interpolate import make_interp_spline as intp2
from scipy.ndimage.filters import gaussian_filter1d as gf1
from matplotlib.pyplot import figure
import matplotlib.ticker

#USER_PARAMETERS

#Size and aspect ratio----
ratio = 0.8
size = 5
#Font sizes ----
label_fs = 15
tic_fs = 15
legend_fs = 15
#Save to ----
file_name = "sc_plot.png"


#MAKE LATEX READY
fig = plt.figure(figsize = [size,size*ratio], tight_layout = {'pad': 0.5}) 
rc('font',**{'family':'serif','serif':['Computer Modern']})
rc('text', usetex=True)

#LOAD FILES HERE
hd = '../kh/'
fni = np.loadtxt(hd+'fni.his');
fna = np.loadtxt(hd+'fna.his');
fxi = np.loadtxt(hd+'fxi.his');
fxa = np.loadtxt(hd+'fxa.his');

rni = np.loadtxt(hd+'rni.his');
rna = np.loadtxt(hd+'rna.his');
rxi = np.loadtxt(hd+'rxi.his');
rxa = np.loadtxt(hd+'rxa.his');

#NORMALIZE DATA HERE
yfac  = 252.0*253.0*126.0
xfac  = 1.0/(252.0*252.0*12.0)
fl = [fni, fna, fxi, fxa, rni, rna, rxi, rxa]
for f in fl:
    f[:,3] /= yfac
    f[:,2] *= xfac

#LOGSCALE?
ax = plt.gca()
ax.set_yscale('log')
import matplotlib.ticker as mtick
ax.yaxis.set_major_locator(mtick.LogLocator(base=100))
ax.yaxis.set_minor_locator(mtick.LogLocator(base=100))
plt.setp(ax.get_yminorticklabels(), visible=False);

#NUMBER OF TICS (NOT FOR LOGSCALE)
#plt.locator_params(axis='y', nbins=4)
plt.locator_params(axis='x', nbins=4)
#plt.locator_params(axis='x', numticks=10)



#ARTIFICIAL LINES
#ax.axhline(0, color='black', lw=1)
#ax.axvline(0, color='black', lw=1)

#---------------------------------------------------------------------------PLOT PLOT PLOT
bv = 2
hv = 3
plt.plot(rna[:,bv],rna[:,hv],'--', color='orange',   alpha=1.00 )
plt.plot(rni[:,bv],rni[:,hv],'--', color='blue', alpha=1.00 )
plt.plot(rxa[:,bv],rxa[:,hv],'-', color='orange',   alpha=1.00 , label=r'anisotropic')
plt.plot(rxi[:,bv],rxi[:,hv],'-', color='blue', alpha=1.00 , label=r'isotropic')
#plt.plot(f2[:,1],f2[:,0],'o', color='black', alpha=0.45 , label=r'$\theta=8.0^\circ$')
#plt.plot(f1[:,1],f1[:,0],'o', mec='red',  color='black', mfc='none', label=r'$\theta=7.5^\circ$')


#MAKING TICS NICE
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.xaxis.set_tick_params(length=8)
ax.yaxis.set_tick_params(length=8)
ax.xaxis.set_tick_params(width=1.1)
ax.yaxis.set_tick_params(width=1.1)
ax.tick_params(which='minor', length=5, width = 1, color='black')


#REMOVING TOP AND RIGHT TICS
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')


#SPECIFY BOUNDS HERE AND EXPLICIT TICKS ----------------------------------------- BOUNDS BOUNDS BOUNDS
#ax.set_xticks([5, 10, 15])
plt.xlim(left= 1e-3)
plt.xlim(right=0.01)
plt.ylim(top=1e-2)
plt.ylim(bottom=5e-7)
#----------------------------------------------------------------------------------

#LABELS
plt.ylabel(r'pdf',size=label_fs)
plt.xlabel(r'$\frac{\Delta^2_c}{12} \nabla \bar \phi \nabla \bar \phi$',size=label_fs)

#ax.set_xticklabels(x_ticks, rotation=0, fontsize=15)a
#TICK FONT SIZE
ax.tick_params(axis="x", labelsize=tic_fs)
ax.tick_params(axis="y", labelsize=tic_fs)
ax.yaxis.offsetText.set_fontsize(tic_fs)

#SCIENTIFIC NOTATION
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))


#GRID----------------------------------
#plt.grid(True)

#LEGENDS-------------------------------
plt.legend(fontsize=legend_fs, numpoints=1, frameon=False,loc='upper right', bbox_to_anchor= (1.0, 1.0), ncol=1, handletextpad=0.1, labelspacing=0.15)

plt.savefig(file_name, dpi = 100, bbox_inches='tight')
plt.show()
