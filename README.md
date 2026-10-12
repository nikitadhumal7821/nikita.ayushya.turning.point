# nikita.ayushya.turning.point
"AI-based horoscope and personality prediction system using machine learning with Ayushya turning point algorithm."
## Algorithm: Ayushya Turning Point

* **Objective:** To compute deterministic life turning-point timelines and integrate them with machine learning classification for personality and horoscope prediction.
* **Inputs:** Date of birth, time of birth, place of birth, and chart-derived astrological features.
* **Outputs:** Predicted horoscope category, personality-oriented characteristics, and calculated turning-point years.

### Phase 1: Training Phase
1. **Dataset Ingestion:** Load the structured horoscope dataset containing historical records and class labels.
2. **Data Preprocessing:** Clean missing values, encode categorical variables, and prepare numerical features into a model-ready format.
3. **Class Balancing:** Apply WSMOTE to address and balance underrepresented classes in the dataset.
4. **Model Training & Comparison:** Train and evaluate six baseline classifiers: Decision Tree, SVC, Random Forest, Multinomial Logistic Regression, Naïve Bayes, and KNN.
5. **Model Selection & Persistence:** Select Random Forest as the final optimal model and save it using Joblib.

### Phase 2: Inference Phase (Ayushya Turning Point)
1. **User Input Collection:** Capture user inputs via the Streamlit interface, including date, time, and place of birth.
2. **Input Validation & Preprocessing:** Validate inputs and pass them through the same preprocessing pipeline used during training.
3. **Feature Engineering & Temporal Calculation:** Extract the birth year, sum its digits, and recursively calculate future turning-point milestones.
4. **Model Prediction:** Load the saved Random Forest model and feed the processed feature vector into it.
5. **Result Presentation:** Display the final predicted horoscope category, personality traits, and turning-point timeline on the Streamlit interface.
