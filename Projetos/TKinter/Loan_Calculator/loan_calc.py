from tkinter import *
class loan_calc:
    
    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")
        window.geometry("400x300")
        
        Label(window, text="Interest Rate (%):").grid(row=0, column=0, padx=10, pady=10)
        Label(window, text="Number of Years:").grid(row=1, column=0, padx=10, pady=10)
        Label(window, text="Loan Amount:").grid(row=2, column=0, padx=10, pady=10)
        Label(window, text="Monthly Payment:").grid(row=3, column=0, padx=10, pady=10)
        Label(window, text="Total Payment:").grid(row=4, column=0, padx=10, pady=10)
        
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=0, column=1, padx=10, pady=10)
        
        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable=self.numberOfYearsVar, justify=RIGHT).grid(row=1, column=1, padx=10, pady=10)
        
        self.loanAmountVar = StringVar()
        Entry(window, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=2, column=1, padx=10, pady=10)
        
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, textvariable=self.monthlyPaymentVar, justify=RIGHT).grid(row=3, column=1, padx=10, pady=10)

        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, textvariable=self.totalPaymentVar, justify=RIGHT).grid(row=4, column=1, padx=10, pady=10)

        btnComputePayment = Button(window, text="Compute Payment", command=self.computePayment).grid(row=5, column=1, padx=10, pady=10)
        
        window.mainloop()
    
    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(float(self.loanAmountVar.get()),
                        float(self.annualInterestRateVar.get()) / 1200,
                        int(self.numberOfYearsVar.get()))
        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = monthlyPayment * int(self.numberOfYearsVar.get()) * 12
        self.totalPaymentVar.set(format(totalPayment, '10.2f'))

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberofYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberofYears * 12))
        
        return monthlyPayment
    
loan_calc()