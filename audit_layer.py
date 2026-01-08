"""
Audit Layer - Immutable audit trails.
"""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from datetime import datetime
import hashlib
import json


@dataclass
class AuditEvent:
    """Single audit event."""
    timestamp: str
    event_type: str
    details: Dict[str, Any]
    hash_prev: str
    signature: Optional[str] = None
    
    def compute_hash(self) -> str:
        """Compute cryptographic hash."""
        event_data = {
            "timestamp": self.timestamp,
            "event_type": self.event_type,
            "details": self.details,
            "hash_prev": self.hash_prev
        }
        event_json = json.dumps(event_data, sort_keys=True)
        return hashlib.sha256(event_json.encode()).hexdigest()


@dataclass
class AuditTrail:
    """Complete audit trail."""
    job_id: str
    policy_name: str
    events: List[AuditEvent] = field(default_factory=list)
    
    def add_event(self, event_type: str, details: Dict[str, Any]):
        """Add event to trail."""
        hash_prev = (
            self.events[-1].compute_hash() if self.events
            else "genesis"
        )
        
        event = AuditEvent(
            timestamp=datetime.utcnow().isoformat(),
            event_type=event_type,
            details=details,
            hash_prev=hash_prev
        )
        
        self.events.append(event)
        return event
    
    def verify_integrity(self) -> bool:
        """Verify trail hasn't been tampered with."""
        if not self.events:
            return True
        
        for i in range(1, len(self.events)):
            expected = self.events[i-1].compute_hash()
            actual = self.events[i].hash_prev
            
            if expected != actual:
                return False
        
        return True
    
    def export_certificate(self) -> Dict[str, Any]:
        """Export as certificate."""
        return {
            "job_id": self.job_id,
            "policy": self.policy_name,
            "event_count": len(self.events),
            "integrity_verified": self.verify_integrity(),
            "exported_at": datetime.utcnow().isoformat()
        }


class AuditLayer:
    """Manages audit trails."""
    
    def __init__(self):
        self.trails = {}
    
    def create_trail(self, job_id: str, policy_name: str):
        """Create new audit trail."""
        trail = AuditTrail(job_id=job_id, policy_name=policy_name)
        self.trails[job_id] = trail
        trail.add_event("trail_created", {"policy": policy_name})
        return trail
    
    @staticmethod
    def export_certificate(job):
        """Export certificate for a job."""
        return job.audit_trail.export_certificate()
