from ..utils import create_typed_property, create_valued_property


from typing import Optional, Literal


class Detector:
    def __init__(self,
            detector_channel_type : Literal['single-channel', 'multichannel'],
            detector_type: Literal['CCD', 'photomultiplier', 'photodiode', 'avalanche-photodiode', 'streak camera', 'bolometer',
                                    'golay detectors', 'pyroelectric detector', 'deuterated triglycine sulphate', 'other']
        ):
        self.detector_channel_type = detector_channel_type
        self.detector_type = detector_type
        
    
    # Getters and setters
    detector_channel_type = create_valued_property('detector_channel_type', ['single-channel', 'multichannel'])
    detector_type = create_valued_property('detector_type', ['CCD', 'photomultiplier', 'photodiode', 'avalanche-photodiode', 'streak camera', 'bolometer',
                                                            'golay detectors', 'pyroelectric detector', 'deuterated triglycine sulphate', 'other'])
    