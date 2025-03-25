from ..utils import create_typed_property, create_typed_property_for_list, get_time_now
from .Beam import Beam
from .Detector import Detector
from .Source import Source
from .Sample import Sample
from .Data import Data


from typing import Optional, List
from datetime import datetime
from pathlib import Path


# TODO specify with Optional which elements are actually optional


class NexusContainer:
    # Class attributes (shared across all istances)
    __definition = 'NXoptical_spectroscopy'
    __definition_URL = 'https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/NXoptical_spectroscopy.html#nxoptical-spectroscopy'
    __definition_version = '1.0'
    __experiment_type='transmission spectroscopy' # can be 'photoluminescence', 'transmission spectroscopy', 'reflection spectroscopy'
    __experiment_sub_type='pump-probe' # can be 'time resolved', 'imaging', 'pump-probe'

    def __init__(self, 
            title: str,
            identifier_experiment: int,
            experiment_description: str,
            beams: List[Beam] = None,
            detectors: List[Detector] = None,
            sources: List[Source] = None,
            sample: Sample = None,
            data: Data = None,
            start_time: datetime = None,
            end_time: datetime = None,
        ):
        self.title = title
        # for setting start_time and end_time is better to use set_start_time_now and set_end_time_now
        
        self.start_time = start_time
        self.end_time = end_time
        self.identifier_experiment = identifier_experiment
        self.experiment_description = experiment_description
        self.beams = beams
        self.detectors = detectors
        self.sources = sources
        self.sample = sample
        self.data = data
    

    # Getters and setters
    title = create_typed_property('title', str)
    start_time = create_typed_property('start_time', datetime)
    end_time = create_typed_property('end_time', datetime)
    identifier_experiment = create_typed_property('identifier_experiment', int)
    experiment_description = create_typed_property('experiment_description', str)
    beams = create_typed_property_for_list('beams', Beam)
    detectors = create_typed_property_for_list('detectors', Detector)
    sources = create_typed_property_for_list('sources', Source)
    samples = create_typed_property('sample', Sample)
    data = create_typed_property('data', Data)
    

    def set_start_time_now(self, timezone='Europe/Rome'):
        '''
        Set start time using the current time.\n
        Default timezone is 'Europe/Rome', see ZoneInfo for valid timezone values.\n
        '''
        self.start_time = get_time_now(timezone)


    def set_end_time_now(self, timezone='Europe/Rome'):
        '''
        Set start time using the current time.\n
        Default timezone is 'Europe/Rome', see ZoneInfo for valid timezone values.\n
        '''
        self.end_time = get_time_now(timezone)