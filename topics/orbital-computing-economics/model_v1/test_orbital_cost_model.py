import copy
import json
import unittest
from pathlib import Path
from orbital_cost_model import SIGMA, calculate_design, run

class ModelV1Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cfg = json.loads((Path(__file__).parent / "inputs.json").read_text(encoding="utf-8"))

    def test_power_and_mass_balance(self):
        c = run(self.cfg)["physical_cases"]
        self.assertEqual([v["it_kw"] for v in c], [100, 1000, 10000])
        for v in c:
            self.assertAlmostEqual(v["power_balance_residual_kw"], 0, delta=1e-9)
            self.assertAlmostEqual(sum(v["mass_items_kg"].values()), v["initial_operational_mass_kg"], delta=1e-6)
            self.assertGreaterEqual(v["radiator_model_area_m2"], v["radiator_ideal_area_m2"])
        self.assertAlmostEqual(c[1]["initial_operational_mass_kg"], c[0]["initial_operational_mass_kg"] * 10, delta=1e-6)

    def test_historical_stefan_boltzmann(self):
        self.assertAlmostEqual(1000000 / (SIGMA * 350**4), 1175.14, delta=1)

    def test_dedicated_launch_lower_bounds(self):
        for c in run(self.cfg)["physical_cases"]:
            l = c["dedicated_launch_scenario"]
            self.assertGreaterEqual(l["minimum_flights_by_mass"] * l["assumed_effective_mass_capacity_kg"], c["initial_operational_mass_kg"])

    def test_static_bcg_cost_floor(self):
        z = run(self.cfg)["bcg_anchored_cost_floor_sensitivity"]
        self.assertAlmostEqual(z["orbital_tco_if_transport_cost_reduced_90pct_usd_per_mw"], 574000000)
        self.assertGreater(z["cost_gap_even_if_transport_zero_usd_per_mw"], 0)

    def test_invalid_inputs_are_rejected(self):
        d = self.cfg["design"]
        for key, value in [
            ("eclipse_fraction", 1), ("solar_array_specific_power_w_per_kg", 0),
            ("battery_discharge_efficiency", -1), ("radiator_temperature_kelvin", 100),
            ("radiator_emissivity", float("nan"))
        ]:
            candidate = copy.deepcopy(d)
            candidate[key] = value
            with self.assertRaises(ValueError):
                calculate_design(100, candidate)

    def test_eclipse_changes_battery_and_pv_mass(self):
        d = self.cfg["design"]
        no = calculate_design(100, dict(d, eclipse_fraction=0))
        yes = calculate_design(100, d)
        self.assertGreater(yes["mass_items_kg"]["battery_pack_kg"], no["mass_items_kg"]["battery_pack_kg"])
        self.assertGreater(yes["mass_items_kg"]["solar_array_kg"], no["mass_items_kg"]["solar_array_kg"])

if __name__ == "__main__":
    unittest.main(verbosity=2)
