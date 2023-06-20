import sys
from datatypes import Project, Outcome, PriceDeck
from projects import root_projects, all_projects
from random import Random

from typing import List, Iterable

def net_cashflow(project: Project, outcome: Outcome, deck: PriceDeck) -> List[float]:
    net_cf = list()
    for o, g, capex, opex, p_o, p_g in zip(
        outcome.oil, outcome.gas, outcome.capex, outcome.opex, deck.oil_price, 
        deck.gas_price):
        gross_revenue = ((1.0 - project.oil_shrink)* o * p_o * project.nri +
        (1.0 - project.gas_shrink)*g *p_g * project.nri)
        net_opex = opex * project.wi * 1000.0
        net_capex = capex* project.wi * 1000.0
        tax = project.tax_rate * gross_revenue
        net_cf.append(gross_revenue-net_opex - net_capex - tax )
    return net_cf

def npv(net_cf: Iterable[float], discount: float) -> float:
    return sum(cf / (1.0 + discount)** (i / 12.0) 
        for (i, cf) in enumerate (net_cf))

def realize_outcome(r: Random, project: Project) -> Outcome:
    return r.choices(project.outcomes, 
                     weights = [o.probability for o in project.outcomes],  k= 1)[0]



def main(argv: List[str]) -> int:
    temp_deck = PriceDeck([40.0]* 36, [2.50] * 36)

    r = Random(12345)
    for p in all_projects:
        for i, o in enumerate(p.outcomes):
            npv10 = npv(net_cashflow(p, o, temp_deck), 0.1)
            print(f'{p.name} #{i} -> NPV10 = {npv10}')
    return 0 

if __name__ == '__main__':
    sys.exit(main(sys.argv))