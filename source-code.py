# IMPORTING DEPENDENCIES

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patch

# PLOTTING THE TRICOLOR

green = patch.Rectangle((0,1), width = 8, height = 2, facecolor = '#138808')
white = patch.Rectangle((0,3), width = 8, height = 2, facecolor = '#FFFFFF')
saffron = patch.Rectangle((0,5), width = 8, height = 2, facecolor = '#FF9933')
m, n = plt.subplots()
n.add_patch(green)
n.add_patch(white)
n.add_patch(saffron)

# ASHOKA CHAKRA

radius = 0.8
plt.plot(4,4, marker = '.', markerfacecolor = '#000080', markersize = 2)
chakra = plt.Circle((4,4), radius, color = '#000080', fill = False, linewidth = 4)
n.add_artist(chakra)

# 24 STROKES OF THE ASHOKA CHAKRA

for i in range(0,24):
  p = 4 + radius/2 * np.cos(np.pi*i/12 + np.pi/48)
  q = 4 + radius/2 * np.cos(np.pi*i/12 - np.pi/48)
  r = 4 + radius/2 * np.sin(np.pi*i/12 + np.pi/48)
  s = 4 + radius/2 * np.sin(np.pi*i/12 - np.pi/48)
  t = 4 + radius   * np.cos(np.pi*i/12)
  u = 4 + radius   * np.sin(np.pi*i/12)
  n.add_patch(patch.Polygon([[4, 4], [p, r], [t, u], [q, s]], fill = True, closed = True, color = '#000080'))

# TITLE AND LABEL

plt.title('''79ve Svantrata Diwas ki Hardik Shubhkamnayein
Happy 79th Independence Day''')

plt.xlabel('By @HeyVatsy. Code Credits: @KnowProgram')

# SHOWING THE PLOT

plt.axis('equal')
plt.show()
