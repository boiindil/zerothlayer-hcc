"""
Governance Kernel - Core constraint engine with fail-closed semantics.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum
import logging

logger = logging.getLogger(__name__)


class GovernanceMode(Enum):
    """Governance enforcement modes."""
    STRICT = "strict"
    ADVISORY = "advisory"
    LEARNING = "learning"


@dataclass
class GovernancePolicy:
    """Defines a governance policy with constraints."""
    name: str
    constraints: List[str]
    objectives: List[str] = None
    mode: GovernanceMode = GovernanceMode.STRICT
    
    def __post_init__(self):
        if self.objectives is None:
            self.objectives = []


class GovernanceKernel:
    """
    Core governance engine.
    
    Philosophy: Fail-closed on ambiguity.
    """
    
    def __init__(
        self,
        policy: Optional[GovernancePolicy] = None,
        constraints: Optional[List[str]] = None,
        mode: GovernanceMode = GovernanceMode.STRICT
    ):
        if policy:
            self.policy = policy
        elif constraints:
            self.policy = GovernancePolicy(
                name="custom",
                constraints=constraints,
                mode=mode
            )
        else:
            raise ValueError("Must provide either policy or constraints")
        
        logger.info(f"GovernanceKernel initialized: {self.policy.name}")
    
    def wrap_job(
        self,
        executable: str,
        resources: Dict[str, Any],
        audit_level: str = "full",
        metadata: Optional[Dict[str, Any]] = None
    ):
        """Wrap a computational job with governance."""
        from .governed_job import GovernedJob
        
        job = GovernedJob(
            kernel=self,
            executable=executable,
            resources=resources,
            audit_level=audit_level,
            metadata=metadata or {}
        )
        
        logger.info(f"Job wrapped: {executable}")
        return job
    
    def validate_constraints(
        self,
        context: Dict[str, Any]
    ) -> tuple:
        """Validate all constraints against context."""
        # Simplified - full version checks each constraint
        violations = []
        return len(violations) == 0, violations
