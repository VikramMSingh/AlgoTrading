import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime,date
import numpy as np
from scipy.stats import norm

def risk_calculator(ticker):
    ms=pd.read_csv("data_files/hist_10y/%s.csv" %ticker)

    # ## Distribution of Log return


    ms['LogReturn'] = np.log(ms['Close']).shift(-1) - np.log(ms['Close'])
    ms.dropna()

    # Plot a histogram to show the distribution of log return of stock.

    mean_sample=ms['LogReturn'].mean()
    std_sample=ms['LogReturn'].std(ddof=1)
    sample=ms['LogReturn'].shape[0]

# Confidence Interval - % chance that average return is between these intervals
    sample_std=std_sample/sample**0.5
    z_left=norm.ppf(0.05)
    z_right=norm.ppf(0.95)
    interval_left=mean_sample+(z_left*sample_std)
    interval_right=mean_sample+(z_right*sample_std)

    density=pd.DataFrame()
    density['x'] = np.arange(ms['LogReturn'].min()-0.01, ms['LogReturn'].max()+0.01, 0.001)
    density['pdf'] = norm.pdf(density['x'], mean_sample, std_sample)

    ms['LogReturn'].hist(bins=50, figsize=(15, 8))
    plt.plot(density['x'], density['pdf'], color='red')
    plt.show()

# ## Calculate the probability of the stock price will drop over a certain percentage in a day
# probability that the stock price will drop over 5% in a day

    prob_return1 = norm.cdf(-0.05, mean_sample, std_sample)
    #print('The Probability of 5% drop in a day is ', prob_return1)


    #Probability of a 5% gain in a day
    prob_return3 = norm.cdf(0.05,mean_sample,std_sample)


# ## Calculate the probability of the stock price will drop over a certain percentage in a year
# drop over 40% in 220 days
    mu220 = 220 * mean_sample
    sigma220 = (220 ** 0.5 * std_sample)
    drop40 = norm.cdf(-0.4, mu220, sigma220)


# drop over 20% in 220 days
    drop20 = norm.cdf(-0.2,mu220,sigma220)



    gain20=norm.cdf(0.2,mu220,sigma220)


    gain40=norm.cdf(0.4,mu220,sigma220)

    ### Two tail test - Is average return 0?

    n = ms['LogReturn'].shape[0]
    zhat = (mean_sample - 0) / (std_sample / n ** 0.5)  # 0 because we are assuming null hypothesis

    alpha = 0.05  # Confidence interval
    zl_2 = norm.ppf(alpha / 2, 0, 1)  # Two tail test - left side of dist
    zr_2 = -zl_2  # Two tail test - right side of dist
    # if zhat > zr_2 or zhat<zl_2 we reject the null hypothesis

    zright = norm.ppf(1 - alpha, 0, 1)



# ## Calculate Value at risk (VaR)

# Value at risk(VaR)
    VaR = norm.ppf(0.05, mean_sample, std_sample)

    f=open("results/risk_numbers_10y/%s_analysis.txt" %ticker,"w")
    f.writelines('The Probability of 5% drop in a day is  {:.10f}\n'.format(prob_return1))
    f.writelines('The probability of 5% gain in a day is {:.10f}\n'.format(prob_return3))
    f.writelines("The probability of a 20% loss in 10 years is {:.10f}\n".format(drop20))
    f.writelines('The probability of a 40% loss in 10 years is {:.10f}\n'.format(drop40))
    f.writelines('The probability of a 20% gain in 10 years is {:.10f}\n'.format(gain20))
    f.writelines("The probability of a 40% gain in 10 years is {:.10f}\n".format(gain40))
    f.writelines("VaR is {:.10f}\n".format(VaR))
    f.writelines("Sample mean is {:.10f}\n".format(mean_sample))
    f.writelines("With 95% confidence,can we reject that average return is 0 - {} \n".format(zhat > zr_2 or zhat < zl_2))
    f.writelines("With 95% confidence, can we reject that average return in 10y period is positive {}\n".format(zhat > zright))
    f.writelines("90% confidence interval is {:.10f} and {:.10f}\n".format(interval_left,interval_right))
    f.close()

with open("portfolio.txt","r") as symbol_file:
    for line in symbol_file:
        risk_calculator(line.strip())
        print("Analyzed %s" %line.strip())
