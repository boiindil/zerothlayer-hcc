#!/usr/bin/env python3
"""ZEROTHLAYER Basic Usage Example"""

from zerothlayer import GovernanceKernel

def main():
    print("🛡️  ZEROTHLAYER Demo")
    
    kernel = GovernanceKernel(constraints=["no_data_exfiltration"])
    job = kernel.wrap_job(executable="echo 'Hello'", resources={"cpu": 4})
    result = job.execute()
    
    print(f"✅ Job completed: {result['job_id']}")

if __name__ == "__main__":
    main()
