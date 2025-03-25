from .classes.NexusDataContainer import NexusDataContainer
from .classes.Beam import Beam
from .classes.Detector import Detector
from .classes.Source import Source
from .classes.Sample import Sample
from .classes.Data import Axis, Data
from .logging_settings import logger


def validate_nexus_data(nexus_container: NexusDataContainer) -> bool:
    '''
    Returns True if the NexusDataContainer can be saved without errors using saveNexus.
    Also print in log all the problems encountered.

    Checks if every field in the NexusDataContainer is not None and if it has the right type.
    Also does integrity checks such as verify that the shape of the signal in Data and the shape of the axis, are compatible.
    '''
    valid = True

    
    def _no_none_in_instance(instance, allowed_none: set) -> bool:
        '''
        Validate that only the optional parameters can be = None
        '''
        valid = True
        for attr, value in vars(instance).items():  # Iterate over all attributes
            logger.debug(f'{attr}: {value}')
            if value is None and attr not in allowed_none:
                logger.error(f"Attribute '{attr}' in {instance} cannot be None.")
                valid = False
            
        return valid
    

    def _all_elements_of_the_same_type(list_name, list, expected_type_of_each_element) -> bool:
        '''
        Checks if all the elements of a list are of the same expected type
        '''
        for element in list:
            if type(element) is not expected_type_of_each_element:
                logger.error(f"The elements of  {list_name}: {list} are not all of type {expected_type_of_each_element.__name__}.")
                return False
        return True
    
    # errors = []
    # validations = [_no_none_in_instance, _all_elements_of_the_same_type]
    # for function in validations:
    #     errors.append(function(container))

    # ENTRY
    valid = _no_none_in_instance(nexus_container, {}) and valid

    # BEAMS
    for element in nexus_container.beams:
        valid =  _no_none_in_instance(element, {}) and valid
    valid = _all_elements_of_the_same_type('beams', nexus_container.beams, Beam) and valid
    
    # DETECTORS
    for element in nexus_container.detectors:
        valid = _no_none_in_instance(element, {}) and valid
    valid = _all_elements_of_the_same_type('detectors', nexus_container.detectors, Detector) and valid

    # SOURCES
    for element in nexus_container.sources:
        valid = _no_none_in_instance(element, {}) and valid
    valid = _all_elements_of_the_same_type('sources', nexus_container.sources, Source) and valid

    # SAMPLE    
    valid = _no_none_in_instance(element, {}) and valid

    # DATA
    valid = _no_none_in_instance(nexus_container.data, {}) and valid




    # TODO validate shape in data confronting signal and axes




    
    # AXES
    for element in nexus_container.data.axes:
        valid = _no_none_in_instance(element, {'__data', '__units'}) and valid
    valid = _all_elements_of_the_same_type('axes', nexus_container.data.axes, Axis) and valid

    return valid