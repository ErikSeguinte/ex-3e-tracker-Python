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
        # (damage, new attacker init, new defender init, a_crash, d_crash, has gone\
        # (tricks, att_trick, def_trick))
        i = 0

        known_values = (
            (1, 4, -1, False, True, True, (False, 0, 0)),
            (5, 5, -9, False, True, True, (False, 0, 0)),
            (10, 7, -5, False, True, False, (False, 0, 0)),  # New Round
            (0, 7, 4, False, False, True, (False, 0, 0)),  # test for missed withering attacks.

            # Testing Tricks
            (0, 4, 1, False, False, True, (True, 0, -2)),  # Reed in the wind
            (0, -6, 1, True, False, True, (True, -2, 0)),  # Attacker crashes himself
            (0, 1, -5, False, True, True, (False, 0, 0)),  # missed attack
            (5, 6, 0, False, True, False, (True, 0, -2)),  # Defender crashes from attack, not trick
            (1, 11, -6, False, True, False, (True, 0, -4)),  # defender crashes from trick
        )
        for damage, n_attacker_init, n_defender_init, a_crash, d_crash, has_gone, \
            tricks, in known_values:
            print("")
            print("")

            combatants = (0, 1)

            shifting = False
            a, d = Z.character_list[0], Z.character_list[1]

            if a.shift_target is d and Z.check_for_crash(combatants[1], damage - tricks[2]):
                shifting = True

            print("*****" + str(a) + " is attacking " + str(d))
            Z.handle_withering(combatants, damage, tricks)

            if not shifting:
                self.assertEqual(a.initiative, n_attacker_init,
                                 "loop " + str(i) + " " + a.name + " attacking " + d.name)
            else:
                self.assertTrue(a.initiative >= 3,
                                str(a) + "'s initiative is: " + str(a.initiative) + " in loop: " + str(
                                    i) + ", Post Shift")
            self.assertEqual(a.crash_state, a_crash,
                             str(a) + "'s a_crash status is not correct.")

            self.assertEqual(a.has_gone, has_gone, a.name + " should have gone: " + str(has_gone))
            self.assertEqual(d.initiative, n_defender_init)
            self.assertEqual(d.crash_state, d_crash,
                             str(d) + "'s d_crash status is not correct.")

            # Trick Assertions
            i += 1
            Z.sort_table()
            Z.print_table()

    # def test_multiple_rounds(self):
    #     """Test for round counting logic.
    #
    #     Tests for initiative break bonus denial after coming out of crash,
    #     coming out of crash after 3 turns
    #     """
    #     pass

    # def test_gambits(self):
    #     """Tests Gambits"""
    #     print("Testing Gambits")
    #
    #
    #     Z.print_table()
    #     known_values = (
    #         (0)
    #     )


    def test_initiative_shift(self):
        for i in range(3):
            Z.handle_withering((0, 1), i, (False, 0, 0))
            Z.sort_table()

        Z.print_table()
        # Attacker, Defender, damage, n_att_init, n_def_init, (Tricks, att_trick, def_trick),\
        # a_crash, d_crash, (Crashing, d_crasher)
        # Crashing_Values=(
        #     (0, "No crashing"),
        #     (1, "Crash"),
        #     (2, "Shift!")
        # )
        known_values = (
            (0, 1, 2, 10, 0, (False, 0, 0), False, True, (1, Z.character_list[0])),  # Arnold Crashes Carol
            (2, 4, 10, None, 0, (False, 0, 0), False, True, (2, None)),  # Shift
        )

        for attacker, defender, damage, n_att_init, n_def_init, trick, a_crash, d_crash, \
            crashing in known_values:
            print("")
            print("")
            combatants = (attacker, defender)
            a, d = Z.character_list[attacker], Z.character_list[defender]
            print(combatants, damage)
            Z.handle_withering(combatants, damage, trick)

            self.assertEqual(d.initiative, n_def_init)
            self.assertEqual(a.crash_state, a_crash)
            self.assertEqual(d.crash_state, d_crash)

            if crashing[0] == 1:
                self.assertEqual(d.shift_target, crashing[1])
            elif crashing[0] == 0:
                self.assertEqual(a.initiative, n_att_init)
            else:
                self.assertTrue(3 <= a.initiative < 16,
                                a.name + "'s initiative is " + str(a.initiative) + ", but should be lower.")

            Z.sort_table()
            Z.print_table()

            # def test_decisive(self):
            #     """Tests decisive attacks against known values and inputs"""
            #     for i in range(13):
            #         Z.handle_withering((0, 1), i, (False, 0, 0))
            #         Z.sort_table()
            #     # success, new_init,
            #     known_values = (
            #         (True, 3),  # Successful
            #         (False, 10),  # Failed, init >=11
            #         (False, 6),  # Failed, init <11
            #     )
            #     print("Testing Decisive Attacks.")
            #     # Z.print_table()
            #
            #     for success, new_init in known_values:
            #         Z.handle_decisive(0, success)
            #         self.assertEqual(Z.character_list[0].initiative, new_init)
            #         self.assertTrue(Z.character_list[0].has_gone)
            #         print("")
            #         print("")
            #         Z.sort_table()
            #         # Z.print_table()


if __name__ == '__main__':
    unittest.main()
