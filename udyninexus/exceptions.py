class NexusValidationError(Exception):
    """Raised by write_nexus when the NexusDataContainer fails validation."""
    def __init__(self, message="Invalid NexusDataContainer, the NeXus file cannot be created"):
        super().__init__(message)


class NexusSaveError(Exception):
    """Raised by write_nexus when saving to file fails unexpectedly."""
    def __init__(self, message="An error occoured while trying to save the file"):
        super().__init__(message)