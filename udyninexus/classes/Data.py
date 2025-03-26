from ..utils import create_typed_property, create_typed_property_for_list


from typing import Optional, List


# TODO specify with Optional which elements are actually optional


class Axis:
    def __init__(self,
            name: str = None,
            data: Optional[List] = None,
            units: Optional[str] = None
        ):
        self.name = name
        self.data = data
        self.units = units

    # Getters and setters
    name = create_typed_property('name', str)
    data = create_typed_property('data', requires_shape=True)
    units = create_typed_property('units', str)


class Data:
    def __init__(self,
            signal_name: str = None,
            signal_data = None,
            signal_units: str = None,
            axes: List[Axis] = None
        ):
        self.signal_name = signal_name
        self.signal_data = signal_data
        self.signal_units = signal_units
        self.axes = axes
    
    # Getters and setters
    signal_name = create_typed_property('signal_name', str)
    signal_data = create_typed_property('signal', requires_shape=True)
    signal_units = create_typed_property('signal_units', str)
    axes = create_typed_property_for_list('axes', Axis)
    # an integrity check that assures that the axis and the data are compatible is performed when the nexus file is created using saveNexus