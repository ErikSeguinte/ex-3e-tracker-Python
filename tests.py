import unittest
import ZeltInit


class MyTest(unittest.TestCase):
    def setUp(self):
        ZeltInit.set_up_test()


    def test_for_crash(self):
        """check_for_crash should return known values for known inputs."""

        ZeltInit.print_table()
        known_values = ((0, 2, True),
                        (1, 2, False),
                        (0, 5, True),
                        (3, 4, True),
                        (2, 4, False))
        for combatants, init_damage, correct_value in known_values:
            result = ZeltInit.check_for_crash(combatants, init_damage)
            self.assertEqual(correct_value, result, "Combatant " + str(combatants) + " taking "
                             + str(init_damage) + " damage crashes: " + str(result) + "\n should be: "
                             + str(correct_value))


if __name__ == '__main__':
    unittest.main()
