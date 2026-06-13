from endpointops.scoring import PatchRiskInput, calculate_patch_risk


def test_known_exploited_scores_higher_than_non_exploited():
    base = PatchRiskInput(cvss_base=7.0, epss_percentile=0.50)
    exploited = PatchRiskInput(cvss_base=7.0, epss_percentile=0.50, known_exploited=True)
    assert calculate_patch_risk(exploited) > calculate_patch_risk(base)


def test_critical_internet_exposed_asset_scores_higher():
    standard = PatchRiskInput(cvss_base=6.0, epss_percentile=0.40, asset_criticality="Standard")
    critical = PatchRiskInput(cvss_base=6.0, epss_percentile=0.40, asset_criticality="Critical", internet_exposed=True)
    assert calculate_patch_risk(critical) > calculate_patch_risk(standard)


def test_compensating_control_lowers_score_but_not_below_zero():
    controlled = PatchRiskInput(cvss_base=0.1, epss_percentile=0.01, compensating_control=True)
    assert calculate_patch_risk(controlled) == 0
