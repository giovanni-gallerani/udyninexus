from ..utils import create_typed_property, create_valued_property


from typing import Optional, Literal


class Detector:
    def __init__(self,
            name_in_nexus: str = None,
            detector_channel_type : Literal['single-channel', 'multichannel'] = None,
            detector_type: Literal['CCD', 'photomultiplier', 'photodiode', 'avalanche-photodiode', 'streak camera', 'bolometer',
                                    'golay detectors', 'pyroelectric detector', 'deuterated triglycine sulphate', 'other'] = None
        ):
        self.name_in_nexus = name_in_nexus
        self.detector_channel_type = detector_channel_type
        self.detector_type = detector_type
        
    
    # Getters and setters
    name_in_nexus = create_typed_property('name_in_nexus', str)
    detector_channel_type = create_valued_property('detector_channel_type', ['single-channel', 'multichannel'])
    detector_type = create_valued_property('detector_type', ['CCD', 'photomultiplier', 'photodiode', 'avalanche-photodiode', 'streak camera', 'bolometer',
                                                            'golay detectors', 'pyroelectric detector', 'deuterated triglycine sulphate', 'other'])
    