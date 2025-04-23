from ..utils import create_property_check_type, create_property_check_in_valid_values, create_property_check_type_for_lists, get_time_now
from .Beam import Beam
from .Detector import Detector
from .Source import Source
from .Sample import Sample
from .Data import Data


from typing import List, Literal
from datetime import datetime


class NexusContainer:

    def __init__(self, 
            title: str = None,
            identifier_experiment: int = None,
            experiment_type: Literal['photoluminescence', 'transmission spectroscopy', 'reflection spectroscopy'] = None,
            experiment_sub_type: Literal['time resolved', 'imaging', 'pump-probe'] = None,
            experiment_description: str = None,
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
        self.experiment_type = experiment_type
        self.experiment_sub_type = experiment_sub_type
        self.beams = beams
        self.detectors = detectors
        self.sources = sources
        self.sample = sample
        self.data = data
    

    # Getters and setters
    title = create_property_check_type('title', str)
    start_time = create_property_check_type('start_time', datetime)
    end_time = create_property_check_type('end_time', datetime)
    identifier_experiment = create_property_check_type('identifier_experiment', int)
    experiment_description = create_property_check_type('experiment_description', str)
    experiment_type = create_property_check_in_valid_values('experiment_type', ['photoluminescence', 'transmission spectroscopy', 'reflection spectroscopy'])
    experiment_sub_type = create_property_check_in_valid_values('experiment_sub_type', ['time resolved', 'imaging', 'pump-probe'])
    beams = create_property_check_type_for_lists('beams', Beam)
    detectors = create_property_check_type_for_lists('detectors', Detector)
    sources = create_property_check_type_for_lists('sources', Source)
    samples = create_property_check_type('sample', Sample)
    data = create_property_check_type('data', Data)
    

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