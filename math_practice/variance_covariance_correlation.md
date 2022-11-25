
# Variance

The variance is the average of the square difference from the mean

 - we have some numbers, ie. 10, 12, 13, 17, 20, 24
 - mean is the sum of all numbers/6 (bcs it is six numbers) = 16
 - we check how far each number is from the mean value
 - 10 - 16 = -6, 12 - 16 = -4 etc, so all numbers are: -6, -4, -3, 1, 4, 8
 - square each of these values above: -6 * -6 = 36, 16, 9, 1, 16, 64 (variance cannot be negative)
 - we add all of these values together = 142
 - we divide 142 with the number of values - 1 which is five, so 142/5 = 28.4 (when calculating the variance of a population we don't use -1. The -1 is known as Bessel's correction)
 - The variance number is 28.4 unit(ie. kg)^2
 - standard deviation = square root of variance 
 - the square root of 28.4 is 5.3
 - the variance is 5.3

# Covariance

-  If we check the covariance with ie. BTC , tech Stocks, ETH, Monero
- If we can see that there is a pattern, that whenever Tech stocks have a price depreciation then BTC has as well. Or that when ETH has price appriciation Monero do too.
- This gives us information to be able to make analysis
- Covariance can classify three types of relationships:
	- relationship with positive trends
	- relationship with neagtive trends
	- no relationship because there is no trend
- covariance is a stepping stone to correlation
- calculating covariance:
	- Cov(x, y) = E(xy) - E(x)E(y)
	- E is the mean
	
	Two examples of x and y:
	- x = [1, 2, 3, 4, 5]
	- y = [2, 3, 4, 5, 6]
	
	- calculate mean for x:
	- 1 + 2 + 3 + 4 + 5 = 15
	- 15/5 = 3
	- E (mean) for x is 3, therefore E(x) = 3
	
	- calculate the mean for y:
	- 2 + 3 + 4 + 5 + 6 = 20
	- 20/5 = 4
	- E (mean) for y is 4, therefore E(y) = 4
	
	
	- to get xy you multiply same position in x and y with each other
	-  1*2 = 2, 3*2 = 6, 4*3 = 12, 5*4 = 20, 6*5 = 30
	- 30/5 = 6
	- the mean of xy is 6, therefore E(xy) = 6
	
	- Cov(x, y) = E(xy) - E(x)E(y)
	- 6 - 3 * 4 =  -6 is the Covariance
	- x and y are negatively correlated

# Correlation


- correlation = Cov(x,y)/square root of V(x)V(y)
- V(x) = E(x^2) - E(x)^2 - variance of x
- V(y) = E(y^2) - E(y)^2 - variance of y

- first we calculate squared x:
- 1*1 =1, 2*2=4, 3*3=9, 4*4=16, 5*5=25
- 1+4+9+16+25=55
- 55/5=11
- E(x^2) = 11

- then we calculate squared y:
- 2*2=4, 3*3=9, 4*4=16, 5*5=25, 6*6=36
- 4+9+16+25+36=90
- 90/5=18
- E(y^2)=18

- variance of x is calculated like this: V(x) = E(x^2) - E(x)^2
- 11 - 7.5^2 (7.5*7.5=56.25) = -45.25 V(x)

- variance of y is calculated like this: V(y) = E(y^2) - E(y)^2
- 18 - 10^2 (10*10=100) = -82 v(y)

- we multiply V(x) and V(y):
- -42.25 * -82 = 3464.5

- and the square root:
- square root of 3464.5 = 58.86

- the formula to calculate correlation is this: correlation = Cov(x,y)/square root of V(x)V(y)
- Covariance as calculated in the example below header Covariance is -6
- correlation is -6/58.86 = -0.1
- There is a negative correlation but not strong


