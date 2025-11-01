# 🌍 Soil Pollution Detection using Hidden Markov Models (HMM)

This project models soil and groundwater pollution as a **Hidden Markov Model (HMM)** to estimate true pollution levels from noisy sensor readings.
By using probabilistic inference (forward and Viterbi algorithms), the model predicts how likely the site is to be **highly polluted** and identifies the **most probable pollution path** over time.

---

## 🧩 Background

Industrial activities such as oil spills, waste dumps, and chemical leaks often contaminate soil and water.
Since the **true pollution state** cannot be observed directly, agencies rely on **sensor readings** (like nitrate, lead, or ammonia levels) that may include noise or errors.

To model this uncertainty, we use an **HMM** where:

* **Hidden states** represent the true pollution level.
* **Observations** represent what instruments detect.
* **Transition probabilities** model how pollution evolves.
* **Observation probabilities** model how reliable the sensors are.

---

## ⚙️ Model Overview

### **Hidden States (True Pollution Levels)**

| State               | Description                  |
| ------------------- | ---------------------------- |
| Clean               | Safe chemical concentrations |
| Moderately Polluted | Slight contamination         |
| Highly Polluted     | Exceeds safe thresholds      |

### **Observations (Sensor Readings)**

| Observation       | Description                     |
| ----------------- | ------------------------------- |
| Safe Level        | Readings within safe limits     |
| Slightly Elevated | Moderate contamination detected |
| Hazardous         | Dangerous contamination levels  |

---

### **Transition Probabilities (T)**

| From → To | Clean | Moderate | High |
| --------- | ----- | -------- | ---- |
| Clean     | 0.8   | 0.2      | 0.0  |
| Moderate  | 0.1   | 0.7      | 0.2  |
| High      | 0.0   | 0.3      | 0.7  |

---

### **Observation Probabilities (O)**

| State    | Safe Level | Slightly Elevated | Hazardous |
| -------- | ---------- | ----------------- | --------- |
| Clean    | 0.9        | 0.1               | 0.0       |
| Moderate | 0.2        | 0.6               | 0.2       |
| High     | 0.0        | 0.3               | 0.7       |

---

## 🧮 Example Task

**Given sensor readings:**

```
["Slight Elevated", "Hazardous", "Hazardous"]
```

### The program computes:

1. The **probability** that the site is *Highly Polluted* after these readings.
2. The **most likely hidden pollution path** explaining the observations.
3. A **natural language interpretation** of results.

---

## 🚀 How to Run

### 1️⃣ Install Dependencies

```bash
pip install pomegranate numpy
```

### 2️⃣ Run the Program

```bash
python soil_pollution.py
```

### 3️⃣ Example Output

```
Final probability distribution after 3 readings:
   Clear    = 0.012
   Moderate = 0.214
   High     = 0.774

Therefore, probability the site is HIGH = 77.40%

Most likely hidden path = Moderate → High → High

Interpretation:
After 3 sensor readings, the model estimates there is a 77.40% chance
the site is HIGHLY polluted. The most likely pollution evolution was:
Moderate → High → High.
```

---

## 🧠 Concepts Used

* Hidden Markov Models (HMMs)
* Forward Algorithm (probability estimation)
* Viterbi Algorithm (most likely path inference)
* Probabilistic reasoning for environmental monitoring

---

## 📈 Applications

* Environmental monitoring systems
* Water and soil quality tracking
* Predictive contamination modeling
* Uncertainty-aware pollution analysis

---

## 🧑‍💻 Technologies

* **Python**
* **pomegranate** (for probabilistic modeling)
* **NumPy**

