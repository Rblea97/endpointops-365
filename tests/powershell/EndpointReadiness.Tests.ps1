BeforeAll {
    $ScriptPath = Join-Path $PSScriptRoot '../../scripts/powershell/Invoke-EndpointReadinessCheck.ps1'
}

Describe 'Invoke-EndpointReadinessCheck' {
    It 'returns ready and remediation statuses for synthetic devices' {
        $results = & $ScriptPath -DeviceCsv './data/synthetic/devices.csv' -Now '2026-06-13'
        $results.Count | Should -Be 25
        ($results | Where-Object DeviceId -eq 'CML-LT-001').Status | Should -Be 'Ready'
        ($results | Where-Object DeviceId -eq 'CML-LT-004').Status | Should -Be 'NeedsRemediation'
    }

    It 'records failed checks and recommended actions' {
        $result = (& $ScriptPath -DeviceCsv './data/synthetic/devices.csv' -Now '2026-06-13' | Where-Object DeviceId -eq 'CML-LT-004')
        $result.FailedChecks | Should -Contain 'BIOS mode is Legacy'
        $result.RecommendedActions | Should -Contain 'Set BIOS mode to UEFI before deployment'
    }
}
