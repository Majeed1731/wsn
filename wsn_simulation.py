"""
Wireless Sensor Network (WSN) Simulation
=========================================
Scenario:
  - 100m x 100m deployment area
  - One Base Station (BS) at center (50, 50)
  - Nodes transmit data directly to the BS (single-hop)

Configurations:
  - 10, 50, and 100 sensor nodes

Performance Metrics:
  - Average Energy Consumption per node  (energy = distance × 0.1 J)
  - Packet Delivery Ratio (PDR)          (success if distance ≤ 50 m)

Each configuration is averaged over 20 independent iterations.
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
AREA_SIZE       = 100          # metres (square grid side length)
BASE_STATION    = (50.0, 50.0) # centre of the area
ENERGY_FACTOR   = 0.1          # J / metre
PDR_THRESHOLD   = 50.0         # metres  — packet delivered if dist ≤ this
N_ITERATIONS    = 20           # simulation repetitions per configuration
NODE_COUNTS     = [10, 50, 100]
RANDOM_SEED     = 42           # master seed for reproducibility


# ---------------------------------------------------------------------------
# Core functions
# ---------------------------------------------------------------------------

def generate_nodes(n_nodes: int, rng: np.random.Generator) -> np.ndarray:
    """
    Randomly place *n_nodes* sensor nodes inside the deployment area.

    Parameters
    ----------
    n_nodes : Number of sensor nodes to generate.
    rng     : NumPy random Generator instance (ensures reproducibility).

    Returns
    -------
    nodes : ndarray of shape (n_nodes, 2) — (x, y) coordinates in [0, AREA_SIZE].
    """
    return rng.uniform(0, AREA_SIZE, size=(n_nodes, 2))


def calculate_distances(nodes: np.ndarray) -> np.ndarray:
    """
    Compute Euclidean distance from each node to the Base Station.

    Parameters
    ----------
    nodes : ndarray of shape (n, 2).

    Returns
    -------
    distances : 1-D array of length n.
    """
    bs = np.array(BASE_STATION)
    return np.sqrt(np.sum((nodes - bs) ** 2, axis=1))


def calculate_energy(distances: np.ndarray) -> float:
    """
    Compute the *average* energy consumed per node for one transmission round.

    Energy model (simplified first-order radio model):
        E_node = distance × ENERGY_FACTOR   (Joules)

    Parameters
    ----------
    distances : 1-D array of per-node distances to the BS.

    Returns
    -------
    avg_energy : Average energy per node (J).
    """
    energies = distances * ENERGY_FACTOR
    return float(np.mean(energies))


def calculate_pdr(distances: np.ndarray) -> float:
    """
    Compute Packet Delivery Ratio.

    A packet is considered *successfully delivered* when the transmitting
    node is within PDR_THRESHOLD metres of the Base Station (sufficient
    signal strength).

    Parameters
    ----------
    distances : 1-D array of per-node distances to the BS.

    Returns
    -------
    pdr : Ratio in [0, 1] representing fraction of packets delivered.
    """
    successful = np.sum(distances <= PDR_THRESHOLD)
    return float(successful / len(distances))


def simulate_network(n_nodes: int, n_iterations: int = N_ITERATIONS,
                     master_seed: int = RANDOM_SEED) -> dict:
    """
    Run the WSN simulation for a given node count over multiple iterations.

    Each iteration uses a unique but deterministic seed derived from the
    master seed, so results are fully reproducible.

    Parameters
    ----------
    n_nodes     : Number of sensor nodes in this configuration.
    n_iterations: Number of independent simulation runs to average.
    master_seed : Base seed for the random number generator.

    Returns
    -------
    results : dict with keys
              'n_nodes'    – node count
              'avg_energy' – mean energy per node averaged over iterations
              'avg_pdr'    – mean PDR averaged over iterations
              'energy_per_iter' – list of per-iteration energy values
              'pdr_per_iter'    – list of per-iteration PDR values
    """
    energy_list = []
    pdr_list    = []

    for i in range(n_iterations):
        # Unique seed per iteration so each run is independent yet deterministic
        rng   = np.random.default_rng(master_seed + i * 1000 + n_nodes)
        nodes = generate_nodes(n_nodes, rng)
        dists = calculate_distances(nodes)

        energy_list.append(calculate_energy(dists))
        pdr_list.append(calculate_pdr(dists))

    return {
        "n_nodes"         : n_nodes,
        "avg_energy"      : float(np.mean(energy_list)),
        "avg_pdr"         : float(np.mean(pdr_list)),
        "energy_per_iter" : energy_list,
        "pdr_per_iter"    : pdr_list,
    }


# ---------------------------------------------------------------------------
# Visualisation
# ---------------------------------------------------------------------------

def plot_results(results: list[dict]) -> None:
    """
    Generate two side-by-side graphs:
      1. Number of Nodes vs Average Energy Consumption
      2. Number of Nodes vs Packet Delivery Ratio

    Parameters
    ----------
    results : List of result dicts returned by simulate_network().
    """
    node_counts  = [r["n_nodes"]    for r in results]
    avg_energies = [r["avg_energy"] for r in results]
    avg_pdrs     = [r["avg_pdr"]    for r in results]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle("WSN Simulation Results (100 m × 100 m area, BS at centre)",
                 fontsize=13, fontweight="bold")

    # --- Graph 1: Energy Consumption ---
    ax1.plot(node_counts, avg_energies, marker="o", linewidth=2, markersize=7)
    ax1.set_title("Number of Nodes vs Energy Consumption")
    ax1.set_xlabel("Number of Nodes")
    ax1.set_ylabel("Average Energy per Node (J)")
    ax1.set_xticks(node_counts)
    ax1.grid(True, linestyle="--", alpha=0.6)

    # Annotate each data point
    for x, y in zip(node_counts, avg_energies):
        ax1.annotate(f"{y:.3f} J", xy=(x, y),
                     xytext=(5, 8), textcoords="offset points", fontsize=9)

    # --- Graph 2: Packet Delivery Ratio ---
    ax2.plot(node_counts, avg_pdrs, marker="s", linewidth=2, markersize=7)
    ax2.set_title("Number of Nodes vs Packet Delivery Ratio")
    ax2.set_xlabel("Number of Nodes")
    ax2.set_ylabel("Packet Delivery Ratio (PDR)")
    ax2.set_xticks(node_counts)
    ax2.set_ylim(0, 1.05)
    ax2.grid(True, linestyle="--", alpha=0.6)

    # Annotate each data point
    for x, y in zip(node_counts, avg_pdrs):
        ax2.annotate(f"{y:.3f}", xy=(x, y),
                     xytext=(5, 8), textcoords="offset points", fontsize=9)

    plt.tight_layout()
    plt.savefig("wsn_results.png", dpi=150, bbox_inches="tight")
    print("\n[INFO] Graph saved as 'wsn_results.png'")
    plt.show()


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def print_results(results: list[dict]) -> None:
    """Print a formatted summary table to the console."""
    separator = "-" * 60
    header    = f"{'Nodes':>8}  {'Avg Energy (J)':>16}  {'PDR':>8}"

    print("\n" + "=" * 60)
    print("  WSN SIMULATION — SUMMARY OF RESULTS")
    print("=" * 60)
    print(f"  Area          : {AREA_SIZE} m × {AREA_SIZE} m")
    print(f"  Base Station  : {BASE_STATION} (centre)")
    print(f"  Energy model  : E = distance × {ENERGY_FACTOR} J")
    print(f"  PDR threshold : distance ≤ {PDR_THRESHOLD} m")
    print(f"  Iterations    : {N_ITERATIONS} per configuration")
    print(f"  Random seed   : {RANDOM_SEED}")
    print("=" * 60)
    print(separator)
    print(header)
    print(separator)

    for r in results:
        print(f"  {r['n_nodes']:>6}  "
              f"  {r['avg_energy']:>14.4f}  "
              f"  {r['avg_pdr']:>6.4f}")

    print(separator)


def report_values(results: list[dict]) -> dict:
    """
    Return a clean dictionary of final averaged values — ready to cite in a
    university report.

    Example usage:
        data = report_values(results)
        print(data)
    """
    return {
        r["n_nodes"]: {
            "avg_energy_J" : round(r["avg_energy"], 4),
            "pdr"          : round(r["avg_pdr"], 4),
        }
        for r in results
    }


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def main() -> None:
    """Run the full WSN simulation pipeline."""

    print("[INFO] Starting WSN simulation …")

    # Run simulation for each node configuration
    all_results = []
    for n in NODE_COUNTS:
        print(f"  Simulating {n:>3} nodes × {N_ITERATIONS} iterations …", end=" ")
        result = simulate_network(n_nodes=n)
        all_results.append(result)
        print(f"done  (energy={result['avg_energy']:.4f} J, "
              f"PDR={result['avg_pdr']:.4f})")

    # Console summary
    print_results(all_results)

    # Report-ready dict
    report = report_values(all_results)
    print("\n[REPORT VALUES]  (copy this directly into your report)\n")
    print(f"{'Node Count':<12} {'Avg Energy (J)':<18} {'PDR':<8}")
    print("-" * 42)
    for nodes, metrics in report.items():
        print(f"{nodes:<12} {metrics['avg_energy_J']:<18} {metrics['pdr']:<8}")

    # Explanation for the report
    print("\n[RESULT EXPLANATION]")
    print(
        "  The simulation shows that as node density increases, the average\n"
        "  energy consumption per node remains nearly stable because each node\n"
        "  still transmits only once per round and the mean distance to the BS\n"
        "  converges with more samples (law of large numbers). The PDR also\n"
        "  stabilises close to the theoretical fraction of the 100×100 m² area\n"
        "  that falls within 50 m of the centre (~78.5%), confirming that a\n"
        "  higher node count yields a more consistent and predictable delivery\n"
        "  ratio with less statistical variance across iterations."
    )

    # Graphs
    plot_results(all_results)


if __name__ == "__main__":
    main()
