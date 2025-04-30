from .Instrument import Instrument
from ..utils import create_property_check_in_valid_values

from typing import Literal


class Detector(Instrument):
    def __init__(self,
            name_in_nexus: str = None,
            detector_channel_type : Literal['single-channel', 'multichannel'] = None,
            detector_type: Literal['CCD', 'photomultiplier', 'photodiode', 'avalanche-photodiode', 'streak camera', 'bolometer',
                                    'golay detectors', 'pyroelectric detector', 'deuterated triglycine sulphate'] = None
        ):
        super().__init__(name_in_nexus)
        self.detector_channel_type = detector_channel_type
        self.detector_type = detector_type
        
    
    # Getters and setters
    detector_channel_type = create_property_check_in_valid_values('detector_channel_type', ['single-channel', 'multichannel'])
    detector_type = create_property_check_in_valid_values('detector_type', ['CCD', 'photomultiplier', 'photodiode', 'avalanche-photodiode', 'streak camera', 'bolometer',
                                                            'golay detectors', 'pyroelectric detector', 'deuterated triglycine sulphate'])
    