import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def polynomial_fit(x_values, y_values, degree):
    return np.polyfit(x_values, y_values, degree)

def format_equation(coeffs):
    terms = [f"{coeff:.4f}x^{i}" for i, coeff in enumerate(reversed(coeffs))]
    return " + ".join(terms).replace("x^1", "x").replace("x^0", "")

st.title("📈 Least Squares Fitting Calculator")
st.markdown("Enter X and Y values as comma-separated lists (e.g., `1,2,3,4`).")

x_input = st.text_input("X values")
y_input = st.text_input("Y values")
fit_type = st.selectbox("Fitting Type", ["Linear", "Polynomial"])
degree = 1

if fit_type == "Polynomial":
    degree = st.slider("Select Degree", 2, 6, step=1)

if st.button("Fit Curve"):
    try:
        x_vals = list(map(float, x_input.strip().split(',')))
        y_vals = list(map(float, y_input.strip().split(',')))

        if len(x_vals) != len(y_vals):
            st.error("❌ X and Y must have the same number of values.")
        else:
            coeffs = polynomial_fit(x_vals, y_vals, degree)
            eqn = format_equation(coeffs)
            st.success(f"Fitted Equation: y = {eqn}")

            x_range = np.linspace(min(x_vals), max(x_vals), 100)
            y_fit = np.polyval(coeffs, x_range)

            fig, ax = plt.subplots()
            ax.scatter(x_vals, y_vals, color='blue', label='Data Points')
            ax.plot(x_range, y_fit, color='red', label='Fitted Curve')
            ax.legend()
            st.pyplot(fig)

    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")
