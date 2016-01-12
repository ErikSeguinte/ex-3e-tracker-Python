import unittest, os, sys

import ZeltInit, config

Z = ZeltInit


def simulate_round(turns):
    for _i in range(turns):
        Z.handle_withering((0, 1), 0)
        Z.sort_table()


class MyTest(unittest.TestCase):
    def setUp(self):
        print("*****")
        config.TrackerConfig(os.path.dirname(sys.executable))
        # print(Z.config)

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
        i = 1

        known_values = (
            (1, 4, -1, False, True, True, (False, 0, 0)),
            (5, 5, -9, False, True, True, (False, 0, 0)),
            (10, 7, -5, False, True, False, (False, 0, 0)),  # New Round
            (0, 8, 4, False, False, True, (False, 0, 0)),  # test for withering attacks with 0 damage.

            # Testing Tricks
            (0, 5, 1, False, False, True, (True, 0, -2)),  # Reed in the wind
            (0, -5, 1, True, False, True, (True, -2, 0)),  # Attacker crashes himself
            (0, 2, -5, False, True, True, (False, 0, 0)),  # missed attack
            (6, 7, 0, False, True, False, (True, 0, -2)),  # Defender crashes from attack, not trick
            (1, 14, -6, False, True, True, (True, 0, -5)),  # defender crashes from trick
        )
        for damage, n_attacker_init, n_defender_init, a_crash, d_crash, has_gone, \
            tricks, in known_values:
            # print("")
            # print("")

            combatants = (0, 1)

            a, d = Z.character_list[0], Z.character_list[1]

            Z.handle_withering(combatants, damage, tricks)

            a.shift_target = None
            d.shift_target = None

            self.assertEqual(a.initiative, n_attacker_init,
                             "loop " + str(
                                     i) + " " + a.name + " attacking " + d.name + ". Initiative is " + str(
                                     a.initiative) + " but should be " + str(n_attacker_init))
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
            (0, 1, 3, 10, -1, (False, 0, 0), False, True, (1, Z.character_list[0])),  # Arnold Crashes Carol
            (2, 4, 12, 16, 0, (False, 0, 0), False, True, (2, None)),  # Shift, init higher than base.
            (3, 2, 1, 3, 0, (False, 0, 0), False, True, (2, None)),  # Shift, init lower than base
        )

        for attacker, defender, damage, n_att_init, n_def_init, trick, a_crash, d_crash, \
            crashing in known_values:

            combatants = (attacker, defender)
            a, d = Z.character_list[attacker], Z.character_list[defender]

            print("")

            print("")

            Z.handle_withering(combatants, damage, trick)
            print(attacker, "attacks", defender)

            print("")

            print("")

            self.assertEqual(d.initiative, n_def_init)
            self.assertEqual(a.crash_state, a_crash)
            self.assertEqual(d.crash_state, d_crash)

            if crashing[0] == 1:
                self.assertEqual(d.shift_target, crashing[1])
            elif crashing[0] == 0:
                self.assertEqual(a.initiative, n_att_init)
            else:
                self.assertTrue(n_att_init <= a.initiative <= (n_att_init + a.join_battle_pool) * 2), ( \
                    a.name + "'s initiative is " + str(a.initiative) + ", but should be between " + str(
                            n_att_init) + " and " + str((n_att_init + a.join_battle_pool) * 2))

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

        #  Get arnold back to the top of the initiative
        Z.skip_turn()
        Z.sort_table()
        Z.skip_turn()
        Z.sort_table()
        Z.skip_turn()
        Z.sort_table()
        Z.skip_turn()
        Z.sort_table()

        combatants, damage, n_att_init, n_def_init, crash_status, counter = next(known_values)
        a, d = Z.character_list[combatants[0]], Z.character_list[combatants[1]]
        Z.handle_withering(combatants, damage)

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
            Z.handle_decisive((0, 1), success)
            self.assertEqual(a.initiative, n_init)
            Z.sort_table()

    def crash_counter_value_gen(self):
        values = (
            ((0, 1), 10, 19, -8, True, 0),
            ((3, 1), 0, -7, 1, True, 1),
            ((4, 0), 0, -7, 1, True, 1),
            ((4, 0), 0, -6, 1, True, 2),
            ((4, 0), 0, -6, 1, True, 2),
            ((4, 0), 0, -5, 1, True, 3),
            ((4, 0), 0, -5, 1, True, 3),
            ((0, 1), 1, 5, 20, True, 0),
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

        for character in still_in_play:
            self.assertIn(character, c_list)

        removed_from_play.append(still_in_play.pop(0))
        Z.remove_from_combat(0)

        for character in still_in_play:
            self.assertIn(character, c_list)

        for character in removed_from_play:
            self.assertNotIn(character, c_list)

        Z.sort_table()

        still_in_play = []
        for c in c_list:
            still_in_play.append(c)
        removed_from_play.append(still_in_play.pop(2))
        Z.remove_from_combat(2)

        for character in still_in_play:
            self.assertIn(character, c_list)

        Z.sort_table()

        for character in removed_from_play:
            self.assertNotIn(character, Z.character_list)

    def test_onslaught_penalty(self):
        Z.character_list = []
        Z.add_npc("Amber", False, 0, initiative=10)
        Z.add_npc("Billy", False, 0, initiative=8)
        Z.add_npc("Carol", False, 0, initiative=6)
        Z.add_npc("Danny", False, 0, initiative=4)
        Z.sort_table()

        values = (
            (0, 3, -1),  # (Attacker, Defender, new Onslaught
            (0, 2, -2),
            (0, 1, -3),
            (0, 2, -1),

        )

        self.assertEqual(Z.character_list[0].onslaught, 0)
        for attacker, defender, onslaught in values:
            # print
            combatants = attacker, defender
            a = Z.character_list[attacker]
            d = Z.character_list[defender]
            Z.handle_withering(combatants, 0)
            self.assertEqual(d.onslaught, onslaught, str(d.name) + "'s onslaught should be " + str(onslaught))
            self.assertEqual(a.onslaught, 0)
            Z.sort_table()
            print("")

        Z.character_list = []
        Z.add_npc("Amber", False, 0, initiative=10)
        Z.add_npc("Billy", False, 0, initiative=8)
        Z.add_npc("Carol", False, 0, initiative=6)
        Z.add_npc("Danny", False, 0, initiative=4)
        Z.sort_table()
        for attacker, defender, onslaught in values:
            # print
            combatants = attacker, defender
            a = Z.character_list[attacker]
            d = Z.character_list[defender]
            Z.handle_decisive(combatants, False)
            self.assertEqual(d.onslaught, onslaught, str(d.name) + "'s onslaught should be " + str(onslaught))
            self.assertEqual(a.onslaught, 0)
            Z.sort_table()
            print("")

        Z.character_list = []
        Z.add_npc("Amber", False, 0, initiative=10)
        Z.add_npc("Billy", False, 0, initiative=8)
        Z.add_npc("Carol", False, 0, initiative=6)
        Z.add_npc("Danny", False, 0, initiative=4)
        Z.sort_table()
        for attacker, defender, onslaught in values:
            # print
            combatants = attacker, defender
            a = Z.character_list[attacker]
            d = Z.character_list[defender]
            Z.handle_gambits(combatants, False, "Disarm")
            self.assertEqual(d.onslaught, onslaught, str(d.name) + "'s onslaught should be " + str(onslaught))
            self.assertEqual(a.onslaught, 0)
            Z.sort_table()
            print("")

    def test_legendary_size(self):
        Z.reset_combat()
        jack = Z.Character(name='Jack', initiative=3)
        Z.character_list.append(jack)
        giant = Z.Character(name='Giant', initiative=10, legendary_size=True)
        Z.character_list.append(giant)
        Z.sort_table()
        i = 0

        known_values = (
            (5, 9, 5, False),
            (7, 17, 1, False),
            (10, 33, -9, True),
            (1, 35, -9, True)
        )

        for damage, j_init, g_init, crash in known_values:
            if Z.character_list[0] != jack:
                Z.skip_turn()
                Z.sort_table()
            Z.print_table(True)
            Z.handle_withering((0, 1), damage)
            Z.print_table(True)
            self.assertEqual(giant.initiative, g_init, "loop " + str(i))
            self.assertEqual(jack.initiative, j_init, "loop " + str(i))
            self.assertEqual(giant.crash_state, crash, "loop " + str(i))
            i += 1

            # values = iter(known_values)
            #
            # damage, j_init, g_init, crash = next(values)

            # Z.skip_turn()
            # Z.sort_table()
            # Z.handle_withering((0, 1), damage)
            # Z.sort_table()

        # Z.print_table(True)
            # self.assertEqual(giant.initiative, g_init)
            # self.assertEqual(jack.initiative, j_init)
            # self.assertEqual(giant.crash_state, crash)
            #
            # damage, j_init, g_init, crash = next(values)
            # Z.sort_table()
            # Z.handle_withering((0, 1), damage)
            # Z.sort_table()
            #
            # Z.print_table(True)
            # self.assertEqual(giant.initiative, g_init)
            # self.assertEqual(jack.initiative, j_init)
            # self.assertEqual(giant.crash_state, crash)


if __name__ == '__main__':
    unittest.main()
