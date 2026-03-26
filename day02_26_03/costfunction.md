## Cost Function (Linear Regression)

### Purpose
The **cost function** measures the aggregate error between predicted values and actual values across all data points.

- A **lower cost** indicates a better model fit.
- A **higher cost** indicates poorer prediction accuracy.

---

### Mathematical Formulation

#### 1. Squared Error Cost (Mean Squared Error)

J(θ) = (1 / 2m) * Σ(i = 1 to m) (yᵢ - ŷᵢ)²

**Description:**
- Averages the squared differences between actual and predicted values.
- The factor (1 / 2m) simplifies derivative calculations.

---

#### 2. Absolute Error Cost (Mean Absolute Error)

J(θ) = (1 / m) * Σ(i = 1 to m) |yᵢ - ŷᵢ|

**Description:**
- Averages the absolute differences.
- Less sensitive to outliers.

---

### Notation

- m  = Number of data points  
- yᵢ = Actual value of the i-th data point  
- ŷᵢ = Predicted value of the i-th data point  
- J(θ) = Cost function dependent on model parameters θ