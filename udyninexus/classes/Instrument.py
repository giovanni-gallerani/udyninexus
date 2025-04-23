from ..utils import create_typed_property

class Instrument:
    def __init__(self, 
            name_in_nexus: str = None
        ):
        self.name_in_nexus = name_in_nexus

    # Getters and setters
    name_in_nexus = create_typed_property('name_in_nexus', str)