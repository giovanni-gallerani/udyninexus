from udyninexus.classes.NexusContainer import NexusContainer
from udyninexus.classes.Beam import Beam
from udyninexus.classes.Detector import Detector
from udyninexus.classes.Source import Source
from udyninexus.classes.Sample import Sample
from udyninexus.classes.Data import Axis, Data
from udyninexus.utils import get_shape
from udyninexus.logging_settings import logger


def _get_invalid_none_attributes(instance_name: str, instance, allowed_none: set) -> list[str]:
    """
    Return a list of error messages for attributes in the given instance that are None but not allowed to be.

    Parameters:
    - instance_name (str): A name used to identify the instance in the error messages.
    - instance: The object whose attributes will be checked.
    - allowed_none (set): A set of attribute names that are allowed to be None.

    Returns:
    - list[str]: A list of strings describing each invalid attribute found.
        If all elements are valid, the list will be empty.
    """
    errors = []
    for attr, value in vars(instance).items():
        attr = str(attr).replace('__', '')  # Clean up private attribute names
        if value is None and attr not in allowed_none:
            errors.append(f"{instance_name}.{attr} cannot be None.")
    return errors


def _get_invalid_type_and_invalid_none_attributes_of_list_elements_(list_name: str, elements: list, expected_type: type, allowed_none: set) -> list[str]:
    """
    Return a list of error messages for all elements in a list that are not exactly of the expected type.
    For elements of the list of the expected type, return a list of error messages for attributes that are None but not allowed to be.

    Parameters:
    - list_name (str): A name used to identify the list in the error messages.
    - elements (list): The list of elements to check.
    - expected_type (type): The exact expected type of each element (no subclassing allowed).

    Returns:
    - list[str]: A list of error messages for
        - elements of the list that are not of the expected type
        - attributes that are None but not allowed to be for elements of the expected type.
        If there is no anomaly, the list will be empty.
    """
    errors = []
    for i, element in enumerate(elements):
        if type(element) is not expected_type:
            errors.append(f"{list_name}[{i}] is not of type {expected_type.__name__}.")
        else:
            errors.extend(_get_invalid_none_attributes(f"{list_name}[{i}]", element, allowed_none))
    return errors


def _get_invalid_axes_data_relation_and_fill_axes_data(data: Data):
    """
    Chack if there are enought axes for data.
    Check if all the Axis are one dimensional arrays, numpy array or ranges.
    If an axis has data = None assign to data a value based on the signal dimensions.
    If an axis has data not None check if it's coherent with the signal dimensions.
 
    Returns:
        If all the axis are valid returns an empty string, otherwise return a list with all the validation errors founded.
    """
    errors = []
    signal_shape = get_shape(data.signal_data)
    if len(signal_shape) != len(data.axes):
        errors.append(f"NexusContainer.data.signal requires {len(signal_shape)} axes but only {len(data.axes)} elements are present in NexusContainer.data.axes.")
    else:
        for i, axis in enumerate(data.axes):
            if type(axis) == Axis: # no need to append to errors if axis is not an Axis since it is done by the previous function
            
                if axis.data is None: # if axis data is not specified use the shape of the signal to deduct it
                    axis.data = range(signal_shape[i])
                    logger.info(f'Setted NexusContainer.data.axis.[{i}].data to {range(signal_shape[i])}.')
                
                else:
                    axis_shape = get_shape(axis.data)
                    if len(axis_shape) == 1: # if the axis is valid (is a one dimensional array) check if the shape fits the data
                        if axis_shape[0] != signal_shape[i]:
                            errors.append(f"NexusContainer.data.axis.[{i}].data has shape {axis_shape} but should have shape ({signal_shape[i]},).")
                    else:
                        errors.append(f"NexusContainer.data.axis.[{i}].data is not a one dimensional axis.")
                        

                if axis.units is None: # if the axis does not have units is an index
                    axis.units = 'index'
                    logger.info(f'Setted NexusContainer.data.axis.[{i}].units to index.')
    
    return errors


def errors_in_nexus_container(nexus_container: NexusContainer) -> list[str]:
    """
    Check if NexusContainer can be saved without errors using write_nexus.
    Checks if every field in the NexusDataContainer is not None.
    Checks if every list has all the elements of the same type.
    Also does integrity checks such as verify that the shape of the signal in Data and the shape of the axis, are compatible.

    Returns:
        If the NexusContainer is valid returns an empty string, otherwise return a list with all the errors in the object.
    """
    errors = []

    # ENTRY
    errors.extend(_get_invalid_none_attributes('NexusContainer', nexus_container, {}))

    # BEAMS
    errors.extend(_get_invalid_type_and_invalid_none_attributes_of_list_elements_('NexusContainer.beams', nexus_container.beams, Beam, {}))
    
    # DETECTORS
    errors.extend(_get_invalid_type_and_invalid_none_attributes_of_list_elements_('NexusContainer.detectors', nexus_container.detectors, Detector, {}))

    # SOURCES
    errors.extend(_get_invalid_type_and_invalid_none_attributes_of_list_elements_('NexusContainer.sources', nexus_container.sources, Source, {}))

    # SAMPLE
    errors.extend(_get_invalid_none_attributes('NexusContainer.sample', nexus_container.sample, {}))

    # DATA
    errors.extend(_get_invalid_none_attributes('NexusContainer.data', nexus_container.data, {})) # note that signal_related_instrument cannot be None

    # AXES
    errors.extend(_get_invalid_type_and_invalid_none_attributes_of_list_elements_('NexusContainer.data.axis', nexus_container.data.axes, Axis, {'data', 'units', 'related_instrument'}))
    errors.extend(_get_invalid_axes_data_relation_and_fill_axes_data(nexus_container.data))

    return errors