[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$DeviceCsv,

    [Parameter(Mandatory = $true)]
    [string]$OutputPath,

    [Parameter(Mandatory = $false)]
    [datetime]$Now = (Get-Date)
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$checkScript = Join-Path $scriptDir 'Invoke-EndpointReadinessCheck.ps1'
$results = & $checkScript -DeviceCsv $DeviceCsv -Now $Now

$ready = @($results | Where-Object Status -eq 'Ready')
$needs = @($results | Where-Object Status -eq 'NeedsRemediation')
$loaners = @($results | Where-Object DeviceRole -eq 'Loaner')

$lines = [System.Collections.Generic.List[string]]::new()
$lines.Add('# Endpoint Readiness Report')
$lines.Add('')
$lines.Add('Synthetic report generated from public-safe lab data.')
$lines.Add('')
$lines.Add('## Summary')
$lines.Add('')
$lines.Add("- Total devices: $($results.Count)")
$lines.Add("- Ready: $($ready.Count)")
$lines.Add("- Needs remediation: $($needs.Count)")
$lines.Add("- Loaner devices: $($loaners.Count)")
$lines.Add('')
$lines.Add('## Devices needing remediation')
$lines.Add('')
$lines.Add('| Device | Role | Failed checks | Recommended actions |')
$lines.Add('|---|---|---|---|')
foreach ($item in $needs) {
    $lines.Add("| $($item.DeviceId) | $($item.DeviceRole) | $($item.FailedChecks -join '; ') | $($item.RecommendedActions -join '; ') |")
}
$lines.Add('')
$lines.Add('## Ready devices')
$lines.Add('')
foreach ($item in $ready) {
    $lines.Add("- $($item.DeviceId) ($($item.DeviceRole))")
}

$parent = Split-Path -Parent $OutputPath
if ($parent) { New-Item -ItemType Directory -Path $parent -Force | Out-Null }
$lines -join "`n" | Set-Content -Path $OutputPath -Encoding utf8
Get-Item -Path $OutputPath
