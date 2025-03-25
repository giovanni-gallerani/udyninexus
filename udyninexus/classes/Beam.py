from ..utils import create_typed_property, create_valued_property
from .Source import Source


from typing import Optional, Literal

# TODO specify with Optional which elements are actually optional

class Beam:
    def __init__(self,
            name: str = None,
            beam_type: Literal['pump', 'probe'] = None,
            parameter_reliability: Literal['measured', 'nominal'] = None,
            incident_wavelength: int = None,
            incident_wavelength_units: Literal['nm'] = None,
            incident_polarization: int = None,
            beam_polarization_type: Literal['linear', 'circular' ,'elliptically', 'unpolarized'] = None,
            associated_source: Source = None
        ):
        self.name = name
        self.parameter_reliability = parameter_reliability
        self.incident_wavelength = incident_wavelength
        self.incident_wavelength_units = incident_wavelength_units
        self.incident_polarization = incident_polarization
        self.beam_polarization_type = beam_polarization_type
        self.associated_source = associated_source
        self.beam_type = beam_type
        
    
    # Getters and setters
    name = create_typed_property('name', str)
    parameter_reliability = create_valued_property('parameter_reliability', ['measured', 'nominal'])
    incident_wavelength = create_typed_property('incident_wavelength', int)
    incident_wavelength_units = create_valued_property('incident_wavelength_units', ['nm']) # TODO decide what units are possible
    incident_polarization = create_typed_property('incident_polarization', int)
    beam_polarization_type = create_valued_property('beam_polarization_type', ['linear', 'circular' ,'elliptically', 'unpolarized'])
    associated_source = create_typed_property('associated_source', Source)
    beam_type = create_valued_property('beam_type', ['pump', 'probe'])