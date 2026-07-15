"""Quality Oracle — deterministic feedback loop for non-code benchmarks.

Converts preference/quality scores into grounded per-failure retry prompts
using the same architecture as the compiler oracle for code tasks.

Core flow:
  response → ClaimExtractor → RagVerifier → FeatureChecks → OracleResult
  OracleResult.feedback_block() → retry prompt (drop-in for EvalResult.feedback_block)
"""

from .oracle import QualityOracle, OracleResult
from .claim_extractor import ClaimExtractor, Claim
from .rag_verifier import RagVerifier, ClaimVerification
from .feature_checks import FeatureChecker, FeatureResult
from .rubric_decomposer import RubricDecomposer
from .feedback_builder import build_feedback_block

__all__ = [
    "QualityOracle", "OracleResult",
    "ClaimExtractor", "Claim",
    "RagVerifier", "ClaimVerification",
    "FeatureChecker", "FeatureResult",
    "RubricDecomposer",
    "build_feedback_block",
]
