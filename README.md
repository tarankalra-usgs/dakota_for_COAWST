Dakota sensitivity analysis for COAWST 

Instructions for dakota installation are here: 

* https://github.com/tarankalra-usgs/self_notes/blob/master/installing%20dakota%20on%20Linux

Files in this repository: 

* ana_grid.h, ocean_sedbed_toy.in, wind_restrat_2events.nc,sedbedtoy.h - original sedbedtoy files for COAWST runs
* util.py - output script to get the model output for sensitivity purposes 

* dprepro - executable file for dakota 
* dakota_sebded.in - sediment input file that will be copied to form multiple input files
* templatedir - template directory that will save sediment input files when they are changed for sensitivity analysis
* simulator_script - 
