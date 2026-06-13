# Intune Concepts Mapping

The MVP does not call Intune. It models concepts that map to Intune endpoint administration:

| Lab concept | Intune/M365 concept |
|---|---|
| `intune_readiness` | Device readiness before enrollment or assignment |
| `compliance_state` | Device compliance posture |
| Device role | Device category, assignment targeting, or operational lifecycle |
| Loaner pool | Device group or category for shared/loaner workflows |
| Patch risk queue | Update/remediation prioritization |
| Mock Graph responses | Shape of future Graph-backed automation |

Future live mode must use a disposable tenant and least-privilege Graph permissions. It should be read-only before any write action is added.
