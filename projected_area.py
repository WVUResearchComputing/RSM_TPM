#!/usr/bin/env python3

"""
Code to calculate Projected area given n-dimensions
"""
import numpy as np
import os
import json
from scipy.interpolate import  LinearNDInterpolator
from scipy.interpolate import  NearestNDInterpolator
from scipy.interpolate import  griddata


def read_input_info(basedir):
     topdir = os.getcwd()
     inputdir = os.path.join(topdir,'Inputs')
     print('Reading Model Input Information \n')
     jsonpath = os.path.join(inputdir, "Model_Evaluation.json")
     rf=open(jsonpath)
     md=json.load(rf)
     MODEL_NAME = md['Model Name']
     Rotation = md['Component Rotation (1=No,2=Yes)']
                
  
                  
     return Rotation 






def area(base_folder):
    """
    

    Parameters
    ----------
    base_folder : TYPE
        Top level folder of the RSM Suite

    Returns
    -------
    Projected Area

    """
    Rotation = read_input_info(base_folder)
    values=[]
    areafile = (base_folder+os.sep+"Outputs/Projected_Area/Aout.dat")
    fcount = open(areafile,'r')
    line_count =0
    for i in fcount:
        if i != "\n":
            line_count += 1
    fcount.close()
    
    f = open(areafile,'r')
    j=0
    for line in f: 
        
        data = line.split()
        floats = []
        for elem in data:
            try:
                floats.append(float(elem))
            except ValueError:
                pass
        if j == 0:
            columns = len(floats)
            values = np.zeros([line_count,columns])
        values[j,:] = np.array(floats)
        j+= 1

    f.close()
     

    points = values[:,1:]
    areavalues = np.array(values[:,0])
   
    
    
    csvfile = (base_folder+os.sep+"Inputs/Model_Evaluation_Inputs/Model_Input_Data.csv")
    inp = np.loadtxt(csvfile,delimiter=',',skiprows=1)
    

    yawreq = np.reshape(inp[:,3],(len(inp),1))
    pitchreq = np.reshape(inp[:,4],(len(inp),1))
    if Rotation==2:
        rotreq = inp[:,12:]
        request = np.hstack((yawreq,pitchreq,rotreq))
    elif Rotation ==1:
        request = np.hstack((yawreq,pitchreq))
    else:
        print('Enter Valid Rotation Flag') 


    interp=NearestNDInterpolator(points, areavalues)
    
    project_area = interp(request)
    print(project_area)
    return project_area                  




    
    
 
    
if __name__ == "__main__":
    
   projected_area =  area('.')
    
    
