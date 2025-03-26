from ..utils import create_typed_property, create_typed_property_for_list


from typing import Optional, List


# TODO specify with Optional which elements are actually optional


class Axis:
    def __init__(self,
            name: str,
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
            signal = None,
            axes: List[Axis] = None
        ):
        self.signal = signal
        self.axes = axes
    
    # Getters and setters
    signal = create_typed_property('signal', requires_shape=True)
    axes = create_typed_property_for_list('axes', Axis)
    # an integrity check that assures that the axis and the data are compatible is performed when the nexus file is created using saveNexus