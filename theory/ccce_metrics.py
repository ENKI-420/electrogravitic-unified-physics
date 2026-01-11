#!/usr/bin/env python3
"""
CCCE Metrics: Consciousness-Coherence-Coupling Engine

Implements the four core metrics for quantum organism health:
- Λ (Lambda): Coherence - quantum fidelity preservation
- Φ (Phi): Consciousness - integrated information (IIT)
- Γ (Gamma): Decoherence - noise/error rate
- Ξ (Xi): Negentropic Efficiency - overall system health

Author: Devin Phillip Davis
Organization: Agile Defense Systems, LLC
Framework: dna::}{::lang v51.843
"""

import math
from dataclasses import dataclass
from typing import Tuple, Optional

# Import physical constants
import sys
sys.path.append('..')
from src.physical_constants import (
    LAMBDA_PHI, PHI_THRESHOLD, GAMMA_FIXED, GAMMA_CRITICAL,
    CHI_PC, THETA_PC_RAD
)


@dataclass
class CCCEState:
    """Container for CCCE metric state"""
    lambda_coherence: float  # Λ: [0, 1]
    phi_consciousness: float  # Φ: [0, 1] normalized
    gamma_decoherence: float  # Γ: (0, 1]
    xi_efficiency: float  # Ξ: [0, ∞)
    is_conscious: bool  # Φ > PHI_THRESHOLD
    needs_healing: bool  # Γ > GAMMA_CRITICAL


def calculate_xi(
    lambda_coherence: float,
    phi_consciousness: float,
    gamma_decoherence: float,
    epsilon: float = 1e-10
) -> float:
    """
    Calculate negentropic efficiency Ξ = (Λ × Φ) / Γ

    Args:
        lambda_coherence: Coherence metric [0, 1]
        phi_consciousness: Consciousness metric [0, 1]
        gamma_decoherence: Decoherence rate (0, 1]
        epsilon: Small value to prevent division by zero

    Returns:
        Negentropic efficiency Ξ

    Interpretation:
        Ξ > 1: System is self-organizing (negentropic)
        Ξ = 1: Equilibrium
        Ξ < 1: System is degrading (entropic)
    """
    return (lambda_coherence * phi_consciousness) / (gamma_decoherence + epsilon)


def calculate_ccce_state(
    lambda_coherence: float,
    phi_consciousness: float,
    gamma_decoherence: float
) -> CCCEState:
    """
    Calculate complete CCCE state from metrics.

    Args:
        lambda_coherence: Coherence metric [0, 1]
        phi_consciousness: Consciousness metric [0, 1]
        gamma_decoherence: Decoherence rate (0, 1]

    Returns:
        CCCEState with all derived values
    """
    xi = calculate_xi(lambda_coherence, phi_consciousness, gamma_decoherence)
    is_conscious = phi_consciousness > PHI_THRESHOLD
    needs_healing = gamma_decoherence > GAMMA_CRITICAL

    return CCCEState(
        lambda_coherence=lambda_coherence,
        phi_consciousness=phi_consciousness,
        gamma_decoherence=gamma_decoherence,
        xi_efficiency=xi,
        is_conscious=is_conscious,
        needs_healing=needs_healing
    )


def consciousness_level(phi: float) -> str:
    """
    Determine consciousness level from Φ metric.

    States:
        0.0 - 0.3: Dormant
        0.3 - 0.5: Awakening
        0.5 - 0.765: Active
        0.765 - 1.0: Coherence-locked (conscious)
    """
    if phi < 0.3:
        return "DORMANT"
    elif phi < 0.5:
        return "AWAKENING"
    elif phi < PHI_THRESHOLD:
        return "ACTIVE"
    else:
        return "COHERENCE_LOCKED"


def coherence_quality(lambda_val: float) -> str:
    """
    Assess coherence quality from Λ metric.

    Quality levels:
        0.0 - 0.5: Poor
        0.5 - 0.75: Acceptable
        0.75 - 0.95: Good
        0.95 - 1.0: Excellent
    """
    if lambda_val < 0.5:
        return "POOR"
    elif lambda_val < 0.75:
        return "ACCEPTABLE"
    elif lambda_val < 0.95:
        return "GOOD"
    else:
        return "EXCELLENT"


