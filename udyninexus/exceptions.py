class NexusValidationError(Exception):
    """Raised by write_nexus when the NexusContainer fails validation."""
    pass

class NexusSaveError(Exception):
    """Raised by write_nexus when saving to file fails unexpectedly."""
    pass