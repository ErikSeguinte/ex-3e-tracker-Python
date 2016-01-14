# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Added
- Attack windows now tracks onslaught
- Added Radio button for successful or failed withering attacks. Successful withering attacks that do 0 damage still give the attacker 1 initiative.
- Attack windows warn if there are less then 2 characters listed.
- Gambits that would cause a character to crash are no longer allowed.
- Customization settings saved to an external file.
- Combat can be saved to and loaded from an external file, either a text file or a binary save file
- Auto save after every turn, round, or never.
- Character at the top of the initiative can be skipped easily.
- Skip allowed a delayed character to remain at the top of the initiative.
- implemented logic to handle creatures of legendary size.
- option to erase all characters, including players. Found in preferences.
- Preferences Window

### Modified
- Modification window: Shift target is now grayed out unless crashed.
- File dialogs default to either directory of last loaded file or application path.
- Character's onslaught Penalty is now reset once they reach the top of the initiative, instead of when
  	they perform an action
- Character's Crash counter is incremented once they reach the top of the initiative, instead of when they perform an action.
- Characters will reset their crash status at the beginning of their 4th turn (when they reach the top of 	initiative), instead of when performing their first action after their 3rd turn.
### Fixed
-   Resetting combat reset's player Character's initiative and crash status.


## [0.1.1] - 2016-01-02
### Added
- Added `Full Defense` to other action window.
- Added this changelog, following the example from  [Keep a Changelog](http://keepachangelog.com/)
### Fixed
- Fixed fatal crash in 'other action' window.
- Possibly fixed packaging so windows version can be opened in Windows older than 10. (Probably still not
   32 bit, though)
- Fixed Typo
## [0.1.0] - 2015-12-24
  * Initial Release.
