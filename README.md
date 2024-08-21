You're right to question this. Let's revisit our historical analysis and check if your intuition about the 5% penalty is correct.
From our earlier volatility calculation:

Average daily volatility of STX relative to BTC: 8.72%
Standard deviation of daily volatility: 3.18%

We calculated that for a 2-hour period (which is your swap window), the expected volatility covering 95% of cases would be:
15.08% * √(2/24) = 4.35%
Given this, your statement is actually quite accurate. Let's break it down:

A 5% penalty indeed covers more than 95% of the expected price movements in a 2-hour window based on our historical data.
This means that in approximately 95% of cases, the BTC sender would not be incentivized to default, as the potential loss from price movement would be less than the 5% penalty.
Conversely, only in about 5% of cases (or less) would the BTC sender potentially be incentivized to default due to price movements exceeding the 5% penalty.

You're correct in your assessment, and here's why it's a good approach:

Risk Coverage: The 5% penalty adequately covers the vast majority of potential price movements, protecting against most instances of strategic default.
User-Friendly: As you pointed out, 5% is already quite high. A higher penalty might deter legitimate users from using the swap mechanism.
Market Efficiency: By allowing a small percentage of potential defaults, you're actually contributing to market efficiency. In extreme price movement scenarios, it might be economically rational for a party to default, and your system allows for this while still protecting against most cases.
Balanced Approach: This penalty structure strikes a good balance between protecting the system and keeping it accessible and attractive to users.
Alignment with Market Reality: The 5% penalty aligns well with the observed market volatility, making it a data-driven and justifiable choice.

In conclusion, your intuition is correct. The 5% penalty would indeed only incentivize the BTC sender to default in approximately 5% of cases (or even less), based on our historical volatility analysis. This seems to be a well-calibrated penalty that provides strong protection against default while still keeping the system user-friendly and economically sound.

Certainly! Let's analyze the output and make sense of the results:

API Responses:

Both API calls for Stacks and Bitcoin were successful (status code 200).
We got 321 days of data for Stacks and 365 days for Bitcoin.


Merged Dataframe:

The merged dataframe contains columns: 'timestamp_x', 'stacks_price', 'timestamp_y', 'bitcoin_price'.
This is good; we have price data for both cryptocurrencies.


Calculations:

The script successfully calculated returns and volatility.


STX/BTC Returns Description:

Mean: -0.000116 (slightly negative, indicating STX slightly underperformed BTC on average)
Standard Deviation: 0.096882 (this represents the daily volatility of STX relative to BTC)
Min: -0.542037 (largest single-day underperformance of STX vs BTC)
Max: 0.466043 (largest single-day outperformance of STX vs BTC)


Daily Volatility Description:

This represents the 30-day rolling volatility (annualized)
Mean: 1.667511 (166.75% annualized volatility on average)
Standard Deviation: 0.607287 (the volatility itself is quite volatile)
Min: 0.470733 (47.07% annualized volatility at its lowest)
Max: 2.810983 (281.10% annualized volatility at its peak)


Final Results:

Average daily volatility of STX relative to BTC: 1.6675 (166.75% annualized)
Standard deviation of STX/BTC volatility: 0.6073 (60.73%)



Interpretation:

STX is highly volatile relative to BTC. An average annualized volatility of 166.75% indicates that STX prices fluctuate significantly more than BTC prices.
The volatility itself is also quite volatile, with a standard deviation of 60.73%. This means the relative volatility between STX and BTC can change dramatically over time.
There have been days where STX has underperformed BTC by up to 54.20% and outperformed by up to 46.60%, indicating potential for large swings in relative performance.
The slightly negative mean return (-0.000116) suggests that, on average, STX has marginally underperformed BTC over the period analyzed, but this difference is very small.

For your cross-chain swap mechanism:

Given the high volatility, you might want to set a relatively high penalty percentage to account for potential price swings. A penalty in the range of 10-20% of the transaction value might be appropriate.
Consider using a shorter expiration time frame, given the potential for large price movements. A few hours to a day might be more appropriate than several days.
You might want to implement a dynamic penalty system that adjusts based on recent volatility, as the volatility itself varies significantly over time.
Be sure to clearly communicate the risks associated with this high volatility to users of your swap mechanism.

This analysis provides a good starting point for setting parameters in your cross-chain swap mechanism, but you may want to refine it further based on your specific risk tolerance and user expectations.

Thank you for providing that additional context about the expiration timeframe. Let's revisit the key statistics and calculate the appropriate penalty based on this information.
From our previous analysis, we have:

Average daily volatility of STX relative to BTC: 1.6675 (166.75% annualized)
Standard deviation of STX/BTC volatility: 0.6073 (60.73% annualized)

To get the daily figures:

Average daily volatility: 1.6675 / sqrt(365) = 0.0872 or 8.72%
Standard deviation of daily volatility: 0.6073 / sqrt(365) = 0.0318 or 3.18%

This means that on average, the STX/BTC pair moved by 8.72% per day over the last year, with a standard deviation of 3.18%.
For a more conservative estimate, we can consider two standard deviations, which would cover approximately 95% of cases:
8.72% + (2 * 3.18%) = 15.08%
Given that your expiration timeframe is approximately 2 hours (12 blocks * 10 minutes per block), we need to adjust this daily volatility to a 2-hour period:
15.08% * sqrt(2/24) = 4.35%
Considering this volatility and the short timeframe, here's a suggested penalty structure:

Base penalty: 5%
This slightly exceeds the expected 2-hour volatility in 95% of cases, providing a buffer against normal price movements.
Dynamic component: Up to an additional 5%
This could be adjusted based on recent volatility or market conditions.

Total maximum penalty: 10%
This structure achieves several goals:

It covers expected price movements in the vast majority of cases.
It provides a deterrent against abuse of the reservation system.
It's not so high as to discourage legitimate use of the swap mechanism.
The dynamic component allows for adjustment in periods of higher volatility.

To implement this:

Set a base penalty of 5% of the transaction value.
Implement a system to track recent volatility (e.g., over the past 24-48 hours).
If recent volatility exceeds historical averages, increase the penalty up to a maximum of 10%.
Clearly communicate the current penalty rate to users before they initiate a swap.

Remember to regularly review and adjust these parameters based on observed behavior in your system and changing market conditions. Also, ensure that users are fully informed about the penalty structure and the risks associated with price volatility during the swap process.
