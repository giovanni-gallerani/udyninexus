from ..utils import create_property_check_type

# TODO specify with Optional which elements are actually optional

class Sample:
    def __init__(self,
        name: str = None,
        sample_id: int = None
        ):
        self.name = name
        self.sample_id = sample_id
    
    # Getters and setters
    name = create_property_check_type('name', str)
    sample_id = create_property_check_type('sample_id', int)