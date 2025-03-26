# TODO create longname concatenating name and units for the axis
# TODO add parameters for specifying compression
# TODO create a naming convention for the files, could be experiment_ID + measurement_ID + file_ID (i would prefer it to be unique in the entire dataset)
# once in the supervisor directory the supervisor saves the file in the path related to that experiment and measurement
# then create a new entry in the file table
# TODO create getter methods for definition, experiment type and subtype in NexusDataContainer, for now they are hardcoded
# TODO understand the cause of the warning for many of the XN classes

from .classes.NexusContainer import NexusContainer
from .nexus_validation import validate_nexus_data
from .logging_settings import logger

from nexusformat.nexus import *
from os import makedirs
from pathlib import Path


def write_nexus(nexus_container: NexusContainer, output_dir: str = '.'):
    '''
    Save the data in the NexusDataContainer in a NeXus file inside the specified directory.\n
    If no directory is specified, save the file into the current directory.
    Saves the file only if the NexusDataContainer is valid, otherwise throw exception.
    '''
    if not validate_nexus_data(nexus_container):
        logger.error(f'Invalid nexus_container, the NeXus file has not been created')
        raise ValueError

    root = NXroot()

    # ENTRY
    root['/entry'] = NXentry()
    root['/entry/definition'] = NXfield('NXoptical_spectroscopy')
    root['/entry/definition'].attrs['URL'] = 'https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXoptical_spectroscopy.html#nxoptical-spectroscopy'
    root['/entry/definition'].attrs['version'] = '1.0'
    root['/entry/title'] = NXfield(nexus_container.title)
    root['/entry/start_time'] = NXfield(nexus_container.start_time.isoformat())
    root['/entry/end_time'] = NXfield(nexus_container.end_time.isoformat())
    root['/entry/identifier_experiment'] = NXfield(nexus_container.identifier_experiment)
    root['/entry/experiment_description'] = NXfield(nexus_container.experiment_description)
    root['/entry/experiment_type'] = NXfield('transmission spectroscopy')
    root['/entry/experiment_sub_type'] = NXfield('pump-probe')

    # INSTRUMENT
    root['/entry/instrument'] = NXinstrument()
    
    # SOURCES
    for source in nexus_container.sources:
        root[f'/entry/instrument/source_{source.name_in_nexus}'] = NXsource()
        root[f'/entry/instrument/source_{source.name_in_nexus}/type'] = NXfield(source.type)
    
    # BEAMS
    for beam in nexus_container.beams:
        root[f'/entry/instrument/beam_{beam.name_in_nexus}'] = NXbeam()
        root[f'/entry/instrument/beam_{beam.name_in_nexus}/parameter_reliability'] = NXfield(beam.parameter_reliability)
        root[f'/entry/instrument/beam_{beam.name_in_nexus}/incident_wavelenght'] = NXfield(beam.incident_wavelength)
        root[f'/entry/instrument/beam_{beam.name_in_nexus}/incident_wavelenght'].attrs['units'] = beam.incident_wavelength_units
        root[f'/entry/instrument/beam_{beam.name_in_nexus}/incident_polarization'] = NXfield(beam.incident_polarization)
        root[f'/entry/instrument/beam_{beam.name_in_nexus}/associated_source'] = NXfield(f'/entry/instrument/source_{beam.associated_source.name_in_nexus}')
        root[f'/entry/instrument/beam_{beam.name_in_nexus}/beam_polarization_type'] = NXfield(beam.beam_polarization_type)
        root[f'/entry/instrument/beam_{beam.name_in_nexus}/beam_type'] = NXfield(beam.beam_type)

    # DETECTORS
    for detector in nexus_container.detectors:
        root[f'/entry/instrument/detector_{detector.name_in_nexus}'] = NXdetector()
        root[f'/entry/instrument/detector_{detector.name_in_nexus}/detector_channel_type'] = NXfield(detector.detector_channel_type)
        root[f'/entry/instrument/detector_{detector.name_in_nexus}/detector_type'] = NXfield(detector.detector_type)

    # SAMPLE
    root['/entry/sample'] = NXsample()
    root['/entry/sample/name'] = NXfield(nexus_container.sample.name)
    root['/entry/sample/sample_id'] = NXfield(nexus_container.sample.sample_id)

    # DATA
    signal = NXfield(
        nexus_container.data.signal_data,
        name=nexus_container.data.signal_name, 
        units=nexus_container.data.signal_units, 
        long_name=f'{nexus_container.data.signal_name} ({nexus_container.data.signal_units})'
    )
    axes = []
    for axis in nexus_container.data.axes:
        axes.append(NXfield(axis.data, name=axis.name, units=axis.units, long_name=f'{axis.name} ({axis.units})'))
    # creating NXdata in this way is useful because the attributes signal and axes gets assigned as part of the creation of NXdata
    root['/entry/data'] = NXdata(signal, tuple(axes))

    root['/entry/data'].set_default()


    # Create the ouput directory if it does not already exists
    output_dir_full_path = Path(output_dir).resolve()
    try:
        makedirs(output_dir_full_path, exist_ok=True)
    except PermissionError:
        logger.error(f"Permission denied: Unable to create '{output_dir_full_path}'.")
        exit(1)
    except Exception as e:
        logger.error(f"An error occurred while creating {output_dir_full_path}: {e}")
        exit(1)

    # Save the NeXus file
    nexus_file_name = 'Udiny_test_file.nxs'
    output_file_full_path = output_dir_full_path / nexus_file_name
    root.save(output_file_full_path, 'w')
    print(f'{output_file_full_path.name} saved in {output_dir_full_path}')