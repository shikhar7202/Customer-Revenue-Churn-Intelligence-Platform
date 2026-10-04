import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
df=pd.read_csv("../data/customers.csv")
features=["age","tenure_months","monthly_revenue","support_tickets_90d","usage_score"]
Xtr,Xte,ytr,yte=train_test_split(df[features],df.churned,test_size=.2,stratify=df.churned,random_state=42)
m=RandomForestClassifier(n_estimators=300,max_depth=7,class_weight="balanced",random_state=42)
m.fit(Xtr,ytr); print("ROC-AUC:",round(roc_auc_score(yte,m.predict_proba(Xte)[:,1]),3))
df["churn_probability"]=m.predict_proba(df[features])[:,1]
df["revenue_at_risk"]=(df.monthly_revenue*df.churn_probability).round(2)
df.to_csv("../data/customer_risk_scored.csv",index=False)
print(pd.Series(m.feature_importances_,index=features).sort_values(ascending=False))
