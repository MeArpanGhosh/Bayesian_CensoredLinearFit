# Bayesian_CensoredLinearFit
This notebook performs a Bayesian linear regression using PyMC  to study the relationship between two quantities, here they are: 1. near-infrared (NIR) fluxes and 2. radio fluxes of astronomical sources, accounting for both detections and upper limits (non-detections).

🔹 Overview

The regression is performed in logarithmic space to model a power-law relation between NIR and radio fluxes:

log10( Radio_flux ) = 𝛼 + 𝛽 * log10( NIR_flux )

where

α → intercept

β → slope (power-law index)

The analysis combines:

a Gaussian likelihood for detections

a cumulative (censored) likelihood for upper limits

This approach enables the use of incomplete data while preserving physical consistency.

🔹 Features

✅ Bayesian inference using PyMC’s NUTS sampler

✅ Handles heteroscedastic uncertainties (different errors per data point)

✅ Incorporates upper limits correctly in the regression

✅ Estimates posterior distributions for slope, intercept, and intrinsic scatter

✅ Provides comprehensive model diagnostics:

Posterior summary statistics (mean, SD, HDI, ESS, R̂)

Slope–intercept correlation

Bayesian Information Criterion (BIC)

Pseudo R² for detections

Correlation coefficient (r) between data and model

🔹 Results Visualization

The notebook generates:

Posterior distributions of slope, intercept, and intrinsic scatter

Traceplots for sampling diagnostics

Regression plot in log–log space showing:

Detected sources with error bars

Upper limits as downward arrows

Median regression line

Random posterior samples for visualizing uncertainty



Make sure your CSV files are in the same directory:

File	Description
detections.csv	Flux data for detected sources
upper_limits.csv	Flux data for upper-limit (non-detected) sources
🔹 Repository Structure
📦 your-repo-name
 ┣ 📜 for_github.ipynb        ← Main Bayesian regression notebook
 ┣ 📜 detections.csv          ← Detection dataset
 ┣ 📜 upper_limits.csv        ← Upper limit dataset
 ┣ 📜 README.md               ← Project documentation
 
🔹 Dependencies
Package	Version (min)
Python	3.10+
numpy	1.25
pandas	2.0
matplotlib	3.8
pymc	5.10
arviz	0.16
scipy	1.11



