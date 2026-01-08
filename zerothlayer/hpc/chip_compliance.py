"""
Chip-level compliance verification.
"""

from typing import List
from dataclasses import dataclass


@dataclass
class ChipSpec:
    """Hardware chip specification."""
    vendor: str
    model: str
    firmware_version: str
    security_features: List[str]
    origin_country: str


class ChipCompliance:
    """Hardware-level governance for HPC chips."""
    
    def __init__(self):
        self.approved_vendors = ["Intel", "AMD", "NVIDIA", "ARM"]
        self.banned_origins = ["CN", "PRC", "RU"]
        self.required_security_features = ["SGX", "SEV", "TrustZone"]
    
    def verify_chip(self, chip_spec: ChipSpec) -> tuple:
        """Verify a chip meets compliance requirements."""
        if chip_spec.vendor not in self.approved_vendors:
            return False, f"Unapproved vendor: {chip_spec.vendor}"
        
        if chip_spec.origin_country in self.banned_origins:
            return False, f"Banned origin: {chip_spec.origin_country}"
        
        has_security = any(
            feature in chip_spec.security_features
            for feature in self.required_security_features
        )
        
        if not has_security:
            return False, "No required security features present"
        
        return True, "Chip compliant"
