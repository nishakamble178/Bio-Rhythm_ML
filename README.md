### Bio-Rhythm

**Bio-Rhythm** is a behavioral biometric security platform that identifies and authenticates users based on their unique typing patterns. Instead of relying on traditional passwords, it analyzes the millisecond-level timing of keystrokes—specifically how long keys are held and the latency between presses—to create a "digital rhythm" that is nearly impossible to forge.

It serves as a non-intrusive security layer that can distinguish between an authorized user and an imposter with high precision.

## **Features**

### **Identity Verification**
* **High-Accuracy Prediction:** Achieves a **94.49% accuracy** rate in identifying users.
* **Neural Confidence:** Provides a real-time probability score indicating the AI's certainty.
* **Imposter Detection:** Instantly flags "Signature Mismatches" when typing patterns deviate from the stored baseline.

### **Biometric Analytics**
* **Real-time Simulation:** Interactive sliders for Hold Duration (H), Down-Down Latency (DD), and Up-Down Latency (UD).
* **Visual Comparison:** Generates live Area Charts comparing the current user's rhythm against the system's authorized baseline.
* **Session Monitoring:** Tracks timing nuances across 33 different keystroke features.

### **Security Dashboard**
* **Status Reporting:** Clear visual indicators for "Authenticated" or "Rejected" status.
* **Data Normalization:** Built-in preprocessing that scales raw timing data for consistent analysis across different sessions.

---

## **Technology Stack**

### **Frontend & UI**
* **Streamlit:** For the interactive web dashboard and real-time visualizations.
* **Matplotlib / Plotly:** For generating the biometric signature graphs.

### **Machine Learning & Backend**
* **Python:** The core programming language.
* **Scikit-learn:** Used for the **Random Forest Classifier** and **StandardScaler** implementation.
* **Pandas & NumPy:** For high-speed data manipulation and feature engineering.

### **Models & Storage**
* **Random Forest (Ensemble Learning):** The primary decision engine trained on 100+ decision trees.
* **Joblib / Pickle:** For storing and loading the pre-trained model and scaler weights.

---

## **Data Structure (Feature Vector)**

Unlike a traditional database with tables, this system operates on a **High-Dimensional Feature Vector**. The system processes 33 specific timing features for every prediction:


### **The Feature Set includes:**

* **H (Hold Time):** The duration from the moment a key is pressed to when it is released.
* **DD (Down-Down):** The time elapsed between two consecutive key-down events.
* **UD (Up-Down):** The time elapsed between a key-release and the next key-press.

### **Prediction Flow:**
1.  **Input:** User provides a sequence of 33 timing values.
2.  **Scaling:** Data is passed through a `StandardScaler` to match the training distribution.
3.  **Inference:** The **Random Forest** model processes the 33 features.
4.  **Output:** Returns the `User_ID` with the highest probability and the associated confidence score.
