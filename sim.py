import sys
from datatypes import Project, Outcome, PriceDeck
from projects import root_projects, all_projects
from random import Random

from typing import Callable, Iterator, List, Iterable, Tuple, Generic, TypeVar, NamedTuple, Sequence 
import matplotlib.pyplot as plt # type: ignore

PRICE_DECKS ={
    'flat': PriceDeck(
        oil_price= [40.0] * 36, 
        gas_price= [2.50] * 36
    ), 
   'high': PriceDeck(
       oil_price= [40.0] * 12 + [60.0] * 12 + [90.0] * 12,
       gas_price=[2.50] * 12 + [3.50] * 12 + [5.00] * 12
   ), 
    'low': PriceDeck(
       oil_price= [40.0] * 12 + [20.0] * 24,
       gas_price=[2.50] * 12 + [2.00] * 24 
    )
    }

DISC = 0.10

TRIALS = 10000


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
    return sum(cf / (1.0 + discount)** (i / 12.0) for (i, cf) in enumerate (net_cf))

def realize_outcome(r: Random, project: Project) -> Outcome:
    return r.choices(project.outcomes, 
                     weights = [o.probability for o in project.outcomes],  k= 1)[0]

def realizations(r: Random, root_projects: Iterable[Project]) -> Iterator[Tuple[Project, Outcome]]:
    for p in root_projects:
        o = realize_outcome(r, p)
        yield(p, o)
        yield from realizations(r, o.leads_to)

_T = TypeVar('_T')
def monte_carlo_trials(r: Random, n: int, root_projects:Iterable[Project], 
            stat_fn: Callable[[Iterator[Tuple[Project, Outcome]]], _T]) -> Iterator[_T]:
    for _ in range(n):
        yield stat_fn(realizations(r, root_projects))

class Stats (NamedTuple):
    mean: float
    p90: float
    p50: float
    p10: float

def extract_stats(xs: List[float]) -> Stats:
    xs.sort()
    n = len(xs)
    return Stats (
        mean = sum(x / n for x in xs), 
        p90 =xs[int(n*0.1)], 
        p50 =xs[int(n*0.5)],
        p10 =xs[int(n*0.9)]
    )

def main(argv: List[str]) -> int:
    # temp_deck = PriceDeck([40.0]* 36, [2.50] * 36)
    r = Random(12345)

    for name, deck in PRICE_DECKS.items():
        npv10 = list(monte_carlo_trials(r, TRIALS, root_projects, 
            lambda rs: sum(npv(net_cashflow(p, o, deck), DISC) for p, o in rs)))
        stats = extract_stats(npv10)
        print(f'{name}: {stats}')

        fig =  plt.figure()
        plt.hist([v/1e6 for v in npv10])
        plt.title(f'NPV10 @ {name} price deck')
        plt.xlabel(f'Total NPV10 ($MM)')
        plt.ylabel(f'Frequency (# of Trials)')
        plt.show()


    return 0 

    # for p in all_projects:
    #     for i, o in enumerate(p.outcomes):
    #         npv10 = npv(net_cashflow(p, o, temp_deck), 0.1)
    #         print(f'{p.name} #{i} -> NPV10 = {npv10}')

if __name__ == '__main__':
    sys.exit(main(sys.argv))