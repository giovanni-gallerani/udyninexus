# TODO AttributeError is the error when an attribute does not exists, we return None in that case, so we just need to check if attribute to see if it's there
# TODO put when saving time, time is saved as a datetime time.isoformat()
# TODO create longname concatenating name and units for the axis
# TODO check if axis and data are coherent
# TODO add parameters for specifying compression
# TODO create a naming convention for the files, could be experiment_ID + measurement_ID + file_ID (i would prefer it to be unique in the entire dataset)
# once in the supervisor directory the supervisor saves the file in the path related to that experiment and measurement
# then create a new entry in the file table
# TODO create the names of the beams accordingly
# TODO do a double check for all the lists to be sure the data is correct, someone could add wrong data using append

from typing import Optional
from os import makedirs


from .logging_settings import logger


def write_nexus(self, output_dir: Optional[str] = '.'):

    # Create the ouput directory if it does not already exists
    output_dir = (output_dir).absolute()
    try:
        makedirs(output_dir, exist_ok=True)
    except PermissionError:
        logger.error(f"Permission denied: Unable to create '{output_dir}'.")
    except Exception as e:
        logger.error(f"An error occurred while creating {output_dir}: {e}")
    

    # Save the NeXus file
    output_file = output_dir/Path(f'Udiny_test_file.nxs')
    root.save(output_file, 'w')
    print(f'{output_file.name} saved in {output_dir}')