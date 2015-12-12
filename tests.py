import unittest
import ZeltInit


class MyTest(unittest.TestCase):
    def setUp(self):
        ZeltInit.set_up_test()

    def test_for_crash(self):
        """check_for_crash should return known values for known inputs."""
        known_values = ((0, 2, False),
                        (1, 2, True),
                        (0, 5, True),
                        (2, 2, False),)
        for combatants, init_damage, correct_value in known_values:
            result = ZeltInit.check_for_crash(combatants, init_damage)
            self.assertEqual(correct_value, result)


if __name__ == '__main__':
    unittest.main()
