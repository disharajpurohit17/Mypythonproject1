# Report generations for student marks project

import matplotlib.pyplot as plt

def plot_scores(df):
    """plot student average scores"""
    plt.figure(figsize=(6,4))
    plt.bar(df["Name"], df["Average"], color="skyblue")
    plt.xlabel("students")
    plt.ylabel("Average Marks")
    plt.title("student performance")
    plt.show()
    