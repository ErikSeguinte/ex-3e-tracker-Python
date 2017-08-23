# Exalted 3rd Edition Initiative Tracker

This is an initiative tracker for Onyx Path's 3rd edition Exalted game. Written in
Python® 3.5.1, QT 5.5.1, and PyQT 5.5.1. Bundled using PyInstaller.

Developed using Test Driven Development and UnitTest.

Created by
 Erik Seguinte <ErikSeguinte@gmail.com>

## Features

*   Keeps track of Initiative, Initiative Break, initiative shift, and Crash
*   Handles battle groups(inert initiative) and creatures with legendary size (Cannot be crashed unless damage > 10)
  *   Note that Legendary Size and Inert Initiative are mutually exclusive. Their rule sets initiative wise are not compatible. (Though it is my belief that battle groups of tyrant lizards should be encouraged!)
*   A round-progress bar at the bottom to help remind you about regaining motes.
    `todo: Option to have a new round popup message?`
*   Automatically resets to base initiative if a character survives 3 turns in crash,
    at the beginning of their 4th turn.
*   Cannot gain a Initiative Break Bonus if the target had returned from crash this
    round or the one before it.
*   Keeps track of who crashed whom for Shift purposes
*   Initiative shift keeps a character at the top of the initiative.
    `todo: Rolls join battle for NPCs. currently does not ask for JB from player, has to be added manually.`
*   Characters that have gone this round will always be beneath those that have not,
    but otherwise everyone is kept in initiative order.
*   Delaying keeps a character at the top of the initiative.
    `todo: some sort of reminder to prevent a delaying character from wasting a round`
*   Players and NPCs can be added from a text file.
*   Can automatically roll Join Battle for NPCs, given a JB pool.
*   Players persist through combat reset by default. This can be changed in preferences.
*   Successful gambits cost (difficulty + 1) Initiative to perform
*   Successful Decisive Attacks reset initiative to 3.
*   Failed Decisive/Gambits cost initiative depending on current initiative.
*   Save and load combats, loading current initiative, order, etc
*   Auto save of combats, configurable to every turn, every round, or never. Defaults to every turn.
*   Resume auto-save without choosing a file.
*   Font can be changed to accomodate usage on a big screen for sharing. (Please see Known Issues below.)



## How to use
You may create a text file that contains a list of your players, each on a new line. While you
can add players one by one using the "Add Character" button, creating this text file in
advance allows you to save time since your players are likely in many of your
battles anyway.

If you are the type of Storyteller who plans out their combats in advance, you can
optionally create a separate text file containing NPCs, each on a new line in the
following format `Name, Join Battle Pool, Inert Initiative`, with the values
separated by commas. You can include just the NPC's name and JB Pool (Inert
initiative will default to False), or even just the name. The Join Battle Pool will
be used to roll for the NPC's join battle in the event that you as the ST don't
want to roll for them. You can leave it blank or 0 if you decide that you would
rather roll. Inert Initiative takes the values of `true` or `1` for true, and anything
 else as false. `todo: Add jb pool functionality to players.`

Examples for both files are included in the Zip file as players.txt and npcs.txt, respectively.

Alternatively, you can fill the tracker with your NPCs and save the combat into a separate file using the save functions.
You have the option of using a binary file, or a text file for these saves. Binary file has
the advantage of letting you have duplicate names, but otherwise should be identical.
Text saves have a slightly lower chance of breaking between versions (Assuming I change the underlying code).

These files can be loaded from the Edit menu.

Additional NPCs can be added using the "Add Character" button. Here, you can dictate inert
 initiative, join battle pool, current initiative, and legendary size as you create them one by one.

Once the tracker is filled, you can use "Join Battle" to get everyone's current
initiative. NPCs with join battle pools > 0 will roll theirs automatically. For everyone
else, you will be asked for their successes. By default, **do not manually add 3**
to this number. It
should just be the number of successes in their roll. I've found that my players forget
 to add the three more often then not, and I have to ask whether or not they'd
 included it, so decided to have the app do it instead. This can be modified in preferences.

For withering attacks and decisive/gambits, you have the option to add initiative
modifiers. If, for example, the defender is using Reed in the Wind to increase his
DV, you would enter `-2`.

For attacks, mark success or failure.

When fighting battle groups, fill the rout check box with the number of rout checks forced onto the battle group.
There's currently a dispute amongst my group whether or not multiple rout-checks allow for multiple
initiative crash bonuses. I've programmed that possibility into this program, so if you force 2 rout checks, you'll
gain 10 initiative as a bonus. If you disagree, you may leave the rout check at one. This option should be grayed
out unless the defender has inert initiative.

When fighting creatures of Legendary size, a check-box has been provided asking if post-soak damage exceeds 10.
Unless this box is checked, it will be impossible to bring the creature's initiative lower than 1. This option
is grayed out unless applicable.

"Other Actions" include Aim, Delay, withdraw, Full Defense and disengage.

Modify Character allows you to manually edit a character's flags and initiative. NOTE: Inert initiative takes
precedence over legendary size.

Reset removes any characters not loaded through the `add Player` function.

Skip flips the top character's has_gone flag to True, effectively skipping them.
This option will ignore delaying characters. Note: This is for characters who choose
to do nothing that interacts with initiative during their turn, not for delaying. Use
'other action' for delaying a turn to go later in the same round.

Custom Gambits that are used frequently can be added for reuse later from the edit menu.
Use the format "Name : Difficulty", with each gambit seperated by a new line. The default
gambits cannot be modified, they will be regenerated if deleted or changed.
The custom gambits will be saved to the config file.

## Known Issues
### General
- Upgrading while keeping an old config file may cause issues. If things aren't working right, please try deleting or renaming the config file.
- If you have both a custom overall font and a different tracker table font, the overall font will over ride the tracker table font on start up.
### Mac
- The default native style doesn't appear to like resizing elements when font size is increased. Combo boxes and buttons will stay the same size regardless of how big the font it inside of it.
  - **Workaround:** The Fusion style may work a little better. The comboboxes grow, but the labels don't.


