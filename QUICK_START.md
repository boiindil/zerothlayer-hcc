# ZEROTHLAYER Quick Start

## Installation

```bash
pip install zerothlayer-hcc
```

## 30-Second Demo

```python
from zerothlayer import GovernanceKernel

# Create kernel with constraints
kernel = GovernanceKernel(
    constraints=["no_data_exfiltration"]
)

# Wrap your job
job = kernel.wrap_job(
    executable="./train_model.sh",
    resources={"gpu": 8, "memory": "512GB"}
)

# Execute with governance
result = job.execute()  # Fail-closed on ambiguity!

# Get certificate
print(f"Job: {result['job_id']}")
print(f"Status: {result['status']}")
print(f"Certificate: {result['certificate']}")
```

## What Just Happened?

1. **Pre-execution:** All constraints validated
2. **During execution:** Monitored in real-time
3. **Post-execution:** Cryptographic certificate generated

## Next Steps

- **Supply-chain verification:** See examples/production_deployment.py
- **EU AI Act compliance:** See docs/EU_AI_ACT.md
- **SLURM integration:** See zerothlayer/integrations/slurm_connector.py

## Enterprise Features

Need hardware attestation, custom constraints, or 24/7 support?

Contact: brueckner@bw-ruah.de
Pricing: €50K-200K/year per datacenter
