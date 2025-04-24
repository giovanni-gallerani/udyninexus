from ..utils import create_property_check_one_dimensional_axis_data, create_property_check_isinstance, create_property_check_type, create_property_check_type_for_lists
from .Instrument import Instrument
from typing import Optional, List, Any


class Axis:
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