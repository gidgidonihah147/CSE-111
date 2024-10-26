#-----------------WEEK 05 ASSIGNMENT---------------#

#-----------------Week 05 - Step 2---------------#
# Create another new file, save it as test_water_flow.py, and copy and paste the following import statements into the file.
from pytest import approx
import pytest

from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynold_numbers, pressure_loss_from_pipe_reduction
#-----------------Week 05 - Step 4---------------#
# In your test_water_flow.py file, write a test function named test_water_column_height. This test function must call water_column_height at least four times to verify that it is working correctly. Use the following numbers in your test function.
# Tower Height | Tank Wall Height |Expected Water Column Height
# 0	   | 0    |	0
# 0	   | 10   | 7.5
# 25   | 0    | 25
# 48.3 | 12.8 |	57.9

def test_water_column_height():
    assert water_column_height(0.0, 0.0) == 0.0
    assert water_column_height(0.0, 10.0) == 7.5
    assert water_column_height(25.0, 0.0) == 25.0
    assert water_column_height(48.3, 12.8) == approx(57.9, rel=0.01)


#-----------------Week 05 - Step 6---------------#
# In your test_water_flow.py file, write a test function named test_pressure_gain_from_water_height. This test function must call pressure_gain_from_water_height at least three times to verify that it is working correctly. Use the following numbers in your test function.
# Height | Expected Pressure | Aprox absolute Tolerance
# 0	   |  0       |	0.001
# 30.2 |  295.628 | 0.001
# 50   |  489.450 | 0.001

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0.0) == 0.0
    assert pressure_gain_from_water_height(30.2) == approx(295.628, rel=0.001)
    assert pressure_gain_from_water_height(50.0) == approx(489.450, rel=0.001)


#-----------------Week 05 - Step 8---------------#
# In your test_water_flow.py file, write a test function named test_pressure_loss_from_pipe . This test function must call pressure_loss_from_pipe at least seven times to verify that it is working correctly. Use the following numbers in your test function.
# Pipe Diameter | Pipe Length | Friction Factor | Fluid Velocity | Expected Pressure Loss | Aprox absolute Tolerance
# 0.048692 | 0	     | 0.018 | 1.75 | 0	       | 0.001
# 0.048692 | 200     | 0     | 1.75 | 0        | 0.001
# 0.048692 | 200     | 0.018 | 0    | 0        | 0.001
# 0.048692 | 200     | 0.018 | 1.75 | -113.008 | 0.001
# 0.048692 | 200     | 0.018 | 1.65 | -100.462 | 0.001
# 0.28687  | 1000    | 0.013 | 1.65 | -61.576  | 0.001
# 0.28687  | 1800.75 | 0.013 | 1.65 | -110.884 | 0.001

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75) == 0.0
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75) == 0.0
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00) == 0.0
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) == approx(-113.008, rel=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65) == approx(-100.462, rel=0.001)
    assert pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65) == approx(-61.576, rel=0.001)
    assert pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) == approx(-110.884, rel=0.001)

#-----------------Week 05 - Step 9---------------#
# Copy and paste the following code at the bottom of your test_water_flow.py file.

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])


#-----------------Week 06 - Step 2---------------#
# In your test_water_flow.py file, write a test function named test_pressure_loss_from_fittings. This test function must call pressure_loss_from_fittings at least five times to verify that it is working correctly. Use the following numbers in your test function.
# Fluid Velocity | Quantity of Fittings | Expected Pressure Loss | approx Absolute Tolerance
# 0    |	3 |	0      |	0.001
# 1.65 |	0 |	0      |	0.001
# 1.65 |	2 |	-0.109 |	0.001
# 1.75 |	2 |	-0.122 |	0.001
# 1.75 |	5 |	-0.306 |	0.001

def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(0.00, 3) == approx(0.000, rel=0.001)
    assert pressure_loss_from_fittings(1.65, 0) == approx(0.000, rel=0.001)
    assert pressure_loss_from_fittings(1.65, 2) == approx(-0.109, rel=0.01)
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122, rel=0.01)
    assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, rel=0.001)

#-----------------Week 06 - Step 4---------------#
# In your test_water_flow.py file, write a test function named test_reynolds_number. This test function must call reynolds_number at least five times to verify that it is working correctly. Use the following numbers in your test function.
# Hydraulic Diameter | Fluid Velocity | Expected Reynolds Number | approx Absolute Tolerance
# 0.048692 | 0    | 0      | 1
# 0.048692 | 1.65 | 80069  | 1
# 0.048692 | 1.75 | 84922  | 1
# 0.28687  | 1.65 | 471729 | 1
# 0.28687  | 1.75 | 500318 | 1

def test_reynold_number():
    assert reynold_numbers(0.048692, 0.00) == approx(0, rel=1)
    assert reynold_numbers(0.048692, 1.65) == approx(80069, rel=1)
    assert reynold_numbers(0.048692, 1.75) == approx(84922, rel=1)
    assert reynold_numbers(0.286870, 1.65) == approx(471729, rel=1)
    assert reynold_numbers(0.286870, 1.75) == approx(500318, rel=1)


#-----------------Week 06 - Step 6---------------#
# In your test_water_flow.py file, write a test function named test_pressure_loss_from_pipe_reduction. This test function must call pressure_loss_from_pipe_reduction at least three times to verify that it is working correctly. Use the following numbers in your test function.
# Larger Diameter | Fluid Velocity | Reynolds Number | Smaller Diameter | Expected Pressure Loss | approx Absolute Tolerance
# 0.28687 | 0    | 1      | 0.048692 | 0        | 0.001
# 0.28687 | 1.65 | 471729 | 0.048692 | -163.744 | 0.001
# 0.28687 | 1.75 | 500318 | 0.048692 | -184.182 | 0.001

def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692) == approx(0.000, rel=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-163.744, rel=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, rel=0.001)


