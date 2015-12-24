# Exalted 3rd Edition Initiative Tracker

This is an initiative tracker for Onyx Path's 3rd edition Exalted game. Written in Python® 3.5.1, QT 5.5.1, and PyQT 5.5.1. Created by Erik Seguinte <ErikSeguinte@gmail.com>

## How to use
Create a text file that contains a list of your players, each on a new line. While you can add players one by one using the "Add NPC" button, creating this text file in advance allows you to save time since, 1), your players are likely in many of your battles anyway, so you can save typing, and 2), players added in this manner persist when combat is reset, whereas npcs are deleted from the tracker. `todo: option to get players without a text file`

If you are the type of Storyteller who plans out their combats in advance, you can optionally create a seperate text file containing NPCs, each on a new line in the following format `Name, Join Battle Pool, Inert Initiative`, with the values seperated by commas. You can include just the NPC's name and JB Pool (Inert initiative will default to False), or even just the name. The Join Battle Pool will be used to roll for the NPC's join battle in the event that you as the ST don't want to roll for them. You can leave it blank or 0 if you decide that you would rather roll. Inert Initiative takes the values of 'true' or '1' for true, and anything else as false. `todo: Add jb pool functionality to players.`

Additional NPCs can be added using the "Add NPC" button. Here, you can dictate inert initiative, join battle pool, or current initiative as you create them one by one.

Once the tracker is filled, you can use "Join Battle" to get everyone's current initiative. NPCs with join battle pools > 0 will roll their automatically. For everyone else, you will be asked for their successes. **do not add 3** to this number. It should just be the number of successes in their roll. I've found that my players forget to add the three more often then not, and I have to ask whether or not they'd included it, so decided to have the app do it instead. `todo: Option to include +3 on join battle or not`
