# Offboarding Device Return

## Purpose

Track returned devices through account/device separation, data handling, update checks, and lifecycle state changes using synthetic records.

## Inputs

- Synthetic device/user/ticket records
- Generated readiness or patch-risk reports
- Approved lab-only notes

## Steps

1. Confirm the record uses synthetic identifiers only.
2. Review the current lifecycle or remediation state.
3. Apply the checklist relevant to the scenario.
4. Record the result in a generated report or sample ticket.
5. Escalate only when an exception blocks readiness or SLA completion.

## Acceptance criteria

- Required fields are present.
- The action is traceable to a synthetic record.
- The report contains no private tenant, endpoint, user, ticket, serial, or BitLocker data.

## Public safety note

This runbook is written for a public portfolio lab. Do not copy employer process text, screenshots, exports, or identifiers into this repository.
