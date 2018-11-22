#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.3
 
# set height of bar 0.368449, 0.116125,       0.409362,0.2782,          'fr2/large_loop', 'fr2/pioneerslam',
rgbd = [ 0.114990, 0.253336 ,1.49554, 0.009449,0.056130 , 0.080732,0.086905 ]
rtab = [0.129466 , 0.460893, 0.449568 ,0.013724,0.061444,0.072157, 0.156432]
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
plt.ylabel('RPE\nTranslational RMSE\n(m)',fontweight='bold')
plt.xticks([r + barWidth for r in range(len(rgbd))], ['fr2/\ndesk with\nperson' , 'fr2/\npioneer360\nrobot slam', 'fr2/\n360\nkidnap','fr3/\nlong office\nhousehold', 'fr3/\nno struct\nno texture','fr3/\nno struct\ntexture','fr3/\nsitting\nstatic'])
# Create legend & Show graphic
plt.legend()
plt.show()
