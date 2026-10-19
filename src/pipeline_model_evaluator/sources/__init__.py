"""Source intake with retained intermediate records and line evidence."""

from .intake import inspect_sources
from .records import IntakeResult

__all__ = ["IntakeResult", "inspect_sources"]
