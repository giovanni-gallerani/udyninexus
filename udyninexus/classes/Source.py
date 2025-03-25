from ..utils import create_valued_property


from typing import Literal


class Source:
    def __init__(self, type : Literal['Synchrotron X-ray Source', 'Rotating Anode X-ray', 'Fixed Tube X-ray',
                                        'UV Laser', 'Optical Laser', 'Laser', 'Dye-Laser', 'Broadband Tunable Light Source',
                                        'Halogen lamp', 'LED', 'Mercury Cadmium Telluride', 'Deuterium Lamp', 
                                        'Xenon Lamp', 'Globar']):
        self.type = type
        
    
    # Getters and setters
    type = create_valued_property('type', ['Synchrotron X-ray Source', 'Rotating Anode X-ray', 'Fixed Tube X-ray',
                                        'UV Laser', 'Optical Laser', 'Laser', 'Dye-Laser', 'Broadband Tunable Light Source',
                                        'Halogen lamp', 'LED', 'Mercury Cadmium Telluride', 'Deuterium Lamp', 
                                        'Xenon Lamp', 'Globar'])