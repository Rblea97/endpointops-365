[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$DeviceCsv,

    [Parameter(Mandatory = $false)]
    [int]$WindowsUpdateSlaDays = 30,

    [Parameter(Mandatory = $false)]
    [datetime]$Now = (Get-Date)
)

$devices = Import-Csv -Path $DeviceCsv
foreach ($device in $devices) {
    $failed = [System.Collections.Generic.List[string]]::new()
    $actions = [System.Collections.Generic.List[string]]::new()

    if ($device.bios_mode -ne 'UEFI') {
        $failed.Add("BIOS mode is $($device.bios_mode)")
        $actions.Add('Set BIOS mode to UEFI before deployment')
    }
    if ($device.secure_boot -ne 'Enabled') {
        $failed.Add("Secure Boot is $($device.secure_boot)")
        $actions.Add('Enable Secure Boot')
    }
    if ($device.tpm_present -ne 'True') {
        $failed.Add('TPM is not present')
        $actions.Add('Verify TPM availability before Intune readiness')
    }
    if ($device.bitlocker_status -notin @('On', 'ExceptionDocumented')) {
        $failed.Add("BitLocker status is $($device.bitlocker_status)")
        $actions.Add('Re-enable BitLocker or document an approved exception')
    }
    $lastUpdate = [datetime]$device.last_windows_update
    if (($Now - $lastUpdate).Days -gt $WindowsUpdateSlaDays) {
        $failed.Add("Windows update age is $(($Now - $lastUpdate).Days) days")
        $actions.Add('Run Windows Update and recheck compliance')
    }
    if ($device.dell_command_update_status -notin @('Current', 'PendingApproved')) {
        $failed.Add("Dell Command Update status is $($device.dell_command_update_status)")
        $actions.Add('Run or approve Dell Command Update before handoff')
    }
    if ([string]::IsNullOrWhiteSpace($device.asset_tag) -or $device.asset_tag -notmatch '^CML-A-\d+$') {
        $failed.Add('Asset tag is missing or not synthetic')
        $actions.Add('Assign a synthetic lab asset tag')
    }
    if ([string]::IsNullOrWhiteSpace($device.serial_number) -or $device.serial_number -notmatch '^SYNTH-DELL-\d{4}$') {
        $failed.Add('Serial number is missing or not synthetic')
        $actions.Add('Use a synthetic serial number before publishing')
    }
    if ($device.device_role -notin @('Production', 'Loaner', 'Staging', 'Retired')) {
        $failed.Add("Unknown device role $($device.device_role)")
        $actions.Add('Set a known lifecycle role')
    }

    [pscustomobject]@{
        DeviceId = $device.device_id
        Status = if ($failed.Count -eq 0 -or $device.device_role -eq 'Retired') { 'Ready' } else { 'NeedsRemediation' }
        DeviceRole = $device.device_role
        FailedChecks = [string[]]$failed
        RecommendedActions = [string[]]$actions
    }
}
