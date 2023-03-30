# VRT_builder
Short python script to create Virtual Raster file (VRT) from image files in (sub-)directories. 

# Usage
In a terminal, call the Python script with the following arguments: 

| --path_folder | Path to the folder containing image files. The script will look to all subfolders so be careful. |
| --path_vrt | Path to the VRT file to create (should end with '.vrt') |
| --pattern | The pattern of the image file to look for. Use * as a wildcard (e.g., 'IMG_*.jpg') |

## Example
```
/bin/python3 create_vrt.py --path_vrt=./subset_train_label.vrt --path_dir=./train --pattern=MSK*
```
