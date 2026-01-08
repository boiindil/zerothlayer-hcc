"""
ZEROTHLAYER_HCC - Hardware Governance for High-Stakes Computing

Fail-closed governance constraints for HPC workloads with tamper-evident
audit trails and compliance verification.

Author: Winfried Brueckner (ORCID: 0009-0009-0008-5263)
License: MIT
DOI: https://doi.org/10.5281/zenodo.14628040
"""

__version__ = "0.1.1"
__author__ = "Winfried Brueckner"
__email__ = "brueckner@bw-ruah.de"
__license__ = "MIT"

# Core governance components
from .core.governance_kernel import GovernanceKernel, GovernancePolicy, GovernanceMode
from .core.audit_layer import AuditLayer, AuditEvent
from .core.fail_closed import FailClosedHandler
from .core.governed_job import GovernedJob

# HPC-specific components
from .hpc.chip_compliance import ChipCompliance, ChipSpec
from .hpc.supply_chain import SupplyChainVerifier, Component

__all__ = [
    # Core
    "GovernanceKernel",
    "GovernancePolicy",
    "GovernanceMode",
    "AuditLayer",
    "AuditEvent",
    "FailClosedHandler",
    "GovernedJob",
    # HPC
    "ChipCompliance",
    "ChipSpec",
    "SupplyChainVerifier",
    "Component",
]
