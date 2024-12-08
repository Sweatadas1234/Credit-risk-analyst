#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[5]:


dic = pd.read_excel('LCDataDictionary.xlsx')
df = pd.read_csv('loan.csv')


# In[6]:


df.shape


# In[7]:


df.info()


# In[8]:


columns = df.columns.tolist()
print(columns)


# In[9]:


null_percentages = df.isnull().mean() * 100


for column, percentage in null_percentages.items():
    
    print({column: [round(percentage, 5), df[column].dtype]})


# In[10]:


first_row = df.iloc[0].T
first_row[:50]


# In[11]:


for i in df.columns:

  print({i: df[i].nunique()})


# In[12]:


df['loan_status'].unique()


# In[13]:


import matplotlib.pyplot as plt
import seaborn as sns

status_counts = df['loan_status'].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=status_counts.index, y=status_counts.values)
plt.title('Distribution of Loan Status')
plt.xlabel('Loan Status')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


# In[14]:


df_selected = df[['loan_amnt', 'int_rate', 'term', 'dti', 'annual_inc', 'delinq_2yrs','open_acc', 'grade',
'home_ownership','collections_12_mths_ex_med','revol_bal', 'total_acc','loan_status']]
#df_selected.dropna(inplace=True)


# In[15]:


df_selected.isnull().sum()


# In[16]:


df_selected.dropna(inplace=True)


# In[17]:


df_selected.isnull().sum()


# In[18]:


df_selected.shape


# In[19]:


df_selected.head(10)


# # Classify loan_status to 4 categories:
# 1. Normal: Fully Paid, Current, In Grace Period, Issued
# 
# 2. Delinquent: Late (16-30 days), Late (31-120 days),
# 
# 3. Default: Charged Off, Default
# 
# 4. Not Compliant: Does not meet the credit policy. Status: Fully Paid, Does not meet the credit policy. Status: Charged Off

# In[20]:


def categorize_loan_status(status):
    if status in ['Fully Paid', 'In Grace Period', 'Issued']:
        return 'Normal'
    elif status in ['Late (16-30 days)', 'Late (31-120 days)']:
        return 'Delinquent'
    elif status in ['Charged Off', 'Default']:
        return 'Default'
    elif 'Does not meet the credit policy' in status:
        return 'Not Compliant'
    elif 'Current' in status:
        return 'Current'
    else:
        return 'Unknown'

df_selected['loan_status'] = df_selected['loan_status'].apply(categorize_loan_status)


# In[21]:


df_selected['loan_status'].unique()


# # Data Visualization

# In[ ]:


#Loan Status vs Loan Amount
plt.figure(figsize=(12, 6))
sns.violinplot(x='loan_status', y='loan_amnt', data=df_selected)
plt.title('Loan Amount Distribution by Loan Status')
plt.xlabel('Loan Status')
plt.ylabel('Loan Amount')
plt.xticks(rotation=45)
plt.show()


# 1. Higher loan amounts are generally associated with a "Delinquent" loan status.
# 2. Defaulted and delinquent loans tend to show similar distributions in this amount range.
# 3. Loans that do not meet credit policy requirements are usually smaller in amount, suggesting higher risk associated with this type, which typically appears in low-amount loans.

# In[26]:


#Loan amount vs Grade
grade_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

plt.figure(figsize=(12, 6))
sns.boxplot(x='grade', y='loan_amnt', data=df_selected, palette='Set3',order=grade_order)
plt.title('Loan Amount Distribution by Grade')
plt.xlabel('Grade')
plt.ylabel('Loan Amount')
plt.xticks(rotation=45)
plt.show()


# 1. Loan amounts for grades A, B, and C are similar, with grade B showing the narrowest distribution.
# 2. From grades C to G, the median loan amount and overall distribution increase as the grade level rises.

# In[28]:


#Loan status vs Grade
grade_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

plt.figure(figsize=(10, 6))
sns.countplot(x='grade', hue='loan_status', data=df_selected, palette='Set2', order = grade_order)

plt.title('Loan Status Distribution by Grade')
plt.xlabel('Grade')
plt.ylabel('Count')
plt.legend(title='Loan Status', loc='upper right')

plt.show()


# As the loan grade increases, the proportion of individuals in the default and delinquent categories noticeably rises.

# In[30]:


#Loan status versus Interest Rate
plt.figure(figsize=(12, 6))
sns.boxplot(x='loan_status', y='int_rate', data=df_selected)
plt.title('Loan Amount by Loan Status')
plt.xlabel('Loan Status')
plt.ylabel('Loan Amount')
plt.xticks(rotation=45)
plt.show()


# The interest rate for the Default and Delinquent categories is significantly higher than for normal loans, and even the Not Compliant category shows a slightly higher interest rate than normal. This elevated interest rate might be one of the factors contributing to the increased likelihood of default or delinquency.

# In[33]:


#Loan status versus Annual Income
plt.figure(figsize=(12, 6))
sns.boxplot(x='loan_status', y='annual_inc', data=df_selected)
plt.yscale('log')
plt.title('Annual Income by Loan Status (Log Scale)')
plt.xlabel('Loan Status')
plt.ylabel('Annual Income (Log Scale)')

plt.xticks(rotation=45)
plt.show()


# The annual income range for individuals in the Normal category is quite broad, whereas those in the Default and Delinquent categories have a similar income distribution, which is relatively narrow with a median slightly lower than that of the Normal category. Meanwhile, individuals in the Not Compliant category generally have lower overall annual incomes.

# In[34]:


df_selected['loan_status'].value_counts().reset_index()


# We can find that the distribution of loan status is imbalanced.

# In[35]:


# Calculate the count of each category of loan status
loan_status_counts = df_selected['loan_status'].value_counts().reset_index()
loan_status_counts.columns = ['Loan Status', 'Count']

plt.figure(figsize=(10, 6))
sns.barplot(y='Loan Status', x='Count', data=loan_status_counts)

plt.title('Distribution of Loan Status')
plt.ylabel('Loan Status')
plt.xlabel('Count')

plt.show()


# In[38]:


#Loan status vs Home Ownership
# create a crosstab to calculate the count of each loan status by home ownership
cross_tab = pd.crosstab(df_selected['home_ownership'], df_selected['loan_status'])

# calcaulte the percentage
cross_tab_percentage = cross_tab.div(cross_tab.sum(1), axis=0)
colors = sns.color_palette("Blues", n_colors=cross_tab_percentage.shape[1])
cross_tab_percentage.plot(kind='bar', stacked=True, figsize=(10, 6), color=colors)

plt.title('Proportion of Loan Status by Home Ownership')
plt.xlabel('Home Ownership')
plt.ylabel('Proportion')
plt.legend(title='Loan Status', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Individuals whose home ownership fall under the "Mortgage," "Own," or "Rent" categories tend to have a lower default rate, while those in the "None" and "Other" categories show a higher rate of default.

# In[39]:


#Loan status vs Annual Income
plt.figure(figsize=(12, 6))
sns.boxplot(x='loan_status', y='annual_inc', data=df_selected)
plt.yscale('log')
plt.title('Annual Income by Loan Status (Log Scale)')
plt.xlabel('Loan Status')
plt.ylabel('Annual Income (Log Scale)')

plt.xticks(rotation=45)
plt.show()


# The annual income range for individuals in the Normal category is quite broad, whereas those in the Default and Delinquent categories have a similar income distribution, which is relatively narrow with a median slightly lower than that of the Normal category. Meanwhile, individuals in the Not Compliant category generally have lower overall annual incomes.

# In[ ]:




