# Graph Permissions

The MVP uses mock Graph responses only.

Future Graph validation should start read-only and use a disposable development tenant with fake users and devices.

## Read-only candidate permissions

| Scenario | Permission type to research before use |
|---|---|
| Read fake users | `User.Read.All` |
| Read fake groups | `Group.Read.All` |
| Read fake devices | `Device.Read.All` |
| Read Intune managed devices | Intune Graph permissions appropriate to the exact endpoint |

Do not add write permissions until a read-only demo is working and documented.

## Public safety rule

Never publish tenant IDs, object IDs, UPNs, group IDs, device IDs, app IDs, secrets, or screenshots from a real tenant. Publish sanitized counts and mocked examples only.
