# Custom Exceptions

class ProfileManagerError(Exception):
    """Base exception for the Profile Manager application."""
    pass

class DatabaseConnectionError(ProfileManagerError):
    """Raised when there's an error connecting to the database."""
    pass

class EncryptionError(ProfileManagerError):
    """Raised when there's an error during encryption or decryption."""
    pass

class APIConnectionError(ProfileManagerError):
    """Raised when there's an error connecting to an external API."""
    pass

class ProfileNotFoundError(ProfileManagerError):
    """Raised when a specific profile is not found."""
    pass

# Error Handling Utilities

def handle_error(error):
    """
    A generic error handler function to process exceptions.
    It can be expanded to log errors, send notifications, or perform other tasks.
    """
    if isinstance(error, DatabaseConnectionError):
        return "Error connecting to the database."
    elif isinstance(error, EncryptionError):
        return "Error during encryption or decryption."
    elif isinstance(error, APIConnectionError):
        return "Error connecting to the external API."
    elif isinstance(error, ProfileNotFoundError):
        return "The specified profile was not found."
    else:
        # A generic error message for unexpected exceptions
        return "An unexpected error occurred. Please try again later."

# Future error-handling utilities can be added below
 
