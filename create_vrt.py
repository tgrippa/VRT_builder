import os 
import fnmatch
from osgeo import gdal


def find_files(path, pattern):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, pattern):
            yield os.path.join(root, file)

class create_vrt:
    def __init__(self, **kwargs):
        self.path_dir = kwargs.get("path_dir")
        self.pattern = kwargs.get("pattern")
        self.path_vrt = kwargs.get("path_vrt")


    def buildvrt(self):
        list_of_paths = [x for x in find_files(self.path_dir, self.pattern)]
        # Create a new VRT file
        vrt = gdal.BuildVRT(self.path_vrt, list_of_paths)
        # Save the VRT file
        vrt.FlushCache()

if __name__ == "__main__":

    # parse arguments
    import argparse
    from argparse import RawTextHelpFormatter

    parser = argparse.ArgumentParser(
        description="Create VRT (Virtual raster) file from all images contained in (sub-)directories",
        formatter_class=RawTextHelpFormatter
    )
    parser.add_argument(
        "--path_dir",
        type=str,
        default="/home/grippa/FNRS_processing/FLAIR_WeakSupervision/FLAIR_One_dataset/subset_dataset/train"
    )
    parser.add_argument(
    "--pattern",
    type=str,
    default="IMG*.tif"
    )
    parser.add_argument(
    "--path_vrt",
    type=str,
    default="/home/grippa/FNRS_processing/FLAIR_WeakSupervision/FLAIR_One_dataset/subset_dataset/subset_train.vrt"
    )

    config = vars(parser.parse_args())

    # Build VRT
    vrt_builder = create_vrt(**config)
    vrt_builder.buildvrt()