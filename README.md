# Credit Risk Analysis
## Overview
The **Credit Risk Analysis** project aims to explore and analyze loan data to understand the factors influencing loan performance and the distribution of loan statuses. The analysis categorizes loan statuses into four distinct groups: Normal, Delinquent, Default, and Not Compliant. By leveraging data visualization techniques, the project provides insights into how various factors such as loan amount, interest rate, annual income, and home ownership status affect loan outcomes.

This project is particularly useful for financial analysts, data scientists, and stakeholders in the lending industry who are interested in understanding loan performance and risk assessment.

---

## Tools Used
- **Python**: The primary programming language used for data analysis.
- **Pandas**: A powerful data manipulation library for handling structured data.
- **NumPy**: A library for numerical computations, used for efficient array operations.
- **Matplotlib**: A plotting library for creating static, animated, and interactive visualizations in Python.
- **Seaborn**: A statistical data visualization library based on Matplotlib, providing a high-level interface for drawing attractive graphics.
- **Jupyter Notebook**: An open-source web application that allows you to create and share documents containing live code, equations, visualizations, and narrative text.
- **Excel**: Used for data dictionary reference and understanding the dataset structure.

---

## Data Description
The analysis uses the following datasets:
- **loan.csv**: Contains loan data with various features such as loan amount, interest rate, term, annual income, and loan status.
- **LCDataDictionary.xlsx**: Provides descriptions of the columns in the loan dataset.

### Key Columns in `loan.csv`:
- **loan_amnt**: The amount of the loan.
- **int_rate**: The interest rate of the loan.
- **term**: The term of the loan (in months).
- **dti**: Debt-to-income ratio.
- **annual_inc**: Annual income of the borrower.
- **delinq_2yrs**: Number of delinquencies in the past 2 years.
- **open_acc**: Number of open credit accounts.
- **grade**: The grade assigned to the loan.
- **home_ownership**: Home ownership status of the borrower.
- **loan_status**: Status of the loan (e.g., Fully Paid, Charged Off).

---

## Analysis Overview
The analysis includes:
1. **Data Exploration**: Initial exploration of the dataset, including shape, info, and null value percentages.
2. **Loan Status Categorization**: Classification of loan statuses into four categories: Normal, Delinquent, Default, and Not Compliant.
3. **Data Visualization**: Various visualizations to illustrate relationships between loan status and factors such as:
   - **Loan Amount vs. Loan Status**: Examination of how loan amounts vary by loan status.
   - **Loan Status vs. Grade**: Analysis of loan status distribution across different grades.
   - **Interest Rate Analysis**: Comparison of interest rates across loan statuses.
   - **Annual Income Analysis**: Investigation of annual income distributions by loan status.
   - **Home Ownership Impact**: Analysis of how home ownership affects loan status.
4. **Statistical Insights**: Analysis of trends and distributions related to loan performance.

---

