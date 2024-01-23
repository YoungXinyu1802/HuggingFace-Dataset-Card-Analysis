---
license: mit
---

This dataset is comprised of ECMWF ERA5-Land data covering 2014 to October 2022. This data is on a 0.1 degree grid and has fewer variables than the standard ERA5-reanalysis, but at a higher resolution. All the data has been downloaded as NetCDF files from the Copernicus Data Store and converted to Zarr using Xarray, then uploaded here. Each file is one day, and holds 24 timesteps.