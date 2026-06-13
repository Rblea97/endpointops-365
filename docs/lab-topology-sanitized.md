# Sanitized Lab Topology

Phase 2 performed read-only host discovery to identify VM platforms and lab assets that could later validate EndpointOps 365 against real Windows/Entra behavior.

## Public-safe findings

| Area | Sanitized result |
|---|---|
| Host OS | Windows 11 Pro |
| Hardware virtualization/hypervisor | Present |
| Docker Desktop / WSL2 | Available and used for the Phase 1 dashboard demo |
| Hyper-V PowerShell inventory | No conventional VM inventory was visible from the current session |
| VirtualBox inventory | No `VBoxManage` inventory was visible from the current session |
| VMware inventory | No `.vmx` files were found in common user/shared VM folders |
| Real Entra/Intune validation | Not performed in Phase 2 |

## Interpretation

The public repo is ready for VM validation, but this read-only pass did not discover the existing Entra-related VMs the user mentioned. They may be stored outside common paths, managed by a platform not exposed to this shell, or require a different/elevated inventory method.

## Public/private boundary

Raw host details are stored only under `private/`, which is ignored by Git. This public document intentionally omits hostname, username, exact local paths, tenant identifiers, device IDs, serial numbers, screenshots, and VM-specific private details.

## Next phase boundary

Phase 3 should not create or modify VMs yet. It should first identify the actual VM platform/path with the user's input, then add a private export workflow and a sanitized evidence process.
