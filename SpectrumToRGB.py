import numpy as np
import sys
from colour_system import cs_hdtv
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

cs = cs_hdtv
file = str(sys.argv[1])



spec = np.loadtxt(file, usecols=(1),skiprows=1)
#print (len(spec))
html_rgb = cs.spec_to_rgb(spec, out_fmt='html')
print (html_rgb)


fig,ax = plt.subplots()
i=0
x, y = i % 6, -(i // 6)
circle = Circle(xy=(x, y*1.2), radius=0.4, fc=html_rgb)
ax.add_patch(circle)

ax.set_xlim(-0.5,0.5)
ax.set_ylim(-0.5, 0.5)
ax.set_xticks([])
ax.set_yticks([])
ax.set_facecolor('k')
ax.set_aspect("equal")
plt.show()