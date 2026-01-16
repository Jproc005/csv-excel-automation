def generate_plot(df):
    if "date" in df.columns and "amount" in df.columns:
        summary = df.groupby("date")["amount"].sum()
        summary.plot(title="Total Amount Over Time")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.tight_layout()
        plt.savefig("../data/cleaned/plot.png")  # saves plot as PNG
        plt.show()
