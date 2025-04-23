from ..utils import create_property_check_isinstance, create_property_check_type, create_property_check_type_for_lists
from .Instrument import Instrument
from typing import Optional, List, Any


class Axis:
    def __init__(self,
            name: str = None,
            data: Optional[List] = None,
            units: Optional[str] = None,
            reference: Optional[Instrument] = None,
        ):
        self.name = name
        self.data = data
        self.units = units
        self.reference = reference

    # Getters and setters
    name = create_property_check_type('name', str)
    data = create_property_check_type('data', requires_shape=True)
    units = create_property_check_type('units', str)
    reference = create_property_check_isinstance('reference', Instrument)


class Data:
    def __init__(self,
            signal_name: str = None,
            signal_data: Any = None,
            signal_units: str = None,
            signal_reference: Instrument = None,
            axes: List[Axis] = None
        ):
        self.signal_name = signal_name
        self.signal_data = signal_data
        self.signal_units = signal_units
        self.signal_reference = signal_reference
        self.axes = axes
    
    # Getters and setters
    signal_name = create_property_check_type('signal_name', str)
    signal_data = create_property_check_type('signal', requires_shape=True)
    signal_units = create_property_check_type('signal_units', str)
    signal_reference = create_property_check_isinstance('signal_reference', Instrument)
    axes = create_property_check_type_for_lists('axes', Axis)
    # an integrity check that assures that the axis and the data are compatible is performed when the nexus file is created using saveNexus