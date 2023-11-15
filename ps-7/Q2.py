import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def logistic_function(x, beta0, beta1):
    return 1 / (1 + np.exp(-(beta0 + beta1 * x)))

def negative_log_likelihood(parameters, x, y):
    machine_precision = 1e-16  # avoid divide by 0 error
    beta0 = parameters[0]
    beta1 = parameters[1]
    likelihood_list = [
        y[i] * np.log(logistic_function(x[i], beta0, beta1) / (1 - logistic_function(x[i], beta0, beta1) + machine_precision))
        + np.log(1 - logistic_function(x[i], beta0, beta1) + machine_precision)
        for i in range(len(x))
    ]
    total_likelihood = np.sum(np.array(likelihood_list))
    return -total_likelihood

def covariance_matrix(hessian_inv, variance):
    return hessian_inv * variance

def parameter_uncertainty(hessian_inv, variance):
    covariance = covariance_matrix(hessian_inv, variance)
    return np.sqrt(np.diag(covariance))

# Load data
ages, responses = np.loadtxt("//Users/nancyshi/Desktop/phys-ga2000/ps-7/survey.csv", delimiter=",", skiprows=1, unpack=True)

# Initial guess
initial_parameters = np.array([0.5, 0.5])

# Minimize negative log-likelihood
fit_result = optimize.minimize(negative_log_likelihood, x0=initial_parameters, args=(ages, responses))
hessian_inverse = fit_result.hess_inv
fit_variance = fit_result.fun / (len(responses) - len(initial_parameters))
fit_uncertainty = parameter_uncertainty(hessian_inverse, fit_variance)

# Print results
print('Optimized Parameters (beta0, beta1): ', fit_result.x)
print('Parameter Uncertainty: ', fit_uncertainty)
print('Covariance Matrix: ', covariance_matrix(hessian_inverse, fit_variance))

# Plot the data and logistic model
optimized_beta0, optimized_beta1 = fit_result.x
plt.scatter(ages, responses, color='blue', label='Data Points')
x_values = np.linspace(min(ages), max(ages), 100)
y_predictions = logistic_function(x_values, optimized_beta0, optimized_beta1)
plt.plot(x_values, y_predictions, color='red', label='Logistic Model')
plt.xlabel('Age')
plt.ylabel('Probability (Yes)')
plt.title('Probability of Respondent')
plt.legend()
plt.show()
