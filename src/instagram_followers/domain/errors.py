## @file errors.py
#  @brief Errors raised by the business rules.


## @brief Raised when a required credential is not set in the environment.
class MissingCredentialsError(RuntimeError):
    pass
