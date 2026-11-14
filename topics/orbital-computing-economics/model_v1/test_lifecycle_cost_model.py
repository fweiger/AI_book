import copy
import json
import unittest
from pathlib import Path
from lifecycle_cost_model import run_case, run_all

HERE=Path(__file__).parent

class LifecycleCostModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.physics=json.loads((HERE/'inputs.json').read_text(encoding='utf-8'))
        cls.life=json.loads((HERE/'inputs_lifecycle.json').read_text(encoding='utf-8'))
    def case(self,kw=1000,p=100,mods=None):
        x=copy.deepcopy(self.life)
        if mods: x['scenario_prices'].update(mods)
        return run_case(kw,self.physics['design'],x,p)
    def test_mass_and_cashflow_ledger_reconcile(self):
        c=self.case()
        self.assertEqual(len(c['yearly_cashflows']),21)
        self.assertAlmostEqual(c['orbital_A_20y_undiscounted_usd']+c['orbital_B_20y_undiscounted_usd'],c['orbital_20y_total_undiscounted_usd'],delta=.01)
        self.assertAlmostEqual(sum(c['orbital_B_initial_build_item_costs_usd'].values()),c['yearly_cashflows'][0]['orbital_B_build_ops_usd'],delta=.01)
    def test_launch_zero_saves_transport_only(self):
        x=self.case(p=1500);z=self.case(p=0)
        self.assertEqual(z['orbital_A_20y_undiscounted_usd'],0)
        self.assertAlmostEqual(x['orbital_B_20y_undiscounted_usd'],z['orbital_B_20y_undiscounted_usd'])
    def test_break_even_reproduces_gpu_hour_parity(self):
        c=self.case(mods=self.life['what_if_modifiers']['high_availability_low_manufacturing'])
        p=c['break_even_transport_usd_per_kg_for_levelized_GPU_hour_parity']
        self.assertGreater(p,0)
        at=self.case(p=p,mods=self.life['what_if_modifiers']['high_availability_low_manufacturing'])
        self.assertAlmostEqual(at['cost_ratio_levelized_orbit_to_ground'],1,delta=1e-10)
    def test_negative_threshold_has_no_nonnegative_launch_price_solution(self):
        x=self.case(mods=self.life['what_if_modifiers']['lower_space_manufacturing'])
        self.assertLess(x['break_even_transport_usd_per_kg_for_levelized_GPU_hour_parity'],0)
        self.assertFalse(x['break_even_feasible_at_nonnegative_transport_price'])
    def test_discounted_cost_below_nominal(self):
        c=self.case()
        self.assertLess(c['orbital_20y_total_real_pv_usd'],c['orbital_20y_total_undiscounted_usd'])
        self.assertLess(c['orbital_discounted_effective_gpu_h'],c['gpu_count_assumed']*8760*20)
    def test_higher_failure_increases_B_and_A(self):
        b=self.case(p=1500)
        high=self.case(p=1500,mods={'orbit_annual_whole_module_loss_probability':0.02})
        self.assertGreater(high['orbital_B_20y_undiscounted_usd'],b['orbital_B_20y_undiscounted_usd'])
        self.assertGreater(high['orbital_A_20y_undiscounted_usd'],b['orbital_A_20y_undiscounted_usd'])
    def test_longer_refresh_reduces_total_cost(self):
        old=self.case(p=1500)
        newer=self.case(p=1500,mods={'orbit_refresh_period_years':6})
        self.assertLess(newer['orbital_20y_total_undiscounted_usd'],old['orbital_20y_total_undiscounted_usd'])
    def test_nonnegative_invalid_parameters(self):
        for k,v in [('orbit_availability',1.1),('gpu_unit_price_usd',-1),('orbit_refresh_period_years',0),('gpu_tdp_w',0),('real_discount_rate_per_year',2)]:
            x=copy.deepcopy(self.life)
            if k in x['scenario_prices']:x['scenario_prices'][k]=v
            else:x[k]=v
            with self.assertRaises(ValueError,msg=k):run_case(1000,self.physics['design'],x,100)
    def test_scenario_grid_count(self):
        r=run_all(self.physics,self.life)
        self.assertEqual(len(r['cases']),len(self.life['it_kw_scales'])*len(self.life['transport_usd_per_operational_kg_scenarios'])*len(self.life['what_if_modifiers']))
    def test_gpu_hour_not_identical_to_it_megawatt_hours(self):
        c=self.case()
        self.assertEqual(c['gpu_count_assumed'],1000)
        self.assertGreater(c['ground_discounted_effective_gpu_h'],c['orbital_discounted_effective_gpu_h'])

if __name__=='__main__': unittest.main(verbosity=2)