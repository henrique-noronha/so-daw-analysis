"""
Calcula intervalos de confianca de 95% por bootstrap a partir dos CSVs
do PerfMon ja coletados.

Uso:
    python bootstrap_ci.py <arquivo.csv>

Saida no console: por contador, media e IC95% (low, high).

Dependencias:
    pip install pandas numpy scipy
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

N_RESAMPLES = 10_000
CONFIDENCE = 0.95
RNG = np.random.default_rng(seed=42)


def bootstrap_mean_ci(samples: np.ndarray) -> tuple[float, float, float]:
    """Retorna (media, ci_low, ci_high) para 95% via bootstrap percentil."""
    samples = samples[~np.isnan(samples)]
    if len(samples) < 5:
        return float("nan"), float("nan"), float("nan")
    res = stats.bootstrap(
        (samples,),
        np.mean,
        n_resamples=N_RESAMPLES,
        confidence_level=CONFIDENCE,
        method="percentile",
        random_state=RNG,
    )
    return float(np.mean(samples)), float(res.confidence_interval.low), float(res.confidence_interval.high)


def analyze(csv_path: Path) -> None:
    # PerfMon exporta com header em PT-BR; tenta latin-1 antes do utf-8
    for enc in ("latin-1", "utf-8", "cp1252"):
        try:
            df = pd.read_csv(csv_path, encoding=enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        raise RuntimeError(f"Nao consegui ler {csv_path}")

    # primeira coluna costuma ser timestamp; ignorar
    metric_cols = [c for c in df.columns if c != df.columns[0]]

    print(f"\n=== {csv_path.name} ===")
    print(f"Amostras totais: {len(df)}")
    print(f"{'Metrica':60s} {'Media':>10s} {'IC95% baixo':>13s} {'IC95% alto':>13s}")
    print("-" * 100)
    for col in metric_cols:
        series = pd.to_numeric(df[col], errors="coerce").to_numpy()
        mean, lo, hi = bootstrap_mean_ci(series)
        nome = col[-58:] if len(col) > 58 else col
        print(f"{nome:60s} {mean:>10.3f} {lo:>13.3f} {hi:>13.3f}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Uso: python bootstrap_ci.py <arquivo.csv> [<arquivo2.csv> ...]")
        sys.exit(1)
    for arg in sys.argv[1:]:
        analyze(Path(arg))


if __name__ == "__main__":
    main()
