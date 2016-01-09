# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Added
- Attack windows now tracks onslaught
- Added Radio button for successful or failed withering attacks. Successful withering attacks
that do 0 damage still give the attacker 1 initiative.
- Attack windows warn if there are less then 2 characters listed.
- Gambits that would cause a character to crash are no longer allowed.
- Customizable settings saved to an external file.
### Modified
- Modification window: Shift target is now greyed out unless crashed.
- File dialogs default to either directory of last loaded file or application path.
### Fixed



## [0.1.1] - 2016-01-02
### Added
- Added `Full Defense` to other action window.
- Added this changelog, following the example from  [Keep a Changelog](http://keepachangelog.com/)
### Fixed
- Fixed fatal crash in 'other action' window.
- Possibly fixed packaging so windows version can be opened in Windows older than 10. (Probably still not
   32bit, though)
- Fixed Typo
## [0.1.0] - 2016-01-02
  * Initial Release.