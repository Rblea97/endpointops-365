# Data Model

## Devices

`data/synthetic/devices.csv` represents staged, production, loaner, and retired Windows endpoints. Key fields include BIOS mode, Secure Boot, TPM presence, BitLocker status, update age, Dell Command Update status, readiness, compliance, and lifecycle state.

## Users

`data/synthetic/users.csv` contains fake `.example` users and Entra-style group assignments.

## Software inventory

`data/synthetic/software_inventory.csv` maps software packages to devices and adds exposure, criticality, and compensating control fields for scoring.

## Vulnerabilities

`data/synthetic/vulnerabilities.csv` uses `CVE-SAMPLE-*` identifiers for MVP safety. It includes CVSS-like and EPSS-like fields, known-exploited flags, patch availability, and SLA days.

## Tickets

`data/synthetic/tickets.csv` provides sample remediation work items generated from synthetic endpoint conditions.
