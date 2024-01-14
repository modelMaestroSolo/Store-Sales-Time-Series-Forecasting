# PROJECT WORKFLOW
Here, we outline the various steps taken from begining to end, to complete the project. 

## Business Understanding

**Goal** 
- Clearly state objectives(outcomes aimed to achieve)
- Clearly state and refine Initial question
- Define Success criteria and deliverables. 


**Activities** 
- Talk to stakeholders to understand their needs and the problem they seek to solve. 
- obtain objective(s) from feedback
- Derive Inital question: Verify that question has good characteristics - of interest to stakeholders, not already answered, answerable, stems from plausible framework
- Translate Quesetion into a data problem: Ensure problem is formulated in a way that it is Interpretable. 
- write down the success criteria and deliverables. 
 

## Prepare data for the project:

**Goal**
- Get data from multiple sources: excel sheets, github and sql database. 

**Activities** 
- Run the src/data/make_dataset.py script to extract data from database and save it in data/raw. (script contains instructions on how to do that)
- Download the other csv files and save it to data/raw. 

## Ask Analytical questions

**Goal**
- Ask at least 5 analytical questions in line with the objective(s) of the stakeholders

## Initial Data Exploration and Data Preprocessing.

**Goal**
To  check if data meets the specifications outlined in metadata and data dictionary (if exists),  gain familiarity with dataset(surface properties, structure and components), check whether there are problems with the data(content quality assessment) and  Assess potential of data to achieve project objective(s). Exploring data to gain insights for informed choices during data preprocessing: handling missing values, outliers, correct data types, removing duplicates, address data integrity issues. Preprocess data using insights gained to ensure that dataset is reasonably consistent and free from major issues. 

**Activities**
- compare datasets to metadata and data dictionary(if exists)
- check surface properties of datasets: format, number of variables, observations, variable types etc
- check quality content: 
    >> completeness - *Missing values, incomplete records*
    >> Accuracy - *Outliers, data entry errors, duplicates*
    >> consistency - *Inconsistent formats, inconsistent categories, inconsistent representations*
    >> Relevancy: - *Irrelevant variables, outdated data* 
- summary statistics and visual inspections. 
- spend time thinking about variables that will be needed to achieve objective(s)
- Preprocess Data:
    >> Handle Missing Values: Address missing values by imputing or removing them.
    >> Handle Outliers: Identify and address outliers if they exist.
    >> Correct Data Types: Ensure that data types are appropriate for each variable.
    >> Remove Duplicates: Check for and remove duplicate rows if necessary.
    >> Address Data Integrity Issues: Correct any data integrity issues.
- save data preprocessed data to data/processed/01_processed_further_analysis.csv

**Files**
- Refer to the 1.0-sy-Initial-EDA.ipynb for this Initial Data Exploration and Data Preprocessing. 
- Data Dictionary created from results of activities {doc}`data_dictionary` since one didn't exist for comparison. 
- data/01_processed_further_analysis.csv contains prepared data for further analysis.  



## In-depth Exploratory Analysis And Answering Analytical Questions

**Goal**
Perform in-depth analysis to understand distributions of variables, inherent patterns and relatioships between two or more variables. Develop plausible hypothesis to test. Use Insights gained for effective feature engineering. We also answer Analytical questions using visualizations. 

**Activities**

- Distribution Analysis: Explore the distribution of each variable more deeply, using techniques like Kernel Density Estimation (KDE) or more advanced histograms.
- Relationship Analysis: Investigate relationships between variables using scatter plots, correlation matrices, or other methods.
- Feature Engineering: Develop a sketch of how features will be engineered for modelling based on insights gained from the data. 
- Answer Analytical questions with visualization. 

**Resources**

**Files**
- plots created are stored in reports/figures

## Deployment to Power BI


## Stationarity Test

## Feature Scaling & Engineering

## Train and Evaluate 4 or More Models

## Advanced Model Evaluation


## Model Improvements

## Testing of predictions

## Article Writing





## Data Wrangling and Preparation 
Prepare data for modelling

