from .classes.NexusContainer import NexusContainer
from .classes.Beam import Beam
from .classes.Detector import Detector
from .classes.Source import Source
from .classes.Sample import Sample
from .classes.Data import Axis, Data


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
            errors.append(f"{list_name}[{i}] is not of type {expected_type.__name__}")
        else:
            errors.extend(_get_invalid_none_attributes(f"{list_name}[{i}]", element, allowed_none))
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
    errors.extend(_get_invalid_none_attributes('NexusContainer.data', nexus_container.data, {}))

    # AXES
    errors.extend(_get_invalid_type_and_invalid_none_attributes_of_list_elements_('NexusContainer.data.axis', nexus_container.data.axes, Axis, {'data', 'units'}))

    # TODO validate shape in data confronting signal and axes

    return errors