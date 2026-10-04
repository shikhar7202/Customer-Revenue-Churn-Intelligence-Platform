Churn Rate = DIVIDE(SUM(Customers[churned]),COUNTROWS(Customers))
MRR = SUM(Customers[monthly_revenue])
Revenue at Risk = SUM(Customers[revenue_at_risk])
ARPU = DIVIDE([MRR],COUNTROWS(Customers))
Retention Rate = 1-[Churn Rate]
