#-----------------WEEK 05 ASSIGNMENT---------------#

#-----------------Step 2---------------#
# Create another new file, save it as test_water_flow.py, and copy and paste the following import statements into the file.
from pytest import approx
import pytest

from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe
#-----------------Step 4---------------#
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


#-----------------Step 6---------------#
# In your test_water_flow.py file, write a test function named test_pressure_gain_from_water_height. This test function must call pressure_gain_from_water_height at least three times to verify that it is working correctly. Use the following numbers in your test function.
# Height | Expected Pressure | Aprox absolute Tolerance
# 0	   |  0       |	0.001
# 30.2 |  295.628 | 0.001
# 50   |  489.450 | 0.001

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0.0) == 0.0
    assert pressure_gain_from_water_height(30.2) == approx(295.628, rel=0.001)
    assert pressure_gain_from_water_height(50.0) == approx(489.450, rel=0.001)


#-----------------Step 8---------------#
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

#-----------------Step 9---------------#
# Copy and paste the following code at the bottom of your test_water_flow.py file.

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
