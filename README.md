#  Phishing Website Detection using Machine Learning  

This project was completed as part of my **Internship at Global Next Consulting India Pvt. Ltd.**  
The goal is to detect **phishing websites** using machine learning models such as Logistic Regression, Random Forest, and XGBoost.  

---

##  Project Overview
- **Problem**: Phishing websites trick users into revealing sensitive information.  
- **Solution**: Train ML models to classify websites as *Legitimate* (1) or *Phishing* (0).  
- **Dataset**: Kaggle – [Phishing Website Dataset](https://www.kaggle.com/datasets/akashkr/phishing-website-dataset)  

---

##  Project Workflow
1. **Data Collection** → Kaggle dataset  
2. **Data Cleaning** → Removed duplicates & missing values  
3. **Exploratory Data Analysis (EDA)** → Count plots, heatmaps, word clouds  
4. **Model Training** → Logistic Regression, Random Forest, XGBoost  
5. **Evaluation** → Accuracy, Precision, Recall, F1 Score, Confusion Matrix  
6. **Visualization** → Feature importance, ROC–AUC curves  
7. **Deployment Step** → Saved best model as `.pkl` for reuse  

---

##  Results
| Model               | Accuracy | Precision | Recall | F1 Score |
|----------------------|----------|-----------|--------|----------|
| Logistic Regression | ~92%     | 0.91      | 0.90   | 0.91     |
| Random Forest       | ~95%     | 0.95      | 0.95   | 0.95     |
| **XGBoost**         | **97%** | 0.97      | 0.97   | 0.97     |

 **Best Model: XGBoost (~97% Accuracy)**  

---

##  Visualizations
-  Count Plot (Phishing vs Legitimate websites)  
-  Heatmap (Feature correlations)  
-  WordClouds (Phishing vs Legitimate patterns)  
-  Feature Importance Plot  
-  ROC–AUC Curve (Model comparison)  

---

##  Key Takeaways
- Machine learning can detect phishing websites with **high accuracy**  
- **XGBoost** outperformed other models  
- Features like HTTPS usage, URL length, and suspicious characters are **strong phishing indicators**  
- Final model was saved for **future deployment**  

---

##  Future Scope
- Deploy as a **browser extension** for real-time phishing detection  
- Extend dataset with **new phishing patterns**  
- Integrate into **cybersecurity tools**  

---

##  Files in this Repository
-  `Phishing_Detection.ipynb` → Colab Notebook (full code)  

---

##  Acknowledgements
- Internship by **Global Next Consulting India Pvt. Ltd.**  
- Dataset from **Kaggle**  

---

