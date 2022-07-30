import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'course_length':200, 'trainer_salary':35000, 'office_rent':540000,'infrastructure_cost':170000, 'electricity':6780, 'daily_expenses':480, 'marketing_expenses':3500, 'enrollment_due_to_brand':25})

print(r.json())