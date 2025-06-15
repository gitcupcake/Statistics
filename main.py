import pandas as pd
import statistics
import math
import matplotlib.pyplot as plt
import scipy.stats as stats

# 0. Data Read ---------------------------------------------------------------------------------------------------------

# CSV dosyasından verilerioku
df = pd.read_csv("activity.csv")
steps = df[df["Steps"].notnull()]["Steps"].tolist()
n = len(steps)

# 1. Descriptive Statistics --------------------------------------------------------------------------------------------


# Mean
mean_value = statistics.mean(steps)
print(f"Mean (Average daily steps): {mean_value:.2f}")

# Median
median_value = statistics.median(steps)
print(f"Median (Middle value): {median_value}")

# Variance
variance_value = statistics.variance(steps)
print(f"Variance (Measure of dispersion): {variance_value:.2f}")

# Standard Deviation
std_dev_value = statistics.stdev(steps)
print(f"Standard Deviation (Typical deviation from mean): {std_dev_value:.2f}")

# Standard Error
std_error_value = std_dev_value / math.sqrt(n)
print(f"Standard Error of the Mean: {std_error_value:.2f}")


# 2. Data Visualization ------------------------------------------------------------------------------------------------


# Histogram
plt.figure(figsize=(10, 5))
plt.hist(steps, bins=15, edgecolor='black')
plt.title("Histogram of Daily Step Counts")
plt.xlabel("Steps")
plt.ylabel("Number of Days")
plt.grid(True)
plt.show()

# Boxplot
plt.figure(figsize=(5, 7))
plt.boxplot(steps, vert=True, patch_artist=True)
plt.title("Boxplot of Daily Step Counts")
plt.ylabel("Steps")
plt.grid(True)
plt.show()


# 3. Confidence Interval -----------------------------------------------------------------------------------------------


# 95% confidence interval for the mean (z = 1.96)
z_95 = 1.96
margin_of_error = z_95 * std_error_value
ci_lower = mean_value - margin_of_error
ci_upper = mean_value + margin_of_error
print(f"95% Confidence Interval for Mean: [{ci_lower:.2f}, {ci_upper:.2f}]")

# 95% confidence interval for variance using chi-square distribution
alpha = 0.05
df_v = n - 1
chi2_lower = stats.chi2.ppf(alpha / 2, df_v)
chi2_upper = stats.chi2.ppf(1 - alpha / 2, df_v)
ci_variance = ((df_v * variance_value) / chi2_upper, (df_v * variance_value) / chi2_lower)
print(f"95% Confidence Interval for Variance: [{ci_variance[0]:.2f}, {ci_variance[1]:.2f}]")


# 4. Sample Size Estimation --------------------------------------------------------------------------------------------


# z: %90 güven düzeyi için
z_90 = 1.645
# E: izin verilen maksimum hata payı
E = 500  # ±500 adım hata ile ortalama tahmini

sample_of_size = ( (z_90 * std_dev_value) / E ) ** 2
sample_of_size = math.ceil(sample_of_size)
print(f"Sample Size: {sample_of_size}")


# 5. Hypothesis Testing ------------------------------------------------------------------------------------------------


mu = 8000  # Test: ortalama 8000 adım mı?
z = (mean_value - mu) / std_error_value
print(f"Z değeri: {z:.2f}")

if abs(z) > 1.96:
    print("Sonuç: H₀ REDDEDİLİR → Ortalama 8000 değildir.")
else:
    print("Sonuç: H₀ REDDEDİLEMEZ → Ortalama 8000 olabilir.")