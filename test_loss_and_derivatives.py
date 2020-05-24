import numpy as np
from loss_and_derivatives  import LossAndDerivatives

def test_l2_reg_derivative():
    x = np.array([1,1,2,2])
    assert LossAndDerivatives.l2_reg(x) == 10
    
