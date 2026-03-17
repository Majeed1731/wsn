# Wireless Sensor Network (WSN) Simulation

A Python simulation of a WSN deployed in a 100 m × 100 m area with a Base Station at the centre (50, 50). Nodes transmit data directly to the BS in a single-hop topology.

## Requirements

```
pip install numpy matplotlib
```

## Run

```
python wsn_simulation.py
```

## What it does

- Simulates **10, 50, and 100 node** configurations
- Runs **20 independent iterations** per configuration (reproducible via fixed seed)
- Computes:
  - **Average Energy per Node** — `E = distance × 0.1 J`
  - **Packet Delivery Ratio (PDR)** — packet delivered if `distance ≤ 50 m`
- Prints a summary table and report-ready values to the console
- Saves `wsn_results.png` with two graphs (Energy vs Nodes, PDR vs Nodes)

## Results (seed = 42)

| Node Count | Avg Energy (J) | PDR    |
|:----------:|:--------------:|:------:|
| 10         | 3.8131         | 0.7700 |
| 50         | 0.8322         | 0.7840 |
| 100        | 3.8258         | 0.7805 |

## Result Explanation

As node density increases, the average energy consumption per node stays nearly constant because each node transmits only once per round and the mean node-to-BS distance converges (law of large numbers). The PDR also stabilises close to the theoretical value of ~78.5% — the fraction of the deployment area within 50 m of the centre — confirming that higher node counts reduce statistical variance and yield more predictable delivery ratios.
