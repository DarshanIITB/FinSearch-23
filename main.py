import numpy as np
from scipy.stats import norm

# variables
r = 0.01 # risk-free rate
S = 30 # initial stock price
K = 40 # strike price
T = 240/365 # maturity in years
sigma = 0.30 # volatility

def blackScholes(r, S, K, T, sigma, type):
    """
    params:
        r: risk-free rate
        S: initial stock price
        K: strike price
        T: maturity in years
        sigma: volatility
        type: call or put
    return:
        option price
    Calculates the Black-Scholes option price for a call or put option.
    """
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        if type == 'call':
            return S*norm.cdf(d1, 0, 1) - K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        elif type == 'put':
            return K*np.exp(-r*T)*norm.cdf(-d2, 0, 1) - S*norm.cdf(-d1, 0, 1)
    except:
        print("Please check if all inputs are valid.")

print("Option price is: ", round(blackScholes(r, S, K, T, sigma,'put'), 2) )