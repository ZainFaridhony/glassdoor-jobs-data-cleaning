import pandas as pd

from datetime import date

df = pd.read_csv('glassdoor_jobs.csv')

# salary parsing
df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

df['min_salary'] = minus_Kd.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_Kd.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

# state field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[0])
job_state = df.job_state.value_counts()

# age of company
df['age'] = df.Founded.apply(lambda x: x if x < 1 else date.today().year - x)

# parsing job description (python, etc)

#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

#r_studio
df['r_yn'] = df['Job Description'].apply(lambda x: 1 if ' r ' in x.lower() else 0)

#java
df['java_yn'] = df['Job Description'].apply(lambda x: 1 if 'java' in x.lower() else 0)

#spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)

#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

#aws
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)

#ai
df['ai'] = df['Job Description'].apply(lambda x: 1 if 'ai' in x.lower() else 0)

#machine learning
df['machine_learning'] = df['Job Description'].apply(lambda x: 1 if 'machine learning' in x.lower() else 0)

#data scientist
df['data_scientist'] = df['Job Description'].apply(lambda x: 1 if 'data scientist' in x.lower() else 0)