# ZEROTHLAYER_HCC 🛡️

**Hardware-Governance for High-Stakes Computing**

Author: Winfried Brueckner (ORCID: 0009-0009-0008-5263)
DOI: https://doi.org/10.5281/zenodo.14628040

## Installation

```bash
pip install zerothlayer-hcc
```

## Quick Start

```python
from zerothlayer import GovernanceKernel

kernel = GovernanceKernel(constraints=["no_data_exfiltration"])
job = kernel.wrap_job(executable="./train.sh", resources={"gpu": 8})
result = job.execute()  # Fail-closed on ambiguity!
```

## Features

- ✅ Fail-Closed Governance
- ✅ Tamper-Evident Audits  
- ✅ China-Free Certification
- ✅ EU AI Act Compliance
- ✅ HPC Integration (SLURM/K8s)

## Contact

Email: brueckner@bw-ruah.de
Web: https://bw-ruah.de
