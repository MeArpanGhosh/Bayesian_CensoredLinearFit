import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate Corona_flux_data.csv
# This should have 6 sources (5 for fitting + 1 IRS6 for plotting only)
n_sources = 30

sources = [f"Source_{i+1}" for i in range(n_sources)]
sources[-1] = "Source_exclude"  # Last one is IRS6 which will be excluded from fitting

# Generate realistic-looking flux values
# NIR_flux in range ~1e-14 to 1e-12 erg/s/cm^2
Nir_flux = 10 ** np.random.uniform(-18, -12, n_sources)
Nir_flux_err = Nir_flux * np.random.uniform(0.1, 0.3, n_sources)



# Radio_flux in range ~0.1 to 2.0 mJy (log scale: -1 to 0.3)
# Create correlation with br_gamma_flux (power law with some scatter)
log_Nir = np.log10(Nir_flux)
true_slope = 0.7
true_intercept = -9.5
log_radio = true_slope * log_Nir + true_intercept + np.random.normal(0, 0.15, n_sources)
Radio_flux = 10**log_radio
Radio_flux_err = Radio_flux * np.random.uniform(0.1, 0.25, n_sources)
yso_class = np.random.choice(['ClassI', 'ClassII', 'ClassIII'], n_sources, p=[0.2, 0.5, 0.3])

df1 = pd.DataFrame({
    'Source': sources,
    'YSO Classification': yso_class,
    'Nir_Flux[erg/s/cm^2]': Nir_flux,
    'Nir_Flux_err[erg/s/cm^2]': Nir_flux_err,
    'Radio_Flux[mJy]': Radio_flux,
    'Radio_Flux_err[mJy]': Radio_flux_err
})

df1.to_csv('Detection_data.csv', index=False)
print("Created Detection_data.csv")
print(df1)

# Generate BrGamma_sources_coords_updated_radiolimits2.csv
# This contains upper limit data for Class II and Class I sources
n_upper_limits = 20

names_ul = [f"UL_Source_{i+1}" for i in range(n_upper_limits)]
yso_class = np.random.choice(['ClassI', 'ClassII', 'ClassIII'], n_upper_limits, p=[0.2, 0.5, 0.3])

# Generate upper limit values (should be lower than detections)
Nir_flux_ul = 10 ** np.random.uniform(-19, -15, n_upper_limits)
log_Nir_ul = np.log10(Nir_flux_ul)

logRadio_flux_limit = true_intercept + true_slope * log_Nir_ul - np.random.uniform(0.3, 1.0, n_upper_limits)
Radio_flux_ul = 10 ** logRadio_flux_limit



df2 = pd.DataFrame({
    'Name': names_ul,
    'YSO Classification': yso_class,
    ' sigma_radio [mJy]': Radio_flux_ul,
    'sigma_nir [erg / s/cm2]':Nir_flux_ul
})

df2.to_csv('Upper_limit_data.csv', index=False)
print("\nCreated Upper_limit_data.csv")
print(df2)

print("\n" + "="*60)
print("Data generation complete!")
print("="*60)
print("\nGenerated files:")
print("1. Detection_data.csv - Main detection data (20 sources)")
print("2. Upper_limit_data.csv - Upper limits (15 sources)")
print("\nYou can now run your MCMC analysis code with these files.")
print("\nNote: Update the file paths in your main script to:")
print("  - 'Detection_data.csv'")
print("  - 'Upper_limit_data.csv'")
