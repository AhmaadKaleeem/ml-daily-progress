# Linear Regression

### 🔹 Dependent and Independent Variables
* **Dependent variable ($Y$):** The outcome we aim to predict or explain; it depends on another variable.
* **Independent variable ($X$):** The predictor or explanatory variable; its values are known or controlled.

**Examples:**
* Income → Expenditure (expenditure is dependent, income is independent)
* Parents’ height → Child’s height
* Study hours → Exam marks

### 🔹 Regression Equation
The simple linear regression model relates $Y$ and $X$ by:

$$Y = \alpha + \beta X + \varepsilon$$

* $\alpha$ = **Intercept** (value of $Y$ when $X = 0$)
* $\beta$ = **Slope** (rate of change of $Y$ per unit change in $X$)
* $\varepsilon$ = **Random error term**

---

##  Estimating Parameters

### 🔹 Intercept ($\alpha$)
The intercept is the predicted value of the dependent variable when the independent variable equals zero. It is calculated as:

$$\alpha = \bar{Y} - \beta\bar{X}$$

*(where $\bar{Y}$ and $\bar{X}$ are the sample means of $Y$ and $X$)*

### 🔹 Slope ($\beta$) – Rate of Change
The slope measures how much the dependent variable changes, on average, for a one‑unit increase in the independent variable. It is computed with:

$$\beta = \frac{\sum XY - n\bar{X}\bar{Y}}{\sum X^2 - n\bar{X}^2}$$

---

##  Interpreting the Model

### 🔹 Predicting Expenditure from Income (Illustrative Data)

| Observation | Income ($X$) (₹ 000) | Expenditure ($Y$) (₹ 000) |
| :--- | :--- | :--- |
| 1 | 1.0 | 4.3 |
| 2 | 2.0 | 5.6 |
| 3 | 3.0 | 6.9 |
| 4 | 4.0 | 8.2 |
| 5 | 5.0 | 9.5 |

**Using the formulas above:**
* Means: $\bar{X}=3$, $\bar{Y}=6.9$
* Slope calculation: 
    $$\beta = \frac{\sum XY - n\bar{X}\bar{Y}}{\sum X^2 - n\bar{X}^2} = \frac{115.5 - 5(3)(6.9)}{55 - 5(3)^2} = 0.65$$
* Intercept calculation:
    $$\alpha = \bar{Y} - \beta\bar{X} = 6.9 - 0.65(3) = 4.95$$

**Regression line:**
$$\hat{Y} = 4.95 + 0.65X$$

> **Interpretation:** For every additional ₹ 1,000 of income, expected expenditure rises by about ₹ 650.

### 🔹 Height of Child from Parents’ Height
* **Dependent:** Child’s height
* **Independent:** Parents’ average height
* *Interpretation:* The slope tells how many centimeters a child gains for each centimeter increase in parental height.

### 🔹 Exam Marks from Study Hours
* **Dependent:** Exam score
* **Independent:** Hours studied
* *Interpretation:* A positive slope indicates higher marks with more study time; the intercept predicts a baseline score when no study occurs.

---

##  Formulas and Computations

| Symbol | Meaning |
| :--- | :--- |
| $n$ | Number of observations |
| $\sum X$ | Sum of all $X$ values |
| $\sum Y$ | Sum of all $Y$ values |
| $\sum XY$ | Sum of products ($X_iY_i$) |
| $\sum X^2$ | Sum of squared $X$ values |
| $\bar{X}$ | Mean of $X$ ($\frac{\sum X}{n}$) |
| $\bar{Y}$ | Mean of $Y$ ($\frac{\sum Y}{n}$) |

**Step‑by‑step Slope Calculation:**
1. Compute $\sum X$, $\sum Y$, $\sum XY$, and $\sum X^2$.
2. Find means $\bar{X}$ and $\bar{Y}$.
3. Plug into the slope formula: $$\beta = \frac{\sum XY - n\bar{X}\bar{Y}}{\sum X^2 - n\bar{X}^2}$$

**Step‑by‑step Intercept Calculation:**
1. Use the slope ($\beta$) from above.
2. Compute the intercept: $$\alpha = \bar{Y} - \beta\bar{X}$$

### Rate of Change Interpretation
* **Positive $\beta$:** $Y$ increases as $X$ increases.
* **Negative $\beta$:** $Y$ decreases as $X$ increases.
* **Magnitude of $\beta$:** The size of the expected change in $Y$ for a one‑unit change in $X$.

---

## 🛠 Practical Use
* **Estimation:** Plug a new $X$ value into the equation $\hat{Y} = \alpha + \beta X$ to obtain a predicted $Y$.
* **Model assessment:** Compare observed $Y$ with predicted $\hat{Y}$; the residuals ($Y - \hat{Y}$) indicate the quality of the fit.