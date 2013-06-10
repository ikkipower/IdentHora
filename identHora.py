#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  identHora.py
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

for cad2 in cadano:
	if re.search(patron,cad2):
		print "El patrón incluye la hora: " + cad2
	else:
		print "El patrón NO incluye la hora: " + cad2


patron = "^([0]?[0-9]|[1]?[0-2])$"


cad = ["0","1","2","3","4","5","6","7","8","9",
       "10","21","32","43","54","65","76","87","98","99",
       "100"]

cadhora2 = ["00","01","02","03","04","05","06","07","08","09",
           "0","1","2","3","4","5","6","7","8","9",
           "10","11","12","13","14","15","16","17","18","19",
           "20","21","22","23","24","25","26","27","28","29",
           "30","31","32","33","34","45","46","47","48","49",
           "50","51","52","53","54","55","56","57","58","59",
           "60","61","62","63","64","65","66","67","68","69",
           "70","71","72","73","74","75","76","77","78","79",
           "80","81","82","83","84","85","86","87","88","89",
           "90","91","92","93","94","95","96","97","98","99",
           "100","200"]

cadhorac = ["00:00","0:00","01:59","13:00","24:00","12:00",
               "6:10","1:00","00:60",
               "5:55","7:11","8:03","9:7","10:00","11:00"]


#for cad in cadhora2:
#	if re.search(patron,cad):
#		print "search: " + cad
#	else:
#		print "NO search: " + cad

#patron2 = "^[0-2]\d:[0-6]\d$"

#for cad2 in cadhorac:
#	if re.search(patron2,cad2):
#		print "csearch: " + cad2
#	else:
#		print "NO csearch: " + cad2

patron3 = "^([0]?[0-9]|[1]?[0-2]):$"




#for cad2 in cadhora2:
#	if re.search(patron3,cad2):
#		print "csearch: " + cad2
#	else:
#		print "NO csearch: " + cad2

patron4= "^([0]?[0-9]|[1]?[0-2]):([0-5][0-9])$"

cadhorac = ["00:00","0:00","01:59","13:00","24:00","12:00","6:10","1:00","00:60",
            "5:55","7:11","8:03","9:7","10:00","11:00"]

#for cad2 in cadhorac:
#	if re.search(patron4,cad2):
#		print "csearch: " + cad2
#	else:
#		print "NO csearch: " + cad2

patron5= "^([0]?[0-9]|[1]?[0-2]):([0-5][0-9]) (AM|PM)$"

cadhoracomp = ["00:00 AM","0:00 PM","01:59 PM","13:00 AM","24:00 PM","12:00 AM",
               "4:45 AM","3:23 AM","2:22 PM","6:10 AM","1:00 PM","00:60 AM",
               "5:55 AM","7:11 AM","8:03 AM","9:7 AM","10:00 PM","11:00 AM"]
               
#for cad2 in cadhoracomp:
#	if re.search(patron5,cad2):
#		print "csearch: " + cad2
#	else:
#		print "NO csearch: " + cad2

patron6= "^(Ene|Feb|Mar|Abr|May|Jun|Jul|Ago|Sep|Oct|Nov|Dec)/([2-9][0-9]{3}) ([0]?[0-9]|[1]?[0-2]):([0-5][0-9]) (AM|PM)$"

cadfecha = ["Ene/2004 00:00 AM","Ene/1999 0:00 PM","Feb/2009 01:59 PM","Dec/9999 13:00 AM","Dec/2999 24:00 PM","Feb/1 12:00 AM",
               "Dec/3000 04:45 AM","Nov/9999 03:23 AM","Jun/2525 2:22 PM","Ago/6578 6:10 AM","Asa/1234 1:00 PM","Fev/2222 00:50 AM",
               "Oct/2000 05:55 AM","Sep/8976 7:11 AM","2000 12:59 AM","Maj/2002 9:7 AM","Agg/1223 10:00 PM","Mar/5643 11:00 AM"]
               
#for cad2 in cadfecha:
#	if re.search(patron6,cad2):
#		print "csearch: " + cad2
#	else:
#		print "NO csearch: " + cad2


cadfecha2 = ["31/Ene/2004 00:00 AM","32/Ene/2999 0:00 PM","12/Feb/2009 01:59 PM","1/Dec/9999 13:00 AM","01/Dec/2999 24:00 PM","09/Feb/1 12:00 AM",
               "21/Dec/3000 04:45 AM","07/Nov/9999 03:23 AM","66/Jun/2525 2:22 PM","22/Ago/6578 6:10 AM","11/Asa/1234 1:00 PM","11/Fev/2222 00:50 AM",
               "23/Oct/2000 05:55 AM","21/Sep/8976 7:11 AM","31/2000 12:59 AM","12/Maj/2002 9:7 AM","12/Agg/1223 10:00 PM","04/Mar/5643 11:00 AM"]

patron7= "^([0]?[1-9]|[1-2][0-9]|[3][0-1])/(Ene|Feb|Mar|Abr|May|Jun|Jul|Ago|Sep|Oct|Nov|Dec)/([2-9][0-9]{3}) ([0]?[0-9]|[1]?[0-2]):([0-5][0-9]) (AM|PM)$"

#for cad2 in cadfecha2:
#	if re.search(patron7,cad2):
#		print "csearch: " + cad2
#	else:
#		print "NO csearch: " + cad2

nomciudad ="^(([A-Z]([a-z])* )?([D|d]e )?[A-Z]([a-z])*)$" 
ciudad = ["Barcelona","Madrid","San Sebastian","Granada","Santiago de Compostela"]

for cad2 in ciudad:
	if re.search(nomciudad,cad2):
		print "csearch: " + cad2
	else:
		print "NO csearch: " + cad2

patron8= "^(([A-ZÑ]([a-zñ])* )?([D|d]e )?[A-ZÑ]([a-zñ])*) ([0]?[1-9]|[1-2][0-9]|[3][0-1])/(Ene|Feb|Mar|Abr|May|Jun|Jul|Ago|Sep|Oct|Nov|Dec)/([2-9][0-9]{3}) ([0]?[0-9]|[1]?[0-2]):([0-5][0-9]) (AM|PM)$"

cadfecha3 = ["Barcelona 31/Ene/2004 00:00 AM",
             "San Sebastian 31/Ene/2004 00:00 AM",
             "Granada 32/Ene/2999 0:00 PM",
             "Cordoba 12/Feb/2009 01:59 PM",
             "Madrid 1/Dec/9999 13:00 AM",
             "Gijon 01/Dec/2999 24:00 PM",
             "Salamanca 09/Feb/1 12:00 AM",
             "La Coruña 21/Dec/3000 04:45 AM",
             "Ciudad Real 07/Nov/9999 03:23 AM",
             "Barcelona 66/Jun/2525 2:22 PM",
             "Alava 22/Ago/6578 6:10 AM",
             "Santiago de Compostela 31/Ene/2004 00:00 AM",
             "Barcelona 11/Fev/2222 00:50 AM",
             "Guadalajara 23/Oct/2000 05:55 AM",
             "Castellon 21/Sep/8976 7:11 AM",
             "Murcia 31/2000 12:59 AM",
             "Oviedo 12/Maj/2002 9:7 AM",
             "Girona 12/Agg/1223 10:00 PM",
             "Tarragona 04/Mar/5643 11:00 AM"]

for cad2 in cadfecha3:
	if re.search(patron8,cad2):
		print "csearch: " + cad2
	else:
		print "NO csearch: " + cad2
