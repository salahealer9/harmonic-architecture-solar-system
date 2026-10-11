"""SRHF-A0-01: frozen arithmetic specification, not a dynamical model.

Uses ONLY the rounded semi-major-axis observations from the v3.0 manuscript.
The listed Earth observation is also the exact 1 AU model-normalisation anchor.
Harmonia has no observed radius and is NEVER an observational score target.
"""

from __future__ import annotations

import math
import numpy as np

A = math.sqrt(2.0)
B = A + 1.0
C = 2.0 * A - 1.0
D = A - 1.0

BODY_ORDER = (
    "Mercury", "Venus", "Earth", "Mars", "Harmonia",
    "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto",
)
OBSERVED_AU = {
    "Mercury": 0.387,
    "Venus": 0.722,
    "Earth": 1.000,
    "Mars": 1.524,
    "Jupiter": 5.204,
    "Saturn": 9.559,
    "Uranus": 19.185,
    "Neptune": 30.156,
    "Pluto": 39.482,
}
BODY_STATUS = {
    **{body: "observed_planet" for body in OBSERVED_AU if body != "Pluto"},
    "Pluto": "observed_dwarf_planet",
    "Harmonia": "hypothetical_unobserved_node",
}
PRIMARY_NINE = tuple(body for body in BODY_ORDER if body in OBSERVED_AU)
EIGHT_PLANETS = tuple(body for body in PRIMARY_NINE if body != "Pluto")
NINE_WITHOUT_ANCHOR = tuple(body for body in PRIMARY_NINE if body != "Earth")
EIGHT_WITHOUT_ANCHOR = tuple(body for body in EIGHT_PLANETS if body != "Earth")
OUTER_FIVE = ("Jupiter", "Saturn", "Uranus", "Neptune", "Pluto")


def fixed_srhf_au() -> dict[str, float]:
    """Published fixed algebraic prescription, with Earth normalised to 1 AU."""
    return {
        "Mercury": (14.0 / 15.0) * D,
        "Venus": 1.0 / A,
        "Earth": 1.0,
        "Mars": (B + D) / C,
        "Harmonia": 2.0 * A * C / B,
        "Jupiter": 2.0 * A * C,
        "Saturn": 2.0 * A * C**2,
        "Uranus": 4.0 * A * C**2,
        "Neptune": 2.0 * A * C * (B / D),
        "Pluto": 4.0 * A * C * (A + B),
    }


def silver_node_au() -> float:
    return 2.0 * A * C / B


def pi_node_au() -> float:
    return math.pi ** (2.0 / 3.0)


def outer_coefficients() -> np.ndarray:
    """Linear response to a_H for Jupiter, Saturn, Uranus, Neptune, Pluto."""
    return B * np.array([1.0, C, 2.0 * C, B / D, 2.0 * (A + B)], dtype=float)


def outer_predictions(h_au: float) -> dict[str, float]:
    return dict(zip(OUTER_FIVE, (h_au * outer_coefficients()).tolist()))


def fitted_outer_node_au() -> float:
    """Analytic least-squares optimum: explicitly post-hoc, five observations."""
    c = outer_coefficients()
    obs = np.array([OBSERVED_AU[name] for name in OUTER_FIVE], dtype=float)
    return float(np.dot(c, obs) / np.dot(c, c))


def neptune_zero_node_au() -> float:
    return OBSERVED_AU["Neptune"] / float(outer_coefficients()[3])


def _values(names: tuple[str, ...], predictions: dict[str, float]):
    if not names or any(n not in OBSERVED_AU for n in names):
        raise ValueError("Only nonempty sets of observed bodies can be scored")
    obs = np.array([OBSERVED_AU[name] for name in names], dtype=float)
    pred = np.array([predictions[name] for name in names], dtype=float)
    return obs, pred


def score(names: tuple[str, ...], predictions: dict[str, float]) -> dict[str, float]:
    """Body-level, AU-dimensional RMSE and percent MAPE/HSI (ddof=0)."""
    obs, pred = _values(names, predictions)
    diff = pred - obs
    residual_pct = 100.0 * diff / obs
    return {
        "n": len(names),
        "mape_pct": float(np.mean(np.abs(residual_pct))),
        "rmse_au": float(np.sqrt(np.mean(diff**2))),
        "hsi_pct": float(np.std(residual_pct, ddof=0)),
    }


def outer_hsi_closed_form(h_au: float) -> float:
    """Exact consequence of linear outer coefficients for h>=0."""
    if h_au < 0:
        raise ValueError("Preregistered HSI identity is for nonnegative h")
    obs = np.array([OBSERVED_AU[name] for name in OUTER_FIVE])
    return float(100.0 * h_au * np.std(outer_coefficients() / obs, ddof=0))


def historical_ten_slot_diagnostic(reference_harmonia_au: float = 2.1437):
    """Historical 10-slot numerical diagnostic; NOT an observational metric."""
    names = BODY_ORDER
    predictions = fixed_srhf_au()
    ref = dict(OBSERVED_AU, Harmonia=reference_harmonia_au)
    obs = np.array([ref[name] for name in names])
    pred = np.array([predictions[name] for name in names])
    residual_pct = 100.0 * (pred - obs) / obs
    return {
        "n": len(names),
        "mape_pct": float(np.mean(np.abs(residual_pct))),
        "rmse_au": float(np.sqrt(np.mean((pred - obs)**2))),
    }
