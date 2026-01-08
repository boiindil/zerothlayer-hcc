"""Custom exceptions for ZEROTHLAYER."""

class ZeroTHLAYERException(Exception):
    """Base exception."""
    pass

class GovernanceViolation(ZeroTHLAYERException):
    """Governance constraint violated."""
    pass

class AmbiguityDetected(ZeroTHLAYERException):
    """Ambiguity detected (fail-closed)."""
    pass
