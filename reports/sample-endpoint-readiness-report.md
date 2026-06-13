# Endpoint Readiness Report

Synthetic report generated from public-safe lab data.

## Summary

- Total devices: 25
- Ready: 12
- Needs remediation: 13
- Loaner devices: 4

## Devices needing remediation

| Device | Role | Failed checks | Recommended actions |
|---|---|---|---|
| CML-LT-002 | Production | Windows update age is 56 days | Run Windows Update and recheck compliance |
| CML-LT-004 | Production | BIOS mode is Legacy; Windows update age is 43 days | Set BIOS mode to UEFI before deployment; Run Windows Update and recheck compliance |
| CML-LT-005 | Production | Secure Boot is Disabled | Enable Secure Boot |
| CML-LT-006 | Production | TPM is not present | Verify TPM availability before Intune readiness |
| CML-LT-007 | Production | BitLocker status is Suspended; Windows update age is 56 days | Re-enable BitLocker or document an approved exception; Run Windows Update and recheck compliance |
| CML-LT-008 | Production | Dell Command Update status is Outdated | Run or approve Dell Command Update before handoff |
| CML-LT-009 | Production | Windows update age is 43 days | Run Windows Update and recheck compliance |
| CML-LT-012 | Production | Windows update age is 56 days | Run Windows Update and recheck compliance |
| CML-LT-014 | Production | Windows update age is 43 days | Run Windows Update and recheck compliance |
| CML-LOANER-001 | Loaner | Secure Boot is Disabled; Windows update age is 56 days | Enable Secure Boot; Run Windows Update and recheck compliance |
| CML-LOANER-002 | Loaner | BitLocker status is Suspended | Re-enable BitLocker or document an approved exception |
| CML-LOANER-003 | Loaner | Windows update age is 43 days; Dell Command Update status is Outdated | Run Windows Update and recheck compliance; Run or approve Dell Command Update before handoff |
| CML-LT-022 | Staging | BIOS mode is Legacy; Windows update age is 56 days | Set BIOS mode to UEFI before deployment; Run Windows Update and recheck compliance |

## Ready devices

- CML-LT-001 (Production)
- CML-LT-003 (Production)
- CML-LT-010 (Production)
- CML-LT-011 (Production)
- CML-LT-013 (Production)
- CML-LT-015 (Production)
- CML-LT-016 (Production)
- CML-LOANER-004 (Loaner)
- CML-LT-021 (Staging)
- CML-LT-023 (Staging)
- CML-LT-024 (Retired)
- CML-LT-025 (Retired)
