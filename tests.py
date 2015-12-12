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

    def test_withering(self):
        """Withering attack logic should return known values for known inputs"""
        # (Attacker, defender, damage, new attacker init, new defender init, a_crash, d_crash, has gone)
        known_values = (
            (0, 1, 1, 4, -1, False, True, True),
            (0, 1, 5, 5, -9, False, True, True),
            (0, 1, 10, 7, -5, False, True, False)  # New Round
        )
        for attacker, defender, damage, n_attacker_init, n_defender_init, a_crash, d_crash, has_gone in known_values:
            print("")
            print("")
            combatants = (attacker, defender)
            ZeltInit.handle_withering(combatants, damage)
            self.assertEqual(ZeltInit.character_list[attacker].initiative, n_attacker_init)
            self.assertEqual(ZeltInit.character_list[defender].initiative, n_defender_init)
            self.assertEqual(ZeltInit.character_list[defender].crash_state, d_crash,
                             ZeltInit.character_list[defender].name + "'s d_crash status is not correct.")
            self.assertEqual(ZeltInit.character_list[attacker].crash_state, a_crash,
                             ZeltInit.character_list[attacker].name + "'s a_crash status is not correct.")
            self.assertEqual(ZeltInit.character_list[attacker].has_gone, has_gone)
            ZeltInit.sort_table()
            ZeltInit.print_table()


if __name__ == '__main__':
    unittest.main()
