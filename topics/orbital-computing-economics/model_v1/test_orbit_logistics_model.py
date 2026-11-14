import copy
import json
import unittest
from pathlib import Path
from orbit_logistics_model import eclipse_fraction, circular_period_hours, orbit_physics_case, finance_schedule, run_all
HERE=Path(__file__).parent

class R3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base=json.loads((HERE/'inputs.json').read_text())
        cls.life=json.loads((HERE/'inputs_lifecycle.json').read_text())
        cls.s=json.loads((HERE/'inputs_logistics.json').read_text())
    def phys(self, kw=1000, beta=0):
        p=orbit_physics_case(kw,beta,self.base['design'],self.s)
        return {**p['design'], 'beta_deg':beta}
    def scenario(self, repair='annual_repair', price=2, kw=1000):
        return finance_schedule(kw,self.phys(kw),self.life,self.s,self.s['pricing_cases'][price],repair)
    def test_eclipse_max_zero_threshold(self):
        self.assertGreater(eclipse_fraction(550,0),.35)
        self.assertEqual(eclipse_fraction(550,70),0)
        self.assertLess(eclipse_fraction(550,45),eclipse_fraction(550,0))
    def test_eclipse_symmetry(self):
        self.assertAlmostEqual(eclipse_fraction(550,30),eclipse_fraction(550,-30))
    def test_orbit_period(self):
        self.assertTrue(1.55 < circular_period_hours(550) < 1.65)
    def test_550km_mass_exceeds_r1_baseline(self):
        from orbital_cost_model import calculate_design
        self.assertGreater(self.phys()['initial_operational_mass_kg'], calculate_design(1000,self.base['design'])['initial_operational_mass_kg'])
    def test_end_horizon_no_replacement(self):
        for method in ('annual_repair','four_year_refresh_only'):
            x=self.scenario(method)
            self.assertEqual(x['flows'][-1]['delivered_kg'],0)
    def test_annual_dispatch_more_than_batched(self):
        a=self.scenario('annual_repair'); b=self.scenario('four_year_refresh_only')
        self.assertEqual(a['dedicated_flights_lower_bound'],20)
        self.assertEqual(b['dedicated_flights_lower_bound'],5)
        self.assertGreater(a['A_transport_PV_usd'],b['A_transport_PV_usd'])
        self.assertGreater(a['discounted_effective_gpu_h'],b['discounted_effective_gpu_h'])
    def test_no_failure_identical_compute_hours(self):
        settings=copy.deepcopy(self.s);settings['partial_compute_failure_fraction_per_year_assumed']=0
        p=self.phys()
        a=finance_schedule(1000,p,self.life,settings,settings['pricing_cases'][0],'annual_repair')
        b=finance_schedule(1000,p,self.life,settings,settings['pricing_cases'][0],'four_year_refresh_only')
        self.assertAlmostEqual(a['levelized_usd_per_effective_gpu_h'],b['levelized_usd_per_effective_gpu_h'])
    def test_proportional_price_linear_A(self):
        a=self.scenario('annual_repair',0);b=self.scenario('annual_repair',1)
        self.assertAlmostEqual(b['A_transport_PV_usd'],15*a['A_transport_PV_usd'])
        self.assertAlmostEqual(b['B_build_operations_PV_usd'],a['B_build_operations_PV_usd'])
    def test_invalid_inputs(self):
        for kw,beta in [(-1,0),(550,100)]:
            with self.assertRaises(ValueError): eclipse_fraction(kw,beta)
    def test_reconciliation(self):
        for x in run_all(self.base,self.life,self.s)['logistics_cases']:
            self.assertAlmostEqual(x['total_PV_usd'],x['A_transport_PV_usd']+x['B_build_operations_PV_usd'])
            self.assertAlmostEqual(x['total_delivered_mass_kg'],sum(f['delivered_kg'] for f in x['flows']))
            self.assertGreater(x['discounted_effective_gpu_h'],0)
if __name__=='__main__': unittest.main(verbosity=2)
