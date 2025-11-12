# Summary – APMonitor Modeling Language

An APMonitor model is structured into several sections: **constants, parameters, variables, intermediates, equations, objects,** and **connections.**

* **Constants:** Fixed values that never change, often used to define array sizes.
* **Parameters:** Normally fixed values that can be adjusted by users or optimized to minimize an objective.
* **Variables:** Computed by the model’s equations; may be measured or controlled to meet targets.
* **Intermediates:** Explicit expressions computed from previously defined elements (not implicit equations).
* **Equations:** Define system relationships — can be equality (`f(dx/dt,x,p)=0`), inequality (`g(dx/dt,x,p)>0`), or objective expressions (using *maximize* or *minimize*).
* **Objects:** Object-oriented model components that include their own parameters, variables, and equations.
* **Connections:** Equality constraints linking variables or parameters across models.

Equations are solved simultaneously, but initialization follows the order of appearance in the model file.

Additionally, APMonitor classifies:

* **Parameters:** as **Fixed Values (FVs)** or **Manipulated Variables (MVs)**.
* **Variables:** as **State Variables (SVs)** or **Controlled Variables (CVs)**.

These classifications, common in process systems engineering, distinguish inputs (MVs), outputs (CVs), disturbances (FVs), and key monitored states (SVs), and are typically set through MATLAB or Python interfaces.

## Summary – GEKKO Python Library

**GEKKO** is an object-oriented Python library that provides a local interface to **APMonitor**. It supports **machine learning** and **optimization** involving **mixed-integer** and **differential-algebraic equations**, using powerful solvers for **LP, QP, NLP, MILP,** and **MINLP** problems.

GEKKO can operate in multiple modes, including:

* **Parameter regression**
* **Data reconciliation**
* **Real-time optimization**
* **Dynamic simulation**
* **Nonlinear predictive control**

## Summary – Time Discretization

Time discretization balances **accuracy** and **computational speed** in numerical simulations.

* **More time points** improve accuracy but increase computation time.
* **Fewer points** are sufficient when system dynamics are slow or near steady state.
* A **hybrid approach** uses finer discretization during **fast dynamics** (e.g., right after a step input) and coarser discretization during **slow dynamics**.

The **dominant time constant** represents how quickly a system approaches steady state — it’s roughly the time to reach **63% of the total response** after a step input. It is often identified empirically by simulation.

When using **recorded dynamic data**, the simulation step size should match the data frequency for accurate comparison. However, this can be computationally expensive. To reduce cost, **downsampling** techniques such as moving averages or less frequent predictions can be applied during **dynamic data reconciliation**.

## Summary – Slack Variables, Conditional Statements, and Model Complexity

* **Slack Variables:**
  Inequality constraints (e.g., `g(dx/dt, x, p) > 0`) are converted into equality constraints with a **slack variable** (`g(dx/dt, x, p) = s`, where `s > 0`).
  This transformation helps solvers—especially **interior-point methods**—by ensuring the initial guess lies within the feasible region.
  Both **APMonitor** and **GEKKO** automatically perform this conversion for all inequalities.

* **Conditional Statements:**
  Discontinuous functions like `abs`, `if...then`, `min`, `max`, and `sign` can cause solver difficulties because they lack smooth derivatives.
  To handle them efficiently, models can be reformulated as:

  * **MPECs (Mathematical Programs with Equilibrium Constraints)**, or
  * **Binary-variable formulations**, which turn equation elements on or off smoothly.

* **Model Complexity:**
  The right model complexity depends on the **application goal** and **computational constraints**:

  * **Simple or reduced-order models** suit real-time or embedded systems where speed matters.
  * **Detailed models** are appropriate when accuracy outweighs time concerns.
    A good strategy is to **start simple and add complexity only when necessary** to capture essential input-output behavior.

