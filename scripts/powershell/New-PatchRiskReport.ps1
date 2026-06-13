[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$DeviceCsv,

    [Parameter(Mandatory = $true)]
    [string]$SoftwareCsv,

    [Parameter(Mandatory = $true)]
    [string]$VulnerabilityCsv,

    [Parameter(Mandatory = $true)]
    [string]$OutputPath
)

function ConvertTo-Bool([string]$Value) {
    return $Value -eq 'True'
}

function Get-RiskScore($software, $vuln) {
    $score = ([double]$vuln.cvss_base * 10) + ([double]$vuln.epss_percentile * 25) + 10
    if (ConvertTo-Bool $vuln.known_exploited) { $score += 25 }
    if ($software.asset_criticality -eq 'Critical') { $score += 15 }
    elseif ($software.asset_criticality -eq 'High') { $score += 8 }
    if (ConvertTo-Bool $software.internet_exposed) { $score += 15 }
    if (ConvertTo-Bool $software.compensating_control) { $score -= 10 }
    return [math]::Max(0, [math]::Round($score))
}

$devices = Import-Csv -Path $DeviceCsv | Group-Object -Property device_id -AsHashTable -AsString
$softwareRows = Import-Csv -Path $SoftwareCsv
$vulns = Import-Csv -Path $VulnerabilityCsv | Group-Object -Property software_name -AsHashTable -AsString

$rows = foreach ($software in $softwareRows) {
    if (-not $vulns.ContainsKey($software.software_name)) { continue }
    $vuln = @($vulns[$software.software_name])[0]
    $device = @($devices[$software.device_id])[0]
    [pscustomobject]@{
        DeviceId = $software.device_id
        DeviceRole = $device.device_role
        SoftwareName = $software.software_name
        CveId = $vuln.cve_id
        FixedVersion = $vuln.fixed_version
        KnownExploited = $vuln.known_exploited
        RiskScore = Get-RiskScore $software $vuln
    }
}

$top = @($rows | Sort-Object -Property RiskScore -Descending | Select-Object -First 10)
$lines = [System.Collections.Generic.List[string]]::new()
$lines.Add('# Patch Risk Report')
$lines.Add('')
$lines.Add('Synthetic vulnerability prioritization from endpoint inventory, CVSS/EPSS-style fields, exposure, asset criticality, and compensating controls.')
$lines.Add('')
$lines.Add('| Rank | Device | Role | Software | CVE | Risk | Recommended action |')
$lines.Add('|---:|---|---|---|---|---:|---|')
$rank = 1
foreach ($item in $top) {
    $lines.Add("| $rank | $($item.DeviceId) | $($item.DeviceRole) | $($item.SoftwareName) | $($item.CveId) | $($item.RiskScore) | Update to $($item.FixedVersion) |")
    $rank += 1
}

$parent = Split-Path -Parent $OutputPath
if ($parent) { New-Item -ItemType Directory -Path $parent -Force | Out-Null }
$lines -join "`n" | Set-Content -Path $OutputPath -Encoding utf8
Get-Item -Path $OutputPath