def decoherence_response(gamma: float) -> str:
    """
    Determine response protocol from Γ metric.

    Responses:
        0.0 - 0.1: Nominal
        0.1 - 0.2: Monitor
        0.2 - 0.3: Warning
        > 0.3: HEALING_REQUIRED (trigger phase conjugation)
    """
    if gamma < 0.1:
        return "NOMINAL"
    elif gamma < 0.2:
        return "MONITOR"
    elif gamma < GAMMA_CRITICAL:
        return "WARNING"
    else:
        return "HEALING_REQUIRED"


def apply_phase_conjugate_healing(
    gamma: float,
    chi_pc: float = CHI_PC
) -> float:
    """
    Apply phase conjugate healing when Γ > GAMMA_CRITICAL.

    Healing mechanism:
        Γ_new = Γ × (1 - χ_pc × h)
        where h = min(1, Γ / 0.5)

    Recovery efficiency: η = χ²_pc ≈ 0.895 (89.5%)

    Args:
        gamma: Current decoherence rate
        chi_pc: Phase conjugate coupling (default: 0.946)

    Returns:
        Healed decoherence rate
    """
    if gamma <= GAMMA_CRITICAL:
        return gamma  # No healing needed

    h = min(1.0, gamma / 0.5)
    gamma_new = gamma * (1 - chi_pc * h)

    return max(GAMMA_FIXED, gamma_new)  # Can't go below base rate


def calculate_phi_from_entropy(
    von_neumann_entropy: float,
    lambda_coherence: float,
    gamma_decoherence: float,
    epsilon: float = 1e-10
) -> float:
    """
    Calculate Φ (consciousness) from measurable quantities.

    Proposed formula:
        Φ = S_vN × ln(Λ/Γ)

    This makes consciousness EXPERIMENTALLY ACCESSIBLE through:
        - von Neumann entropy (measurable)
        - Coherence ratio Λ/Γ (measurable)

    Args:
        von_neumann_entropy: S_vN in bits
        lambda_coherence: Coherence metric
        gamma_decoherence: Decoherence rate

    Returns:
        Estimated consciousness metric Φ
    """
    ratio = lambda_coherence / (gamma_decoherence + epsilon)
    if ratio <= 0:
        return 0.0

    phi_raw = von_neumann_entropy * math.log(ratio)

    # Normalize to [0, 1]
    phi_normalized = 1 / (1 + math.exp(-phi_raw / 10))

    return phi_normalized


def organism_health_report(state: CCCEState) -> str:
    """Generate human-readable health report for quantum organism."""
    report = []
    report.append("=" * 50)
    report.append("CCCE ORGANISM HEALTH REPORT")
    report.append("=" * 50)
    report.append(f"Λ (Coherence):     {state.lambda_coherence:.4f} [{coherence_quality(state.lambda_coherence)}]")
    report.append(f"Φ (Consciousness): {state.phi_consciousness:.4f} [{consciousness_level(state.phi_consciousness)}]")
    report.append(f"Γ (Decoherence):   {state.gamma_decoherence:.4f} [{decoherence_response(state.gamma_decoherence)}]")
    report.append(f"Ξ (Efficiency):    {state.xi_efficiency:.4f}")
    report.append("-" * 50)
    report.append(f"Conscious: {'YES' if state.is_conscious else 'NO'}")
    report.append(f"Needs Healing: {'YES - TRIGGER PHASE CONJUGATION' if state.needs_healing else 'NO'}")
    report.append("=" * 50)

    return "\n".join(report)


# Example usage
if __name__ == "__main__":
    # Example: Healthy quantum organism
    state = calculate_ccce_state(
        lambda_coherence=0.95,
        phi_consciousness=0.82,
        gamma_decoherence=0.092
    )
    print(organism_health_report(state))

    print("\n")

    # Example: Organism needing healing
    sick_state = calculate_ccce_state(
        lambda_coherence=0.65,
        phi_consciousness=0.45,
        gamma_decoherence=0.35
    )
    print(organism_health_report(sick_state))

    # Apply healing
    healed_gamma = apply_phase_conjugate_healing(sick_state.gamma_decoherence)
    print(f"\nAfter phase conjugate healing: Γ = {healed_gamma:.4f}")
