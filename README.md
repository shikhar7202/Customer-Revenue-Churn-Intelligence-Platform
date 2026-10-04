# Customer Revenue & Churn Intelligence Platform
**Industry:** SaaS / Subscription | **Stack:** SQL, Python, Pandas, Scikit-learn, Power BI

## Business problem
Identify churn drivers, quantify revenue at risk, and prioritize retention actions.

## Questions
1. Which customers are most likely to churn?
2. How much MRR is at risk?
3. Which plans/channels have weak retention?
4. Which high-value customers need intervention?

## Pipeline
CSV → SQL KPI layer → Python churn model → scored customer table → Power BI executive dashboard.

## KPIs
Churn Rate, MRR, ARPU, CLV, Retention Rate, Revenue at Risk, Usage Score.

## Run
Install `requirements.txt`; run `python/churn_analysis.py`; load generated CSVs into Power BI.
