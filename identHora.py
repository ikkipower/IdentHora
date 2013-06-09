#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  CRUD.py
#       
#  Copyright 2013 Sergio Morlans <https://github.com/ikkipower/IdentHora.git>
#       
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#       
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#       
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

import re

patron = "^2[0-9]{3}$"
cadano = ["1999","2000","2999","2500","250","120","1900","2222","25000","2","1"]

#for cad in cadano:
#	if re.search(patron,cad):
#		print "El patrón incluye el año: " + cad
#	else:
#		print "El patrón NO incluye el año: " + cad
		
patron2 = "([0-1]?[0-9]|2[0-4]?):([0-5]{1}[0-9]{1}) [AM|PM]{1}"
patron3 = "(^[0-5][0-9]$)"
cadhora = ["00:","01","02","03","04","05","06","07","08","09",
           "0","1","2","3","4","5","6","7","8","9",
           "10","11","12","13","14","15","16","17","18","19",
           "20","21","22","23","24","25","26","27","28","29",
           "40","41","42","43","44","45","46","47","48","49",
           "50","51","52","53","54","55","56","57","58","59",
           "60","61","62","63","64","65","66","67","68","69",
           "70","71","72","73","74","75","76","77","78","79",
           "80","81","82","83","84","85","86","87","88","89",
           "90","91","92","93","94","95","96","97","98","99",
           "100","200"]
cadhoracomp = ["00:00 AM","0:00 PM","01:59 PM","13:00 AM","24:00 PM","12:00 AM",
               "4:45 AM","3:23 AM","2:22 PM","6:10 AM","1:00 PM","00:60 AM",
               "5:55 AM","7:11 AM","8:03 AM","9:7 AM","10:00 PM","11:00 AM"]

for cad2 in cadhoracomp:
	if re.search(patron2,cad2):
		print "El patrón incluye la hora: " + cad2
	else:
		print "El patrón NO incluye la hora: " + cad2
