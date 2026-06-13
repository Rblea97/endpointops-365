BeforeAll {
    $ScriptPath = Join-Path $PSScriptRoot '../../scripts/powershell/New-PatchRiskReport.ps1'
}

Describe 'New-PatchRiskReport' {
    It 'writes a markdown patch risk report' {
        $out = Join-Path $TestDrive 'patch-report.md'
        & $ScriptPath -DeviceCsv './data/synthetic/devices.csv' -SoftwareCsv './data/synthetic/software_inventory.csv' -VulnerabilityCsv './data/synthetic/vulnerabilities.csv' -OutputPath $out
        Test-Path $out | Should -BeTrue
        (Get-Content $out -Raw) | Should -Match '# Patch Risk Report'
        (Get-Content $out -Raw) | Should -Match 'CVE-SAMPLE-2026'
    }
}
