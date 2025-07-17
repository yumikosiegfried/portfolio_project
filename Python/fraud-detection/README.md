# Credit Card Fraud Detection

This project aims to detect fraudulent credit card transactions using machine learning (ML) models on Kaggle Credit Card Fraud Detection dataset.

The goal is to find the best model for predicting fraudulent transactions in real-time. After the model selection and training process, a production-ready pipeline is created for deployment. The final pipeline can be run on a single new transaction and predict quickly whether it is a fraud or not, using the pre-trained model.

## Project Overview

- Use Kaggle Credit Card Fraud dataset (492 fraudulent transactions out of 284,807 transactions)
- Compare several ML models, including both supervised and unsupervised models, for their abilities to correctly identify fraudulent transactions. The models considered are: logistic regression, Random Forest, XGBoost, LightGBM, Isolation Forest, Local Outlier Factor (LOF), and Support Vector Machine (SVM)
- Choose the best performing model and build a fraud prediction pipeline for new transactions
- Apply the pipeline to a simulated data point as a use example

## Dataset

The input dataset (`creditcard.csv`) as well as X_res.pkl, results.pkl, and X_train_raw.pkl are **NOT included** in this repository due to their large sizes (100MB+) and GitHub file size limits. 

One can download the original csv file directly from Kaggle: <https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/data>.

The .pkl files should be created automatically by running the notebooks.

If one wishes to replicate this project, after downloading the dataset from Kaggle, save the `creditcard.csv` file in the following directory within the project: ".../portfolio_project/Python/fraud-detection/data"

## Folder Structure
```
fraud-detection/
├── data/                # Raw and processed .pkl files, except for Kaggle Data (too large)
├── notebooks/           # Includes Jupyter notebooks for exploratory data analysis (EDA), preprocessing, modeling, tuning, and pipeline creation as well as visualizations created in the notebooks
└── README.md            # Project overview, descriptions, and summary of results
```

## Methods

1. Perform EDA on the Kaggle dataset including descriptive statistics and visualizations (see notebooks/01_eda.ipynb)
2. Preprocess the raw data (log transform and scale 'Amount', drop unnecessary covariates) (see notebooks/02_preprocessing.ipynb)
3. Narrow down models to 2-3 top performing models by comparing the performances of logistic regression, Random Forest, XGBoost, LightGBM, Isolation Forest, Local Outlier Factor (LOF), and Support Vector Machine (SVM) under default parameters. Evaluate performance based on ROC curve and its corresponding AUC value, Precision-Recall curve and its corresponding AUC value, runtime, recall, precision, F1 score, and accuracy (see notebooks/03_modeling.ipynb)
4. Tune parameters for the top performing models from step 3, and choose the best tuned model based on the same set of metrics (see notebooks/04_hyperparameter_tuning.ipynb)
5. Create a pipeline for new data points using the tuned model from step 4 (see notebooks/05_pipeline.ipynb)
6. Provide an example of the pipeline application using a simulated data point (see notebooks/05_pipeline.ipynb)

## Tools

- Python
    - pandas
    - numpy
    - joblib
    - time
    - matplotlib
    - seaborn
    - SMOTE
    - scikit-learn
        - LogisticRegression, RandomForestClassifier, IsolationForest, XGBClassifier, LGBMClassifier, SVC, SGDClassifier, CalibratedClassifierCV, classification_report, roc_auc_score, confusion_matrix, roc_curve, precision_recall_curve, auc, f1_score, accuracy_score, precision_score, recall_score, Pipeline, RobustScaler, train_test_split, TSNE, GridSearchCV
- JupyterNotebook

## Summary of Results

- In the first round of model selection to narrow down to 2-3 models for hyperparameter tuning, **XGBoost**, **Random Forest**, and **LightGBM** were chosen due to their superior precisions and F1 scores as well as competitive ROC/PR AUC, recall, and accuracy values

- After hyperparameter tuning and comparison of tuned models, XGBoost was chosen for its highest precision and F1 score on the test dataset, with comparable ROC/PR AUC, recall, and accuracy values

| Model         | Precision | Recall | F1 Score | Accuracy |
|--------------:|----------:|-------:|---------:|---------:|
| XGBoost       | 0.8173    | 0.8673 | 0.8416   | 0.9994   |
| Random Forest | 0.8095    | 0.8673 | 0.8374   | 0.9994   |
| LightGBM      | 0.6942    | 0.8571 | 0.7671   | 0.9991   |
 

## Model Comparison Plots

For all models:
- ROC Curve (see notebooks/roc_curve_all_models.png)
- Precision-Recall Curve (see notebooks/PR_curve_all_models.png)
- Evaluation Metric Bar Chart (see notebooks/evaluation_metrics_all_models.png)

For tuned models:
- ROC Curve (see notebooks/roc_curve_tuned_models.png)
- Precision-Recall Curve (see notebooks/PR_curve_tuned_models.png)
- Evaluation Metric Bar Chart (see notebooks/evaluation_metrics_tuned_models.png)

## Final Model Pipeline

- Implemented using Pipeline and a custome Preprocessor class
- Saved to disc using joblib for deployment
- Accepts raw transaction data and returns fraud probability and predicted label

**Sample Application**
```
new_data = df.sample(n = 1, random_state = 42)
result = predict_fraud(new_data)
print(result[['fraud_probability','predicted_fraud']])
```

## Note

This project is for demonstration and it uses a single train/test split. In practice, it is best to reserve a third set (validation dataset) to perform the final evaluation of the model, but since this is for a demonstration, the final evaluation of the model is simply done using the test dataset

## Contact

If you would like to collaborate or provide feedback, please contact me on www.linkedin.com/in/yumiko-siegfried-95b61a232