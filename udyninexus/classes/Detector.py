from udyninexus.classes.Instrument import Instrument
from udyninexus.utils import create_property_check_in_valid_values

from typing import Literal


class Detector(Instrument):
    """
    Represents the characteristics of a detector used in spectroscopy experiments.

    Attributes:
        name_in_nexus (str): Identifier used in the NeXus file. The detector will be saved inside the 'instrument' group under the name 'detector\_\<name_in_nexus\>'.
        detector_channel_type (str): Type of detector based on the number of channels ('single-channel' or 'multichannel').
        detector_type (str): Type of detector ('CCD', 'photomultiplier', 'photodiode', 'avalanche-photodiode', 'streak camera', 'bolometer', 'golay detectors', 'pyroelectric detector', 'deuterated triglycine sulphate').
    """
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
    