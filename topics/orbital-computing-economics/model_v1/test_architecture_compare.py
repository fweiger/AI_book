import copy,json,math,unittest
from pathlib import Path
from architecture_compare import avg_survival, p_dispatch, case, run
CFG=json.loads(Path(__file__).with_name('inputs_architecture.json').read_text())
class TestArchitecture(unittest.TestCase):
 def test_prob_exact(self):
  self.assertAlmostEqual(p_dispatch(10,-math.log(.98)),1-.98**10,places=12)
 def test_zero_fail(self):
  self.assertEqual(p_dispatch(10,0),0);self.assertEqual(avg_survival(0,3),1)
 def test_annual_repairs_improve_capacity(self):
  for a in ('serviceable_hub','replaceable_fleet'):
   x=case(CFG,a,'annual','kg_100_whatif'); y=case(CFG,a,'four_year_only','kg_100_whatif')
   self.assertGreater(x['discounted_effective_gpu_h'],y['discounted_effective_gpu_h'])
 def test_expected_shipments_positive(self):
  for x in run(CFG)['cases']:
   self.assertGreater(x['total_expected_delivery_mass_kg'],0)
   self.assertGreater(x['cost_B_pv_usd'],0)
 def test_proportional_freight_identity(self):
  x=case(CFG,'serviceable_hub','annual','kg_100_whatif')
  self.assertAlmostEqual(x['cost_A_pv_usd'],sum(z['expected_kg']*100/1.08**z['year'] for z in x['rows']))
 def test_dedicated_expected_flights_not_20(self):
  x=case(CFG,'serviceable_hub','annual','dedicated_25m_100t_video_whatif')
  self.assertGreater(x['expected_dedicated_launches'],5)
  self.assertLess(x['expected_dedicated_launches'],20)
 def test_fleet_refresh_mass_more(self):
  h=case(CFG,'serviceable_hub','four_year_only','kg_100_whatif')
  d=case(CFG,'replaceable_fleet','four_year_only','kg_100_whatif')
  self.assertGreater(d['total_expected_delivery_mass_kg'],h['total_expected_delivery_mass_kg'])
 def test_robot_cost_raise_hub(self):
  a=copy.deepcopy(CFG);b=copy.deepcopy(CFG);b['robot_capex_usd']*=2
  self.assertGreater(case(b,'serviceable_hub','annual','kg_100_whatif')['levelized_usd_per_gpu_hour'],case(a,'serviceable_hub','annual','kg_100_whatif')['levelized_usd_per_gpu_hour'])
 def test_bad_input(self):
  a=copy.deepcopy(CFG);a['node_failure_hazard_per_year']=-1
  with self.assertRaises(ValueError):run(a)
 def test_fleet_equal_without_failure_in_zero_rate(self):
  a=copy.deepcopy(CFG);a['node_failure_hazard_per_year']=0
  x=case(a,'replaceable_fleet','annual','kg_100_whatif')
  y=case(a,'replaceable_fleet','four_year_only','kg_100_whatif')
  self.assertAlmostEqual(x['levelized_usd_per_gpu_hour'],y['levelized_usd_per_gpu_hour'])
if __name__=='__main__':unittest.main(verbosity=2)