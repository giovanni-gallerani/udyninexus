from udyninexus.classes.Instrument import Instrument
from udyninexus.classes.Source import Source
from udyninexus.utils import create_property_check_type, create_property_check_in_valid_values

from typing import Literal


class Beam(Instrument):
    """
    Represents the characteristics of a beam used in spectroscopy experiments.

    Attributes:
        name_in_nexus (str): Identifier used in the NeXus file. The beam will be saved inside the 'instrument' group under the name 'beam\_\<name_in_nexus\>'.
        beam_type (str): Specify the role of the beam ('pump' or 'probe').
        parameter_reliability (str): Indicates how the beam characteristics were obtained ('measured', 'nominal').
        incident_wavelength (int): Wavelength of the incident beam.
        incident_wavelength_units (str): Units of the incident wavelength ('nm', 'um').
        incident_polarization (int): Polarization value of the incident beam.
        beam_polarization_type (str): Type of beam polarization ('linear', 'circular', 'elliptically', 'unpolarized').
        associated_source (Source): Device that emitted the beam. In the NeXus file the path to the source will be specified in the 'associated_source' NXfield.
    """
    def __init__(self,
            name_in_nexus: str = None,
            beam_type: Literal['pump', 'probe'] = None,
            parameter_reliability: Literal['measured', 'nominal'] = None,
            incident_wavelength: int = None,
            incident_wavelength_units: Literal['nm', 'um'] = None,
            incident_polarization: int = None,
            beam_polarization_type: Literal['linear', 'circular' ,'elliptically', 'unpolarized'] = None,
            associated_source: Source = None
        ):
        super().__init__(name_in_nexus)
        self.parameter_reliability = parameter_reliability
        self.incident_wavelength = incident_wavelength
        self.incident_wavelength_units = incident_wavelength_units
        self.incident_polarization = incident_polarization
        self.beam_polarization_type = beam_polarization_type
        self.associated_source = associated_source
        self.beam_type = beam_type
        
    
    # Getters and setters
    parameter_reliability = create_property_check_in_valid_values('parameter_reliability', ['measured', 'nominal'])
    incident_wavelength = create_property_check_type('incident_wavelength', int)
    incident_wavelength_units = create_property_check_in_valid_values('incident_wavelength_units', ['nm', 'um'])
    incident_polarization = create_property_check_type('incident_polarization', int)
    beam_polarization_type = create_property_check_in_valid_values('beam_polarization_type', ['linear', 'circular' ,'elliptically', 'unpolarized'])
    associated_source = create_property_check_type('associated_source', Source)
    beam_type = create_property_check_in_valid_values('beam_type', ['pump', 'probe'])