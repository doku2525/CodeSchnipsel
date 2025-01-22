import multiprocessing as mp
import os


if __name__ == "__main__":
    print(f"\n",
          f"Anzahl der CPUs nach {mp.cpu_count() = }\n",
          f"Anzahl der CPUs nach {os.cpu_count() = }")
