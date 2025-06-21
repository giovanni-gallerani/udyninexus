from udyninexus.classes.Instrument import Instrument
from udyninexus.utils import create_property_check_one_dimensional_axis_data, create_property_check_isinstance, create_property_check_type, create_property_check_type_for_lists

from typing import Optional, List, Any


class Axis:
    """
    Represents a one-dimensional axis in data.

    Attributes:
        name (str): Name used to identify this axis in the NeXus file. This will be the key under which the signal data is stored.
        data (List): A one-dimensional sequence of values representing the axis (e.g., range(10)).
        units (str): The unit of measurement for the axis values (e.g., 'nm', 'ms'). Defaults to 'index' if not specified.
        related_instrument (Instrument): Reference to the instrument that controls or is associated with this axis.\
        If specified the signal data will be stored inside this instrument's group in the NeXus file and linked via an NXlink in the 'data' group.\
        Otherwise the data of the axis will be directly saved inside the 'data' group.
    """
    def __init__(self,
            name: str = None,
            data: Optional[List] = None,
            units: Optional[str] = None,
            related_instrument: Optional[Instrument] = None,
        ):
        self.name = name
        self.data = data
        self.units = units
        self.related_instrument = related_instrument

    # Getters and setters
    name = create_property_check_type('name', str)
    data = create_property_check_one_dimensional_axis_data('data')
    units = create_property_check_type('units', str)
    related_instrument = create_property_check_isinstance('related_instrument', Instrument)


class Data:
    """
    Represents measured signal data.

    Attributes:
        signal_name (str): Name used to identify the signal in the NeXus file. This will be the key under which the signal data is stored.
        signal_data: A multi-dimensional array of values representing the signal measurements.
        signal_units (str): Unit of measurement for the signal values (e.g., 'nm', 'ms').
        signal_related_instrument (Instrument): Reference to the instrument that measured the signal. The signal data will be stored inside this instrument's group in the NeXus file and linked via an NXlink in the 'data' group.
        axes (List[Axis]): List of axes associated with the signal data.
    """

    def __init__(self,
            signal_name: str = None,
            signal_data: Any = None, # it must be a data with a shape (multi dimensional array)
            signal_units: str = None,
            signal_related_instrument: Instrument = None,
            axes: List[Axis] = None
        ):
        self.signal_name = signal_name
        self.signal_data = signal_data
        self.signal_units = signal_units
        self.signal_related_instrument = signal_related_instrument
        self.axes = axes
    
    # Getters and setters
    signal_name = create_property_check_type('signal_name', str)
    signal_data = create_property_check_type('signal', requires_shape=True)
    signal_units = create_property_check_type('signal_units', str)
    signal_related_instrument = create_property_check_isinstance('signal_related_instrument', Instrument)
    axes = create_property_check_type_for_lists('axes', Axis)
    # an integrity check that assures that the axis and the data are compatible is performed when NexusContainer is validated