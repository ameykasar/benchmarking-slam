#!/usr/bin/python

# Requirements: 
# sudo apt-get install python-argparse

"""
This script computes the absolute trajectory error from the ground truth
trajectory and the estimated trajectory.
"""

import sys
import numpy
import argparse
import associate

def plot_traj(ax,stamps,traj,style,color,label):
    """
    Plot a trajectory using matplotlib. 
    
    Input:
    ax -- the plot
    stamps -- time stamps (1xn)
    traj -- trajectory (3xn)
    style -- line style
    color -- line color
    label -- plot legend
    
    """
    stamps.sort()
    interval = numpy.median([s-t for s,t in zip(stamps[1:],stamps[:-1])])
    x = []
    y = []
    last = stamps[0]
    for i in range(len(stamps)):
        if stamps[i]-last < 2*interval:
            x.append(traj[i][0])
            y.append(traj[i][1])
        elif len(x)>0:
            ax.plot(x,y,style,color=color,label=label)
            label=""
            x=[]
            y=[]
        last= stamps[i]
    if len(x)>0:
        ax.plot(x,y,style,color=color,label=label)
            

if __name__=="__main__":
    # parse command line
    parser = argparse.ArgumentParser(description='''
    This script plots the ground truth trajectory. use --plot fig_name.png 
    ''')
    parser.add_argument('first_file', help='ground truth trajectory (format: timestamp tx ty tz qx qy qz qw)')
    parser.add_argument('--plot', help='plot the first and the aligned second trajectory to an image (format: png)')
    args = parser.parse_args()

    first_list = associate.read_file_list(args.first_file)
  
    first_stamps = first_list.keys()
    first_stamps.sort()
    first_xyz_full = numpy.matrix([[float(value) for value in first_list[b][0:3]] for b in first_stamps]).transpose()
    
    if args.plot:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        import matplotlib.pylab as pylab
        from matplotlib.patches import Ellipse
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plot_traj(ax,first_stamps,first_xyz_full.transpose().A,'-',"black","ground truth")
        #plot_traj(ax,second_stamps,second_xyz_full_aligned.transpose().A,'-',"blue","estimated")

       # label="difference"
        #for (a,b),(x1,y1,z1),(x2,y2,z2) in zip(matches,first_xyz.transpose().A,second_xyz_aligned.transpose().A):
            #ax.plot([x1,x2],[y1,y2],'-',color="red",label=label)
            #label=""
            
        ax.legend()
            
        ax.set_xlabel('x [m]')
        ax.set_ylabel('y [m]')
        plt.savefig(args.plot,dpi=90)
        
