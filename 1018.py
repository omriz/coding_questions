#!/usr/bin/env python3
'''
This problem was asked by Microsoft.

Given a clock time in hh:mm format, determine, to the nearest degree,
the angle between the hour and the minute hands.

Bonus: When, during the course of a day, will the angle be zero?
'''

# Equality will be when 23minutes = 120hours (12h format)

import sys


def main():
    hour,minute = [int(x) for x in sys.argv[1].split(':')]
    if hour > 23 or hour < 0:
        sys.exit(1)
    if hour > 12:
        hour = hour - 12
    if minute > 60 or minute < 0:
        sys.exit(2)
    m_angle = minute*6.0
    h_angle = hour*30.0 + minute*15.0/60.0

    if h_angle > m_angle:
        print(h_angle-m_angle)
    else:
        print(m_angle-h_angle)
    
if __name__ == "__main__":
    main()