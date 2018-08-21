import netCDF4
import numpy as np 

datafile='ocean_his.nc'
ncfile=netCDF4.Dataset(datafile,'r')
try:
    x_rho=ncfile.variables['lon_rho'][:]
    y_rho=ncfile.variables['lat_rho'][:]
    axis='degrees'
except:
    x_rho=ncfile.variables['x_rho'][:]
    y_rho=ncfile.variables['y_rho'][:]
    axis='mts.'
try:
    mask_rho=ncfile.variables['mask_rho'][:]
except:
    mask_rho=1
sand01=ncfile.variables['sand_01'][:]*mask_rho
ntime,nx,ny,nz=sand01.shape
print(ntime,nx,ny,nz)
print sand01[ntime-1,nx-1,ny-1,nz-1]

