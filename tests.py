import unittest
import ZeltInit


class MyTest(unittest.TestCase):
    def test_for_crash(self):
        """check_for_crash should return known values for known inputs."""
        a = ZeltInit.Character()
        b = ZeltInit.Character()
        b.initiative = 5
        a.initiative = -5
        list1 = (a, b)
        list2 = (b, a)
        known_values = ((list1, 4, False),
                        (list1, 5, True),
                        (list1, 7, True),
                        (list2, 1, False),
                        (list2, 4, False))
        for combatants, init_damage, correct_value in known_values:
            result = ZeltInit.check_for_crash(combatants, init_damage)
            self.assertEqual(correct_value, result)
