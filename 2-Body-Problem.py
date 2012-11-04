#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

GravitationConstant = 6.67300 / 100000000000
Mass = 1.9891 * 1000000000000000000000000000000
radius = 1.496 * 100000000000
semimajorAxis = 1.496 * 100000000000

velocity = math.sqrt(GravitationConstant*Mass*((2/radius)-(1/semimajorAxis)))

print velocity

#Rank	Name	Semimajor Axis (kilometer)
#1	Pluto	5.90638 x 109
#2	Neptune	4.49506 x 109
#3	Uranus	2.87246 x 109
#4	Saturn	1.43353 x 109
#5	Jupiter	7.7857 x 108
#6	Mars	2.2792 x 108
#7	Earth	1.496 x 108
#8	Venus	1.0821 x 108
#8	Mercury	5.791 x 107
#9	Moon	3.844 x 105
