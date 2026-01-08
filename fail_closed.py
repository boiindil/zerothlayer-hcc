"""
Fail-Closed Handler - Safe shutdown on ambiguity.
"""

from typing import Dict, Any
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class FailClosedHandler:
    """Implements fail-closed semantics."""
    
    def __init__(self):
        self.halt_log = []
    
    def halt_execution(
        self,
        reason: str,
        context: Dict[str, Any],
        metadata: Dict[str, Any] = None
    ):
        """Halt execution with fail-closed semantics."""
        halt_record = {
            "timestamp": datetime.utcnow().isoformat(),
            "reason": reason,
            "context": context,
            "metadata": metadata or {}
        }
        
        self.halt_log.append(halt_record)
        logger.critical(f"FAIL-CLOSED: {reason}")
