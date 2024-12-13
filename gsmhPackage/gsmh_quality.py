import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
import numpy as np

#Method to create plots checking normality of columns
def check_normality(df, columns):
    #for each column
    for col in columns:
        #create a QQ plot for all non null values
        plt.figure(figsize=(12, 6))
        
        plt.subplot(1, 2, 1)
        plt.hist(df[col].dropna(), bins=30)
        plt.title(f'{col} Histogram')
        
        plt.subplot(1, 2, 2)
        stats.probplot(df[col].dropna(), dist="norm", plot=plt)
        plt.title(f'{col} Q-Q Plot')
        
        plt.show()

#This checks linearity, not entirely necessary for the DNN but still work checking
def check_linearity(df, columns, target_col):
    for col in columns:
        plt.figure(figsize=(8, 6))
        plt.scatter(df[col], df[target_col])
        plt.title(f'{col} vs {target_col}')
        plt.xlabel(col)
        plt.ylabel(target_col)
        plt.show()

#used after getting the model predictions
def check_homoscedasticity(targets, predictions):
    # Ensure targets and predictions have the same length
    if len(targets) != len(predictions):
        raise ValueError("targets and predictions must be the same size")
    
    targets = np.asarray(targets) 
    predictions = np.asarray(predictions)
    # Check for NaN values
    if np.isnan(targets).any() or np.isnan(predictions).any(): 
        raise ValueError("targets and predictions must not contain NaN values")

    # Calculate residuals
    residuals = targets - predictions
    
    print("\n\n len of residuals")
    print(len(residuals))
    print("\n\n len of predictions")
    print(len(predictions))

    # for i in range(0, len(residuals)):
    #     print(f"prediction: {predictions[i]}")
    #     print(f"residual: {residuals[i]}")
    
    # Plot residuals vs. predicted values
    plt.figure(figsize=(8, 6))
    plt.scatter(predictions, residuals)
    plt.axhline(y=0, color='r', linestyle='--')
    plt.title('Residuals vs Predicted Values')
    plt.xlabel('Predicted Values')
    plt.ylabel('Residuals')
    plt.show()

#correlation check, pretty similar to what was done before
def check_multicollinearity(df, columns):
    corr_matrix = df[columns].corr()
    
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title('Feature Correlation Matrix')
    plt.show()

#method to check distribution of a column, can be used to check if the train and 
#test sets are distributed well
def check_target_distribution(df, target_col):
    plt.figure(figsize=(8, 6))
    plt.hist(df[target_col], bins=30)
    plt.title(f'{target_col} Distribution')
    plt.xlabel(target_col)
    plt.ylabel('Frequency')
    plt.show()




