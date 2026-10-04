SELECT plan, COUNT(*) customers, SUM(churned) churned_customers,
ROUND(100.0*SUM(churned)/COUNT(*),2) churn_rate_pct,
ROUND(AVG(monthly_revenue),2) arpu,
ROUND(SUM(CASE WHEN churned=1 THEN monthly_revenue ELSE 0 END),2) monthly_revenue_at_risk
FROM customers GROUP BY plan ORDER BY churn_rate_pct DESC;

SELECT customer_id, plan, monthly_revenue, usage_score, support_tickets_90d, clv_12m
FROM customers WHERE churned=1 ORDER BY monthly_revenue DESC LIMIT 100;
