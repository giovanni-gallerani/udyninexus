from ..utils import create_typed_property


class Sample:
    def __init__(self, name: str, sample_id: int):
        self.name = name
        self.sample_id = sample_id
    
    # Getters and setters
    name = create_typed_property('name', str)
    sample_id = create_typed_property('sample_id', int)