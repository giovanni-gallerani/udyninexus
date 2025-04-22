class NexusValidationError(Exception):
    """Raised when the NexusContainer fails validation."""
    pass

class NexusSaveError(Exception):
    """Raised when saving to file fails unexpectedly."""
    pass