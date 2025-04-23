# Future developements
# - Add parameters for specifying compression
# - Create methods for editing definition in NexusDataContainer, for now it's hardcoded since the lab will only use an implementation of NXoptical_spectroscopy

from .classes.NexusContainer import NexusContainer
from .nexus_validation import errors_in_nexus_container
from .logging_settings import logger
from .exceptions import NexusValidationError, NexusSaveError

from nexusformat.nexus import *
from pathlib import Path


def write_nexus(nexus_container: NexusContainer, filename: str):
    '''
    Save the data in the NexusDataContainer in a specified NeXus file.\n
    If the specified path does not exist, this function creates it and save the file inside it.\n
    
    Raises:
        NexusValidationError: throwed when NexusContainer object is not valid.
        NexusSaveError: throwed when occours an error while trying to save the NeXus file.
    '''

    logger.info("Starting validation of NexusContainer...")
    errors = errors_in_nexus_container(nexus_container)
    if  errors != []:
        logger.error("Validation failed.")
        joined_errors = '\n'.join(errors)
        raise NexusValidationError(
            f"Invalid NexusContainer, the NeXus file cannot be created:\n{joined_errors}"
        )
    logger.info("Validation successful.")
    
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
    root['/entry/experiment_type'] = NXfield(nexus_container.experiment_type)
    root['/entry/experiment_sub_type'] = NXfield(nexus_container.experiment_sub_type)

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


    filename_full_path = Path(filename).resolve()
    logger.info(f"Creating necessary directories for saving {filename_full_path}...")
    directories = filename_full_path.parent
    try:
        directories.mkdir(parents=True, exist_ok=True)
    except (PermissionError, FileExistsError, OSError, Exception) as e:
        logger.error(f"Failed to create directory '{directories}': {e}")
        raise NexusSaveError(f"Failed to create directory '{directories}': {e}") from e
    logger.info(f"Created necessary directories for saving {filename_full_path}")


    logger.info(f"Saving Nexus file to {filename_full_path}...")
    try:
        root.save(filename_full_path)
    except NeXusError as e:
        logger.error(f"Failed to save NeXus file at {filename_full_path}: {e}")
        raise NexusSaveError(e) from e
    logger.info(f"File saved to {filename_full_path}")