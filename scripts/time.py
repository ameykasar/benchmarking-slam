#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.3
 
# set height of bar 0.368449, 0.116125,       0.409362,0.2782,          'fr2/large_loop', 'fr2/pioneerslam',
rgbd = [ 314.4850 , 84.0442,93.4713,157.567,46.7727,79.1437, 38.9614]
rtab = [443.34, 88.889425,76.3,284.411,66.212,109.648092,68.528952]
#bars3 = [0.29, 0.3, 0.24,0.25, 0.17]
 
# Set position of bar on X axis
r1 = np.arange(len(rgbd))
r2 = [x + barWidth for x in r1]
#r3 = [x + barWidth for x in r2]cd ..
 
# Make the plot
plt.bar(r1, rgbd, color='#0066ff', width=barWidth, edgecolor='white', label='RGBD-SLAM')
plt.bar(r2, rtab, color='#33cc33', width=barWidth, edgecolor='white', label='RTABMAP')
#plt.bar(r3, bars3, color='#2d7f5e', width=barWidth, edgecolor='white', label='var3')
 
# Add xticks on the middle of the group bars
plt.xlabel(' ', fontweight='bold')
plt.ylabel('Time Taken\n(sec)',fontweight='bold')
plt.xticks([r + barWidth for r in range(len(rgbd))], ['fr2/\ndesk with\nperson' , 'fr2/\npioneer360\nrobot slam', 'fr2/\n360\nkidnap','fr3/\nlong office\nhousehold', 'fr3/\nno struct\nno texture','fr3/\nno struct\ntexture','fr3/\nsitting\nstatic'])
# Create legend & Show graphic
plt.legend()
plt.show()
