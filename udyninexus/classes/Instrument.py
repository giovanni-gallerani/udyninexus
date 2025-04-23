from ..utils import create_property_check_type

class Instrument:
    def __init__(self, 
            name_in_nexus: str = None
        ):
        self.name_in_nexus = name_in_nexus

    # Getters and setters
    name_in_nexus = create_property_check_type('name_in_nexus', str)