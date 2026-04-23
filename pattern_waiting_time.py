import random
import matplotlib.pyplot as plt

def waiting_time(pattern):
    k = len(pattern)
    sequence = ""
    steps = 0

    while True:
        sequence += str(random.getrandbits(1))
        steps += 1

        if sequence[-k:] == pattern:
            return steps

def average_wait(pattern, trials=100):
    return sum(waiting_time(pattern) for _ in range(trials)) / trials

def run_experiment(max_k=8):
    lengths = []
    times = []

    for k in range(1, max_k + 1):
        pattern = "1" * k  # simple worst-case pattern
        avg_time = average_wait(pattern)

        lengths.append(k)
        times.append(avg_time)

        print(f"k={k}, avg_wait={avg_time}")

    plt.plot(lengths, times)
    plt.xlabel("Pattern Length (k)")
    plt.ylabel("Average Waiting Time")
    plt.title("Pattern Emergence in Random Sequences")
    plt.show()

if __name__ == "__main__":
    run_experiment()