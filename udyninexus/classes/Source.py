from ..utils import create_typed_property, create_valued_property


from typing import Literal


# TODO specify with Optional which elements are actually optional


class Source:
    def __init__(self,
            name_in_nexus: str = None,
            type: Literal['Synchrotron X-ray Source', 'Rotating Anode X-ray', 'Fixed Tube X-ray',
                                            'UV Laser', 'Optical Laser', 'Laser', 'Dye-Laser', 'Broadband Tunable Light Source',
                                            'Halogen lamp', 'LED', 'Mercury Cadmium Telluride', 'Deuterium Lamp', 
                                            'Xenon Lamp', 'Globar'] = None
        ):
        self.type = type
        self.name_in_nexus = name_in_nexus
        
    
    # Getters and setters
    name_in_nexus = create_typed_property('name_in_nexus', str)
    type = create_valued_property('type', ['Synchrotron X-ray Source', 'Rotating Anode X-ray', 'Fixed Tube X-ray',
                                        'UV Laser', 'Optical Laser', 'Laser', 'Dye-Laser', 'Broadband Tunable Light Source',
                                        'Halogen lamp', 'LED', 'Mercury Cadmium Telluride', 'Deuterium Lamp', 
                                        'Xenon Lamp', 'Globar'])