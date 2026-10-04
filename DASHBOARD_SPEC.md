# Power BI Dashboard Specification

## Page 1 — Executive Overview
Cards: Customers, Churn Rate, MRR, Revenue at Risk, Avg CLV.
Visuals: Churn by Plan, Churn by Acquisition Channel, Revenue at Risk by Plan, Customer Risk Table.

## Page 2 — Retention Intelligence
Visuals: Tenure vs Churn, Usage Score vs Churn, Support Tickets vs Churn, High-Value At-Risk Customers.

## Page 3 — Customer 360
Slicers: Plan, Region, Acquisition Channel.
Table: Customer ID, Plan, MRR, Usage Score, Support Tickets, Churn Probability, Revenue at Risk.

## Key DAX
Churn Rate = DIVIDE(SUM(Customers[churned]), COUNTROWS(Customers))
MRR = SUM(Customers[monthly_revenue])
Revenue at Risk = SUM(Customers[revenue_at_risk])
