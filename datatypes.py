from typing import List
import dataclasses as dc

# we are using dataclass over namedtuple mostly because of mypy's 
# limitations when checking recursive NamedTuple types

#floating point comparison is hard...
_EPSILON = 1e-3

@dc.dataclass(frozen= True)
class Project:
    name: str
    oil_shrink: float
    gas_shrink: float
    wi: float
    nri: float
    tax_rate: float
    outcomes: 'List[Outcome]'

    # we can use post__init__ to enforce 'class invariants' about our 
    # data types - in a sense, we can ensure that values of our types are 
    # "correct by construction"

    def __post_init__(self) -> None:
        '''Validate project level data and outcome probabilities'''
        if not 0.0 <= self.oil_shrink <= 1.0:
            raise ValueError('invalid oil shrink')
        if not 0.0 <= self.gas_shrink <= 1.0:
            raise ValueError('invalid gas shrink')
        if not 0.0 <= self.wi <= 1.0:
            raise ValueError("invalid wi")
        if not 0.0 <= self.nri <= 1.0:
            raise ValueError('invalid nri')
        if not 0.0 <= self.tax_rate <= 1.0:
            raise ValueError("invalid tax rate")
        if abs(sum(o.probability for o in self.outcomes) -1.0) > _EPSILON:
            raise ValueError('outcome probabilities must sum to 1.0')
    # additional validation to be added 

@dc.dataclass(frozen=True)
class Outcome:
    probability: float
    oil: List[float]
    gas: List[float]
    capex: List[float]
    opex: List[float]
    leads_to: List[Project]

    def __post_init__(self)-> None:
        if not 0.0 <= self.probability <= 1.0:
            raise ValueError('invalid probabilty')
        if not(len(self.oil) == len(self.gas) == len(self.capex) == len(self.opex)):
            raise ValueError('monthly array lengths must match')
        
@dc.dataclass(frozen=True)
class PriceDeck:
    oil_price: List[float]
    gas_price: List[float]

    def __post_init__(self)-> None:
        if not(len(self.oil_price) == len(self.gas_price)):
            raise ValueError('monthly array lengths must match')



