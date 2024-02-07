import processing
import pandas as pd

sun = pd.read_csv('SR_full_data.csv')

i=0

for az, alt in zip(sun.azimuth.to_numpy(), sun.altitude.to_numpy()):
    if alt>0: # I don't want to make a run if it is night time, it's just a waste of time
        processing.run("terrain_shading:Shadow depth", {'INPUT':'MEGAsync/univ/SNODAS/terrain_rasters/SFF_30m_squared_METERED_CRS.tif', 'DIRECTION':az, 'ANGLE':alt, 'SMOOTH':True, 'OUTPUT':'MEGAsync/univ/SNODAS/notebooks solar radiation/shadow_rasters/'+str(i)+'.tif'})

    i+=1
