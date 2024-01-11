# DATA DICTIONARY
Contains granular details about each variable. 

## Surface Properties of Dataset 

|          | Number of instances | Nufmber of Attributes | Attribute types | Contains missing values? | Mismatches between data and metadata file|
| -------- | -------- | -------- | -------- | -------| ---------- |
| first_3000   | 3000   | 21   | <ul><li>Categorical</li><li>Float</li><li>Integer</li><li>Boolean</li></ul>   |   Yes  |  <ul><li> Boolean values where string object expected</li></ul> |
| last_2000   | 2043   |  21  | <ul><li>Categorical</li><li>Float</li><li>Integer</li><ul>   |      No  |  <ul><li>SeniorCitizen values mismatch with first 3000</li><li>TotalCharges dtype mismatch</li></ul>              |


**Comments on the Surface Properties of the DataSet**
- Both dataset contains the same columns. However, there are differences in dtypes of corresponding columns.  
- Discrepancies in Attribute types will be investigated and rectified. eg: We notice boolean variables have True/False in first_3000 but Yes/No in last_2000.
- We'll conduct detailed investigation on the completeness of first 3000 data and impute missing values based on sufficient evidence from investigation.  
- We'll then perform necessary actions for uniformity and then merge the two datasets for indepth exploratory analysis.

## Data content and Quality 

**Completeness:** Missing values, Incomplete records

**Accuracy:** Outliers, Data entry errors, Duplicates.

**Consistency:** Inconsistent formats, Inconsistent categories or labels, Inconsistent representations

**Relevancy:** Irrelevant variables, Outdated data


|          | **Completeness** | **Accuracy** | **Consistency** |
| -------- | -------- | -------- | -------- |
| **first_3000**  | <ul><li>OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies attributes have 21.70% missing values for the same records. We refer to these as "smart features" </li> <li>MultipleLines and TotalCharges have 269(8.97%) and 5(0.17%) missing values respectively. </li> <li>The target variable "Churn" contains 1 missing value</li> </ul>   | <ul> <li>No duplicated records</li></ul>   | <ul> <li>No outliers in TotalCharges. Imputing with mean will be good</li> <li>Inconsistent data types. eg: True/False vs Yes/No</li> <li>"smart features" formatted as Boolean</li> </ul> |
| **last_2000**   | <li>No missing values </li> | <ul> <li>No duplicated records</li> </ul>  </ul>  | <li>Inconsistent data types. eg: Yes/No vs 0/1.</li> <li>TotalCharges formated as string</li> <li>"smart features" formated as string</li>|


**Comments on Identified Data Quality issues**
    
 | **Completeness** | **Accuracy** | **Consistency** |
 | -------- | -------- | -------- |
 |   <ul> <li>Comparing unique values in last 2000 dataset and exploring the "InternetService" attribute, we found enough evidence to impute the "smart features" missing values with "No internet service" </li> <li>"MultipleLines" column will be imputed with "No phone service" as in last 2000</li> <li>"TotalCharges" will be replaced with the median </li> <li>record with "Churn" missing will be dropped</li> </ul>       |  <ul><li>Dataset appears to be quite Accurate</li></ul>         |  <ul><li>We'll reformat SeniorCitizen values from 1/0 to Yes/No in the last 2000 data</li> <li>All boolean columns will be reformtted to Yes/No</li> </ul> |
