from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
from copy import deepcopy


from .logging_settings import logger


def get_time_now(timezone: str):
    try:
        time = datetime.now(ZoneInfo(timezone))
    except ZoneInfoNotFoundError:
        logger.error(f'Invalid value for timezone: {timezone}. No time zone found')
        raise ValueError
    return time


def get_shape(obj):
    """Returns the shape of obj if possible, otherwise raises TypeError."""
    if hasattr(obj, "shape"):  # NumPy arrays, Torch tensors, etc.
        return obj.shape  
    elif isinstance(obj, range):  # Treat range like a 1D tuple
        return (len(obj),)
    elif isinstance(obj, (list, tuple)):  # Handle nested lists/tuples
        def _recursive_shape(lst):
            if isinstance(lst, (list, tuple)) and lst: 
                return (len(lst),) + _recursive_shape(lst[0])  # Recursively compute shape
            return ()
        return _recursive_shape(obj)
    else:
        raise TypeError(f"Object of type {type(obj).__name__} does not have a valid shape.")


def typeErrorCheck(variable_name, value, expected_type):
    if type(value) is not expected_type:
        logger.error(f'Invalid type for {variable_name}: {value}. Must be of type {expected_type.__name__}.')
        raise TypeError(f'Invalid type for {variable_name}: {value}. Must be of type {expected_type.__name__}.')


def typeErrorCheckList(variable_name, value, expected_type_of_each_element):
    typeErrorCheck(variable_name, value, list)
    for element in value:
        if type(element) is not expected_type_of_each_element:
            logger.error(f'Invalid type for {variable_name}: {value}. Each element of the list must be of type {expected_type_of_each_element.__name__}.')
            raise TypeError(f'Invalid type for {variable_name}: {value}. Each element of the list must be of type {expected_type_of_each_element.__name__}.')


def typeErrorCheck_requires_shape(variable_name, value):
    try:
        get_shape(value)
    except TypeError as e:
        logger.error(f'Invalid type for {variable_name}. Must be an array-like object (e.g., list, tuple, range, NumPy array) with a shape.')
        raise TypeError(f'Invalid type for {variable_name}. Must be an array-like object (e.g., list, tuple, range, NumPy array) with a shape. {e}')


def valueError_inList_Check(variable_name, value, list_of_valid_values):
    if value not in list_of_valid_values:
        logger.error(f'Invalid value for {variable_name}: {value}. Expected one of the following: {list_of_valid_values}.')
        raise ValueError(f'Invalid value for {variable_name}: {value}. Expected one of the following: {list_of_valid_values}.')


def create_typed_property(attribute_name, expected_type=None, requires_shape=False):
    """
    Creates a property with a getter and a setter that validates the type.

    Args:
        name (str): The attribute name.
        expected_type (type): The expected type of the attribute.
        requires_shape (bool): If true it's required for the attribute to be array-like object (e.g., list, tuple, NumPy array) with a shape.

    Returns:
        property: A property object with type validation.
    """
    private_name = f'__{attribute_name}'

    def getter(self):
        return getattr(self, private_name, None)  # returns None if the attribute is not set

    def setter(self, value):
        if value is not None:
            if expected_type:
                typeErrorCheck(attribute_name, value, expected_type)
            if requires_shape:
                typeErrorCheck_requires_shape(attribute_name, value)
        setattr(self, private_name, deepcopy(value))

    return property(getter, setter)


def create_typed_property_for_list(attribute_name, expected_type_of_each_element):
    """
    Creates a property with a getter and a setter that validates the type, the attribute in this case must be a list of elements of a certain type.
    This function uses deepcopy intrenally to safely copy the data inside the class.

    Args:
        name (str): The attribute name.
        expected_type_of_each_element (type): The expected type of each element of the list.

    Returns:
        property: A property object with type validation.
    """
    private_name = f'__{attribute_name}'

    def getter(self):
        return getattr(self, private_name, None)

    def setter(self, value):
        if value is not None:
            typeErrorCheckList(attribute_name, value, expected_type_of_each_element)
        setattr(self, private_name, deepcopy(value)) # without deepcopy the objects that constitute the list if edited would be edited in the NexusDataContainer!!!

    return property(getter, setter)


def create_valued_property(attribute_name, list_of_valid_values):
    """
    Creates a property with a getter and a setter that validates the type.

    Args:
        name (str): The attribute name.
        expected_type (type): The expected type of the attribute.

    Returns:
        property: A property object with type validation.
    """
    private_name = f'__{attribute_name}'

    def getter(self):
        return getattr(self, private_name, None)  # returns None if the attribute is not set

    def setter(self, value):
        if value is not None:
            valueError_inList_Check(attribute_name, value, list_of_valid_values)
        setattr(self, private_name, value)

    return property(getter, setter)