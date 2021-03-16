from Mapping.types import InPort, OutPort, List
from Mapping.utils import MethodCall, Requires, Setup

@MethodCall(target="RandomSingle.vix", Lower=float, Upper=float, Number=float)
def randomNumeric():
    return '''
        Number = random.uniform(Lower, Upper)
    '''

@MethodCall(target="RandomBoolean.vix", PercentTrue=float, Result=bool)
def randomBoolean():
    return '''
        Result = random.random() * 100 <= PercentTrue
    '''
