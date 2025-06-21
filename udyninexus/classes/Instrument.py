from udyninexus.utils import create_property_check_type


class Instrument:
    """
    Base class for an istrument used in spectroscopy experiments, all the instrument inherit from this class.

    Attributes:
        name_in_nexus (str): Identifier used in the NeXus file. The specific instrument will be saved inside the 'instrument' group under the name '\<type_of_instrument_instance\>\_\<name_in_nexus\>'.
    """
    def __init__(self, 
            name_in_nexus: str = None
        ):
        self.name_in_nexus = name_in_nexus

    # Getters and setters
    name_in_nexus = create_property_check_type('name_in_nexus', str)