class SavingsAccount:
    def input_balance(self,balance):
        self.savings=balance
    def monthly_interest(self,annual_inter_rate):
        interest=self.savings*annual_inter_rate/12
        self.savings+=interest
saver1=SavingsAccount()
saver2=SavingsAccount()
saver1.input_balance(2000)
saver2.input_balance(3000)
annual_inter_rate=0.05
saver1.monthly_interest(annual_inter_rate)
print(f"New balance for saver 1: {saver1.savings}")
saver2.monthly_interest(annual_inter_rate)
print(f"New balance for saver 2: {saver2.savings}")
annual_inter_rate=0.07
saver1.monthly_interest(annual_inter_rate)
print(f"Next month balance for saver 1: {saver1.savings}")
saver2.monthly_interest(annual_inter_rate)
print(f"Next month balance for saver 2: {saver2.savings}")