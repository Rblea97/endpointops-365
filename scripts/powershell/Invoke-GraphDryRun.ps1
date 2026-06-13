[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$MockResponseDir
)

$usersPath = Join-Path $MockResponseDir 'users.json'
$groupsPath = Join-Path $MockResponseDir 'groups.json'
$devicesPath = Join-Path $MockResponseDir 'devices.json'

[pscustomobject]@{
    Mode = 'DryRun'
    Users = (Get-Content $usersPath -Raw | ConvertFrom-Json).value.Count
    Groups = (Get-Content $groupsPath -Raw | ConvertFrom-Json).value.Count
    Devices = (Get-Content $devicesPath -Raw | ConvertFrom-Json).value.Count
    Note = 'Mock Graph responses only. No tenant calls were made.'
}
