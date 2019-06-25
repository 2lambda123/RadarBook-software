"""
Project: RadarBook
File: shnidman.py
Created by: Lee A. Harrison
One: 10/9/2018
Created with: PyCharm
"""
import sys
from scipy import exp, sqrt, log, sign, log10


def signal_to_noise(probability_of_detection, probability_of_false_alarm, number_of_pulses, swerling_type):
    """
    Calculate the single pulse signal to noise for non-coherent integration.
    :param probability_of_detection: The probability of detection.
    :param probability_of_false_alarm: The probability of false alarm.
    :param number_of_pulses: The number of pulses to be non-coherently integrated.
    :param swerling_type: The Swerling target type.
    :return: The single pulse signal to noise.
    """
    # First parameter, based on Swerling type
    if swerling_type == 'Swerling 0':
        k = sys.float_info.max
    elif swerling_type == 'Swerling 1':
        k = 1
    elif swerling_type == 'Swerling 2':
        k = number_of_pulses
    elif swerling_type == 'Swerling 3':
        k = 2
    else:
        k = 2 * number_of_pulses

    # Second parameter, based on number of pulses
    if number_of_pulses < 40:
        alpha = 0
    else:
        alpha = 0.25

    # Calculated parameters
    eta = sqrt(-0.8 * log(4 * probability_of_false_alarm * (1.0 - probability_of_false_alarm))) \
          + sign(probability_of_detection - 0.5) * sqrt(-0.8 * log(4 * probability_of_detection * (1.0 - probability_of_detection)))
    x = eta * (eta + 2.0 * sqrt(0.5 * number_of_pulses + alpha - 0.25))

    # Constants
    c1 = (((17.7006 * probability_of_detection - 18.4496) * probability_of_detection + 14.5339) * probability_of_detection - 3.525) / k
    c2 = (1.0 / k) * (exp(27.31 * probability_of_detection - 25.14) + (probability_of_detection - 0.8)
                      * (0.7 * log(1e-5 / probability_of_false_alarm) + (2.0 * number_of_pulses - 2)) / 80)

    if 0.1 <= probability_of_detection <= 0.872:
        cdb = c1
    elif 0.872 <= probability_of_detection <= 0.99:
        cdb = c1 + c2

    c = 10.0 ** (cdb / 10.0)

    # Signal to noise ratio
    return 10.0 * log10(c * x / number_of_pulses)
