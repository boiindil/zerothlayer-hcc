"""
Supply-chain verification for hardware components.
"""

from typing import List, Dict, Any
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Component:
    """Hardware component."""
    component_id: str
    type: str
    manufacturer: str
    origin_country: str
    manufacture_date: str
    certifications: List[str]


@dataclass
class SupplyChainRecord:
    """Complete supply chain record."""
    components: List[Component]
    verified: bool
    verification_date: str
    certificate_id: str = None


class SupplyChainVerifier:
    """Verifies supply chain integrity."""
    
    def __init__(self):
        self.banned_countries = ["CN", "PRC", "HK", "RU", "KP"]
        self.trusted_manufacturers = [
            "Intel", "AMD", "NVIDIA", "Micron"
        ]
    
    def verify_component(self, component: Component) -> tuple:
        """Verify single component."""
        if component.origin_country in self.banned_countries:
            return False, f"Banned origin: {component.origin_country}"
        
        return True, "Component verified"
    
    def verify_supply_chain(self, components: List[Component]):
        """Verify entire supply chain."""
        all_verified = True
        
        for component in components:
            is_verified, reason = self.verify_component(component)
            if not is_verified:
                all_verified = False
        
        record = SupplyChainRecord(
            components=components,
            verified=all_verified,
            verification_date=datetime.utcnow().isoformat(),
            certificate_id=self._generate_certificate_id() if all_verified else None
        )
        
        return record
    
    def _generate_certificate_id(self) -> str:
        import uuid
        return f"SC-{uuid.uuid4().hex[:12].upper()}"
    
    def export_china_free_certificate(self, record: SupplyChainRecord) -> Dict[str, Any]:
        """Export China-free certificate."""
        if not record.verified:
            raise ValueError("Cannot certify unverified supply chain")
        
        return {
            "certificate_type": "China-Free Supply Chain",
            "certificate_id": record.certificate_id,
            "issued_date": record.verification_date,
            "components_count": len(record.components),
            "attestation": "All components verified free of PRC origin"
        }
