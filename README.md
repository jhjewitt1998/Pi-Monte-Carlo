# Estimating Pi Via the Monte Carlo Simulation Method (Pi-Monte-Carlo)
<p>
This script uses the monte carlo algorithm to estimate pi. The x coords, y coords, points in the circle, estimation of pi and variance are all recoreded in a pandas df for further manipulation if needed.</p>

# Monte Carlo Simulation

<p>
The Monte Carlo Simulation is a mathamatical technique which uses random sampling to estimate the possible outcomes of an uncertain event, in this event calculating pi. This example is specifically done by generating a random 2d coordinate and checking if its inside or outside of the circle, as seen in the image below. Pi is estimated by calculating the ratio of points that lay inside the circle and total number points which had been generated overall.
</P>

<p align="center">
  <img width="300" height="300" src="https://nclab.com/wp-content/media/2017/08/pi1.gif">
</p>

# Equations Used 

$$
  \cfrac{Area of Circle}{Area of Square} = \cfrac{\pi r^2}{4r^2} = \cfrac{\pi}{4}
$$

As seen in the eqaution above it is known that area of the square is 4r^2 while that of circle is pi r^2. The above equation shows how to evaluate a suitable outcome.

$$
  \cfrac{\pi}{4} = 4 * \cfrac{Total number of points inside the circle}{Total number of points inside the square}
$$

<p>

The above equation allows us to estimate pi from the simulated information. Essentially we are checking that x^2 + y^2 <= 1. If this is the case the plot is inside the circle and the variable for the number of plots inside the circle is incremented. This is then divided over the total number of generated plots to gather an estimate of pi. This is repeated an x amount of times, presenting new results each time a simulation is run. Generating more plots tends to lead to a more accurate estimate of pi.

</p>

# References:
</p>
<p>
img: Author: Manas Sharma, https://www.bragitoff.com/2021/05/value-of-pi-using-monte-carlo-python-program/
</p>
