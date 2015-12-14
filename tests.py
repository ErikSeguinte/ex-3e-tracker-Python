import unittest

import ZeltInit

Z = ZeltInit


def simulate_round(turns):
    for _i in range(turns):
        Z.handle_withering((0, 1), 0)
        Z.sort_table()


class MyTest(unittest.TestCase):
    def setUp(self):
        print("*****")

        Z.set_up_test()

    def test_for_crash(self):
        """check_for_crash should return known values for known inputs."""
        print("Testing for Crash")
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
            (1, 13, -6, False, True, True, (True, 0, -4)),  # defender crashes from trick
        )
        for damage, n_attacker_init, n_defender_init, a_crash, d_crash, has_gone, \
            tricks, in known_values:
            print("")
            print("")

            combatants = (0, 1)

            a, d = Z.character_list[0], Z.character_list[1]

            Z.handle_withering(combatants, damage, tricks)

            a.shift_target = None
            d.shift_target = None

            self.assertEqual(a.initiative, n_attacker_init,
                             "loop " + str(i) + " " + a.name + " attacking " + d.name)
            self.assertEqual(a.crash_state, a_crash,
                             str(a) + "'s a_crash status is not correct.")

            self.assertEqual(a.has_gone, has_gone, a.name + " should have gone: " + str(has_gone))
            self.assertEqual(d.initiative, n_defender_init)
            self.assertEqual(d.crash_state, d_crash,
                             str(d) + "'s d_crash status is not correct.")

            # Trick Assertions
            i += 1
            Z.sort_table()

    def test_initiative_shift(self):
        print("Testing for Shift")
        for i in range(3):
            Z.handle_withering((0, 1), i, (False, 0, 0))
            Z.sort_table()

        for c in Z.character_list:
            if c.crash_state:
                Z.character_list[4].shift_target = Z.character_list[3]

        # Attacker, Defender, damage, n_att_init, n_def_init, (Tricks, att_trick, def_trick),\
        # a_crash, d_crash, (Crashing, d_crasher)
        # Crashing_Values=(
        #     (0, "No crashing"),
        #     (1, "Crash"),
        #     (2, "Shift!")
        # )
        known_values = (
            (0, 1, 2, 10, 0, (False, 0, 0), False, True, (1, Z.character_list[0])),  # Arnold Crashes Carol
            (2, 4, 10, 16, 0, (False, 0, 0), False, True, (2, None)),  # Shift, init higher than base.
            (3, 2, 1, 3, 0, (False, 0, 0), False, True, (2, None)),  # Shift, init lower than base
        )

        for attacker, defender, damage, n_att_init, n_def_init, trick, a_crash, d_crash, \
            crashing in known_values:

            combatants = (attacker, defender)
            a, d = Z.character_list[attacker], Z.character_list[defender]

            Z.handle_withering(combatants, damage, trick)

            self.assertEqual(d.initiative, n_def_init)
            self.assertEqual(a.crash_state, a_crash)
            self.assertEqual(d.crash_state, d_crash)

            if crashing[0] == 1:
                self.assertEqual(d.shift_target, crashing[1])
            elif crashing[0] == 0:
                self.assertEqual(a.initiative, n_att_init)
            else:
                self.assertTrue(n_att_init <= a.initiative <= (n_att_init + a.join_battle_pool) * 2), \
                a.name + "'s initiative is " + str(a.initiative) + ", but should be between " + str(
                        n_att_init) + " and " + str((n_att_init + a.join_battle_pool) * 2)

            Z.sort_table()

    def test_crash_3_turns(self):
        for i in range(3):
            Z.handle_withering((0, 1), i)
            Z.sort_table()

        # Combatants, damage, n_att_init, n_def_init, crash_status, crash counter

        known_values = self.crash_counter_value_gen()

        combatants, damage, n_att_init, n_def_init, crash_status, counter = next(known_values)
        a, d = Z.character_list[combatants[0]], Z.character_list[combatants[1]]

        Z.handle_withering(combatants, damage)
        Z.sort_table()
        print("")
        self.assertEqual(a.initiative, n_att_init)
        self.assertEqual(d.initiative, n_def_init)
        self.assertTrue(d.crash_state)
        self.assertEqual(d.crash_counter, counter)

        combatants, damage, n_att_init, n_def_init, crash_status, counter = next(known_values)
        a, d = Z.character_list[combatants[0]], Z.character_list[combatants[1]]
        Z.handle_withering(combatants, damage)

        self.assertEqual(a.initiative, n_att_init)
        self.assertTrue(a.crash_state)
        self.assertEqual(a.crash_counter, counter)
        Z.sort_table()
        # End Round 1

        simulate_round(3)
        combatants, damage, n_att_init, n_def_init, crash_status, counter = next(known_values)
        a, d = Z.character_list[combatants[0]], Z.character_list[combatants[1]]
        self.assertEqual(a.initiative, n_att_init)
        self.assertTrue(a.crash_state)
        self.assertEqual(a.crash_counter, counter)

        combatants, damage, n_att_init, n_def_init, crash_status, counter = next(known_values)
        a, d = Z.character_list[combatants[0]], Z.character_list[combatants[1]]
        Z.handle_withering(combatants, damage)
        self.assertEqual(a.initiative, n_att_init)
        self.assertTrue(a.crash_state)
        self.assertEqual(a.crash_counter, counter)
        Z.sort_table()
        # end Round 2

        simulate_round(4)
        combatants, damage, n_att_init, n_def_init, crash_status, counter = next(known_values)
        a, d = Z.character_list[combatants[0]], Z.character_list[combatants[1]]
        self.assertEqual(a.initiative, n_att_init)
        self.assertTrue(a.crash_state)
        self.assertEqual(a.crash_counter, counter)
        combatants, damage, n_att_init, n_def_init, crash_status, counter = next(known_values)
        a, d = Z.character_list[combatants[0]], Z.character_list[combatants[1]]
        Z.handle_withering(combatants, damage)
        self.assertEqual(a.initiative, n_att_init)
        self.assertTrue(a.crash_state)
        self.assertEqual(a.crash_counter, counter)
        Z.sort_table()

        # end Round 3
        simulate_round(4)
        combatants, damage, n_att_init, n_def_init, crash_status, counter = next(known_values)
        a, d = Z.character_list[combatants[0]], Z.character_list[combatants[1]]
        self.assertEqual(a.initiative, n_att_init)
        self.assertTrue(a.crash_state)
        self.assertEqual(a.crash_counter, counter)
        combatants, damage, n_att_init, n_def_init, crash_status, counter = next(known_values)
        a, d = Z.character_list[combatants[0]], Z.character_list[combatants[1]]
        Z.handle_withering(combatants, damage)
        Z.sort_table()
        self.assertEqual(a.initiative, n_att_init)
        self.assertFalse(a.crash_state)
        self.assertEqual(a.crash_counter, counter)

    def test_decisive(self):
        print("Testing Decisive Attacks")
        simulate_round(3)
        init = self.decisive_initiative_generator()
        for c in Z.character_list:
            c.initiative = next(init)
        Z.sort_table()

        known_values = (
            (False, 12),
            (True, 3),
            (False, 8),
            (True, 3),
            (False, 7),
        )

        for success, n_init in known_values:
            a = Z.character_list[0]
            Z.handle_decisive(0, success)
            self.assertEqual(a.initiative, n_init)
            Z.sort_table()

    def crash_counter_value_gen(self):
        values = (
            ((0, 1), 10, 18, -8, True, 0),
            ((3, 1), 0, -8, 1, True, 1),
            ((4, 0), 0, -8, 1, True, 1),
            ((4, 0), 0, -8, 1, True, 2),
            ((4, 0), 0, -8, 1, True, 2),
            ((4, 0), 0, -8, 1, True, 3),
            ((4, 0), 0, -8, 1, True, 3),
            ((4, 0), 1, 5, 17, True, 0),
        )

        for value in values:
            yield value

    def decisive_initiative_generator(self):
        values = (9, 10, 11, 15, 10)
        for value in values:
            yield value

    def test_character_remove(self):
        c_list = Z.character_list

        still_in_play = []
        removed_from_play = []
        for c in c_list:
            still_in_play.append(c)

        Z.print_table()

        for character in still_in_play:
            self.assertIn(character, c_list)

        removed_from_play.append(still_in_play.pop(0))
        Z.remove_from_combat(0)

        for character in still_in_play:
            self.assertIn(character, c_list)

        for character in removed_from_play:
            self.assertNotIn(character, c_list)

        Z.sort_table()
        Z.print_table()

        still_in_play = []
        for c in c_list:
            still_in_play.append(c)
        removed_from_play.append(still_in_play.pop(2))
        Z.remove_from_combat(2)

        for character in still_in_play:
            self.assertIn(character, c_list)

        Z.sort_table()
        Z.print_table()

        for character in removed_from_play:
            self.assertNotIn(character, Z.character_list)


if __name__ == '__main__':
    unittest.main()
