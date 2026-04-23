import numpy as np
import random
import matplotlib.pyplot as plt

# Measurement angles (radians)
a = 0
a_p = np.pi / 2
b = np.pi / 4
b_p = -np.pi / 4

def simulate_pair(theta):
    # Probability that A*B = +1
    p_same = (1 - np.cos(theta)) / 2
    return 1 if random.random() < p_same else -1

def run_trials_with_progress(N=100000, step=5000):
    results = {
        ('a','b'): [],
        ('a','b_p'): [],
        ('a_p','b'): [],
        ('a_p','b_p'): []
    }

    choices = list(results.keys())
    S_values = []
    trial_counts = []

    for i in range(1, N + 1):
        choice = random.choice(choices)

        if choice == ('a','b'):
            theta = a - b
        elif choice == ('a','b_p'):
            theta = a - b_p
        elif choice == ('a_p','b'):
            theta = a_p - b
        else:
            theta = a_p - b_p

        outcome = simulate_pair(theta)
        results[choice].append(outcome)

        # Every 'step' trials, compute S
        if i % step == 0:
            def E(key):
                return np.mean(results[key]) if results[key] else 0

            S = (
                E(('a','b')) +
                E(('a','b_p')) +
                E(('a_p','b')) -
                E(('a_p','b_p'))
            )

            S_values.append(abs(S))
            trial_counts.append(i)

    return trial_counts, S_values

if __name__ == "__main__":
    trials, S_vals = run_trials_with_progress(200000, step=5000)

    print(f"Final |S| ≈ {S_vals[-1]}")

    # Plot
    plt.plot(trials, S_vals)
    plt.axhline(2*np.sqrt(2), linestyle='--', label="2√2 (Tsirelson Bound)")
    plt.axhline(2, linestyle='--', label="Classical Limit (2)")
    plt.xlabel("Number of Trials")
    plt.ylabel("|S|")
    plt.title("CHSH Simulation Convergence")
    plt.legend()
    plt.show()