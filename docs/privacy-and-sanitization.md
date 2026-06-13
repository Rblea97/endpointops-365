# Privacy and Sanitization

EndpointOps 365 is designed for public GitHub. Treat privacy as a build requirement, not polish at the end.

## Allowed public data

- Synthetic users under `contoso-mountain-lab.example`
- Synthetic devices such as `CML-LT-001`
- Synthetic serial numbers such as `SYNTH-DELL-0001`
- Mock Graph responses with fake IDs only
- Generated reports from synthetic data
- Runbooks written from scratch

## Never commit

- Employer data
- Real tenant IDs
- Real UPNs, users, groups, or device IDs
- Real serial numbers or asset tags
- Real tickets or ticket wording
- Real BitLocker recovery keys or key IDs
- Hardware hashes
- App registrations, secrets, tokens, or `.env`
- Screenshots from production systems

## Sanitization checklist before each commit

1. Run `gitleaks detect --source .`.
2. Run the project sanitizer tests.
3. Search staged files for private domains or real identifiers.
4. Inspect generated reports and screenshots manually.
5. Commit only synthetic or explicitly mocked output.

## Microsoft tenant boundary

The MVP runs offline. Future Graph or Intune examples must be dry-run by default and only target disposable development tenants with fake users and fake devices.
