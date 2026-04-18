def main() -> None:
    print("\nLOADING STATUS: Loading programs...")
    flag = True

    print("\nChecking dependencies...")
    try:
        import pandas as pd
        print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
    except ModuleNotFoundError:
        flag = False
        print("[ERROR] pandas: Missin dependency")
        print("pip install -r requirements.txt\nor")
        print("poetry install")

    try:
        import numpy as np
        print(f"[OK] numpy ({np.__version__}) - Numerical computation ready")
    except ModuleNotFoundError:
        flag = False
        print("[ERROR] numpy: Missin dependency")
        print("pip install -r requirements.txt\nor")
        print("poetry install")
    try:
        import matplotlib as mat
        from matplotlib import pyplot as plt
        print(f"[OK] matplotlib ({mat.__version__}) - Visualization ready")
    except ModuleNotFoundError:
        flag = False
        print("[ERROR] matplotlib: Missin dependency")
        print("pip install -r requirements.txt\nor")
        print("poetry install")

    if flag:
        print("\nAnalyzing Matrix data...")
        print("Processing 1000 data points...")
        time = np.linspace(0, 10, 1000)
        sign = np.sin(time) + np.random.normal(0, 0.3, 1000)
        df = pd.DataFrame({
            "time": time,
            "signal": sign})

        print("Generating visualization...")
        plt.figure()
        plt.plot(df["time"], df["signal"])
        plt.title("Matrix Signal Activity")
        plt.xlabel("Time")
        plt.ylabel("Signal Strenght")
        plt.savefig("matrix_analysis.png")

        print("\nAnalysis complete!")
        print("Result saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
