"""
Governed Job - Wrapper for computational workloads.
"""

from typing import Dict, Any, Optional
import uuid
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class GovernedJob:
    """A computational job wrapped with governance."""
    
    def __init__(
        self,
        kernel,
        executable: str,
        resources: Dict[str, Any],
        audit_level: str = "full",
        metadata: Optional[Dict[str, Any]] = None
    ):
        self.kernel = kernel
        self.executable = executable
        self.resources = resources
        self.audit_level = audit_level
        self.metadata = metadata or {}
        
        self.job_id = str(uuid.uuid4())
        self.status = "initialized"
        
        # Create audit trail
        from .audit_layer import AuditLayer
        audit_layer = AuditLayer()
        self.audit_trail = audit_layer.create_trail(
            self.job_id,
            self.kernel.policy.name
        )
    
    def execute(self) -> Dict[str, Any]:
        """Execute job with governance."""
        logger.info(f"Executing: {self.job_id}")
        
        try:
            # Pre-execution check
            self._pre_execution_check()
            
            # Execute
            self.status = "running"
            self.audit_trail.add_event(
                "execution_started",
                {"executable": self.executable}
            )
            
            # Mock execution
            self.result = {"exit_code": 0, "stdout": "Success"}
            
            self.status = "completed"
            self.audit_trail.add_event(
                "execution_completed",
                {"result": self.result}
            )
            
            return {
                "job_id": self.job_id,
                "status": self.status,
                "certificate": self.audit_trail.export_certificate()
            }
        
        except Exception as e:
            self.status = "failed"
            logger.error(f"Job failed: {e}")
            raise
    
    def _pre_execution_check(self):
        """Validate constraints."""
        context = {
            "resources": self.resources,
            "metadata": self.metadata
        }
        
        is_valid, violations = self.kernel.validate_constraints(context)
        
        if not is_valid:
            raise Exception(f"Constraint violations: {violations}")
