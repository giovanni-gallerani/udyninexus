from udyninexus.classes.Instrument import Instrument
from udyninexus.utils import create_property_check_in_valid_values

from typing import Literal


class Source(Instrument):
    """
    Represents the characteristics of a source emitting a beam used in spectroscopy experiments.

    Attributes:
        name_in_nexus (str): Identifier used in the NeXus file. The source will be saved inside the 'instrument' group under the name 'source\_\<name_in_nexus\>'.
        type (str): Type of source ('Synchrotron X-ray Source', 'Rotating Anode X-ray', 'Fixed Tube X-ray', 'UV Laser', 'Optical Laser', 'Laser', 'Dye-Laser',\
              'Broadband Tunable Light Source', 'Halogen lamp', 'LED', 'Mercury Cadmium Telluride', 'Deuterium Lamp', 'Xenon Lamp', 'Globar').
    """
    def __init__(self,
            name_in_nexus: str = None,
            type: Literal['Synchrotron X-ray Source', 'Rotating Anode X-ray', 'Fixed Tube X-ray',
                                            'UV Laser', 'Optical Laser', 'Laser', 'Dye-Laser', 'Broadband Tunable Light Source',
                                            'Halogen lamp', 'LED', 'Mercury Cadmium Telluride', 'Deuterium Lamp', 
                                            'Xenon Lamp', 'Globar'] = None
        ):
        super().__init__(name_in_nexus)
        self.type = type
        
    
    # Getters and setters
    type = create_property_check_in_valid_values('type', ['Synchrotron X-ray Source', 'Rotating Anode X-ray', 'Fixed Tube X-ray',
                                        'UV Laser', 'Optical Laser', 'Laser', 'Dye-Laser', 'Broadband Tunable Light Source',
                                        'Halogen lamp', 'LED', 'Mercury Cadmium Telluride', 'Deuterium Lamp', 
                                        'Xenon Lamp', 'Globar'])