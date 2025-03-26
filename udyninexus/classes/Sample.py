from ..utils import create_typed_property

# TODO specify with Optional which elements are actually optional

class Sample:
    def __init__(self,
        name: str = None,
        sample_id: int = None
        ):
        self.name = name
        self.sample_id = sample_id
    
    # Getters and setters
    name = create_typed_property('name', str)
    sample_id = create_typed_property('sample_id', int)