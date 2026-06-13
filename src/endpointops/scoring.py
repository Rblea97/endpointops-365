from __future__ import annotations

from dataclasses import dataclass

KNOWN_EXPLOITED_BONUS = 25
CRITICAL_ASSET_BONUS = 15
HIGH_ASSET_BONUS = 8
INTERNET_EXPOSED_BONUS = 15
PATCH_AGE_BONUS = 10
COMPENSATING_CONTROL_CREDIT = 10


@dataclass(frozen=True)
class PatchRiskInput:
    cvss_base: float
    epss_percentile: float
    known_exploited: bool = False
    asset_criticality: str = "Standard"
    internet_exposed: bool = False
    patch_age_bonus: bool = False
    compensating_control: bool = False


def calculate_patch_risk(item: PatchRiskInput) -> int:
    score = (item.cvss_base * 10) + (item.epss_percentile * 25)
    if item.known_exploited:
        score += KNOWN_EXPLOITED_BONUS
    if item.asset_criticality.lower() == "critical":
        score += CRITICAL_ASSET_BONUS
    elif item.asset_criticality.lower() == "high":
        score += HIGH_ASSET_BONUS
    if item.internet_exposed:
        score += INTERNET_EXPOSED_BONUS
    if item.patch_age_bonus:
        score += PATCH_AGE_BONUS
    if item.compensating_control:
        score -= COMPENSATING_CONTROL_CREDIT
    return max(0, round(score))
