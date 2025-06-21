from udyninexus.utils import create_property_check_type


class Sample:
    """
    Represents the characteristics of the sample used in a spectroscopy experiment.

    Attributes:
        name (str): Name of the sample.
        sample_id (int): Identifier of the sample used inside the laboratories (Sample ID in LabLogbook).
    """
    def __init__(self,
        name: str = None,
        sample_id: int = None
        ):
        self.name = name
        self.sample_id = sample_id
    
    # Getters and setters
    name = create_property_check_type('name', str)
    sample_id = create_property_check_type('sample_id', int)