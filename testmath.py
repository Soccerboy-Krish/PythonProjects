from MathFunctions import *

gc = GCF (15,20)
if(gc != 5):
	print 'GCF failed'

gc = GCF (20,-1)
if(gc != 1):
	print 'GCF failed'

gc = GCF (-3,-6)
if(gc != 3):
	print 'GCF failed (-3,-6)'

gc = GCF (-18,-4)
if(gc != 2):
	print 'GCF failed for (-18, -4)'

cod = count_of_divisors(4)
if (cod != "odd"):
	print 'COD failed for 4'

cod = count_of_divisors(36)
if (cod != "odd"):
	print "COD failed for 36"

cod = count_of_divisors(2)
if (cod != "even"):
	print "COD failed for 2"

cod = count_of_divisors(1)
if cod != "odd":
	print "cod failed for 1"


cod = count_of_divisors(0)
if cod != "odd":
	print "cod failed for 0"


odd = sum_odd_factors(12)
if odd != 4:
	print "odd has failed for 12"


odd = sum_odd_factors(1)
if odd != 1:
	print "odd has failed for 1"


odd = sum_odd_factors(0)
if odd != 0:
	print "odd has failed for 0"


sums = sums_odd_minus_sums_even ([3,5,7,8])

if sums !=7:
	print "sums_odd_minus_sums_even has failed for 7"








