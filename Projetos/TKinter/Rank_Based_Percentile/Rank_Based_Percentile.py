from tkinter import *

class RankBasedPercentile:
    def __init__(self):
        self.window = Tk()
        self.window.title("Rank Based Percentile")
        self.window.geometry("400x300")

        Label(self.window, text="Rank:").grid(row=0, column=0, padx=10, pady=10)
        Label(self.window, text="And").grid(row=1, column=0, padx=10, pady=10)
        Label(self.window, text="Total Participants:").grid(row=2, column=0, padx=10, pady=10)
        Label(self.window, text="Percentile:").grid(row=4, column=0, padx=10, pady=10)

        self.rank_field = Entry(self.window)
        self.rank_field.grid(row=0, column=1, padx=10, pady=10)

        self.total_participants_field = Entry(self.window)
        self.total_participants_field.grid(row=2, column=1, padx=10, pady=10)

        self.percentile_field = Entry(self.window)
        self.percentile_field.grid(row=4, column=1, padx=10, pady=10)

        Button(self.window, text="Find Percentile", command=self.getPercentile).grid(row=3, column=0, padx=10, pady=10)
        Button(self.window, text="Clear", command=self.clear).grid(row=5, column=0, padx=10, pady=10)

        self.window.mainloop()

    def getPercentile(self):
        try:
            students = int(self.total_participants_field.get())
            rank = int(self.rank_field.get())
            result = round((students - rank) / students * 100, 3)
            self.percentile_field.delete(0, END)
            self.percentile_field.insert(0, f"{result}%")
        except ValueError:
            self.percentile_field.delete(0, END)
            self.percentile_field.insert(0, "Invalid input")

    def clear(self):
        self.rank_field.delete(0, END)
        self.total_participants_field.delete(0, END)
        self.percentile_field.delete(0, END)

if __name__ == "__main__":
    RankBasedPercentile()