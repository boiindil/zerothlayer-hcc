# ZEROTHLAYER Deployment Guide

## Quick Deploy (< 1 Hour)

### Step 1: GitHub (15 min)

```bash
cd zerothlayer-v0.1.0
git init
git add .
git commit -m "Initial: ZEROTHLAYER v0.1.0"

# Create repo on GitHub
gh repo create wbrueckner/zerothlayer-hcc --public
git push -u origin main
```

### Step 2: PyPI (20 min)

```bash
# Install tools
pip install build twine

# Build package
python -m build

# Upload (get PyPI account first at pypi.org)
python -m twine upload dist/*
```

### Step 3: Landing Page (15 min)

Go to carrd.co and create:

**Headline:** "Turn Your HPC Cluster into a Compliance Engine"

**Features:**
- Fail-closed governance
- EU AI Act compliant
- China-free certification

**CTA:** `pip install zerothlayer-hcc`

### Step 4: Distribution (10 min)

Post on:
- Reddit r/HPC
- LinkedIn (HPC groups)
- Direct to TensorDyne/Helsing

## Message Template for TensorDyne

```
Subject: ZEROTHLAYER - Open-source HPC governance

Hi Gilles,

You viewed my profile recently. I've converted the ZEROTHLAYER 
framework into a production library:

→ github.com/wbrueckner/zerothlayer-hcc
→ pip install zerothlayer-hcc

If TensorDyne runs HPC workloads needing compliance verification,
you can test it in 30min. MIT licensed base.

Best,
Winfried
brueckner@bw-ruah.de
```

## Enterprise Conversion

When interest comes:

1. Free tier → Let them test
2. Ask questions → "What constraints do you need?"
3. Custom demo → Show their exact use case
4. Pricing → €50K-200K based on scale
5. POC → 2-week trial

## Support

Email: brueckner@bw-ruah.de
ORCID: 0009-0009-0008-5263
DOI: https://doi.org/10.5281/zenodo.14628040
