class NexusValidationError(Exception):
    """Raised when the NexusContainer fails validation."""
    pass

class NexusSaveError(Exception):
    """Raised by write_nexus when saving the NeXus file fails unexpectedly."""
    pass