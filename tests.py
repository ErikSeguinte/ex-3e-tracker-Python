import unittest
import ZeltInit

Z = ZeltInit


class MyTest(unittest.TestCase):
    def setUp(self):
        print("*****")
        for i in range(5):
            print("")

        Z.set_up_test()

    def test_for_crash(self):
        """check_for_crash should return known values for known inputs."""
        print("Testing for Crash")
        # ZeltInit.print_table()
        known_values = (
            (0, 2, True),
            (1, 2, False),
            (0, 5, True),
            (3, 4, True),
            (2, 4, False)
        )
        for combatants, init_damage, correct_value in known_values:
            result = Z.check_for_crash(combatants, init_damage)
            self.assertEqual(correct_value, result, "Combatant " + str(combatants) + " taking "
                             + str(init_damage) + " damage crashes: " + str(result) + "\n should be: "
                             + str(correct_value))

    def test_withering(self):
        """Withering attack logic should return known values for known inputs"""
        print("Testing for Withering Attacks")
        # (Attacker, defender, damage, new attacker init, new defender init, a_crash, d_crash, has gone)
        known_values = (
            (0, 1, 1, 4, -1, False, True, True),
            (0, 1, 5, 5, -9, False, True, True),
            (0, 1, 10, 7, -5, False, True, False),  # New Round
            (0, 1, 0, 7, 4, False, False, True),  # test for missed withering attacks.
        )
        for attacker, defender, damage, n_attacker_init, n_defender_init, a_crash, d_crash, has_gone in known_values:
            print("")
            print("")
            combatants = (attacker, defender)
            Z.handle_withering(combatants, damage)
            self.assertEqual(Z.character_list[attacker].initiative, n_attacker_init)
            self.assertEqual(Z.character_list[defender].initiative, n_defender_init)
            self.assertEqual(Z.character_list[defender].crash_state, d_crash,
                             Z.character_list[defender].name + "'s d_crash status is not correct.")
            self.assertEqual(Z.character_list[attacker].crash_state, a_crash,
                             Z.character_list[attacker].name + "'s a_crash status is not correct.")
            self.assertEqual(Z.character_list[attacker].has_gone, has_gone)

            Z.sort_table()
            Z.print_table()

    def test_multiple_rounds(self):
        """Test for round counting logic.

        Tests for initiative break bonus denial after coming out of crash,
        coming out of crash after 3 turns
        """

        #
        # def test_decisive(self):
        #     """Tests decisive attacks against known values and inputs"""
        #     # success, new_init
        #     Z = ZeltInit
        #     print("Testing Decisive Attacks.")
        #     Z.print_table()


if __name__ == '__main__':
    unittest.main()
