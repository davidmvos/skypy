# Skills

Skills are player-specific leveling system. They unlock different things. Everything that has to do with skills can be accessed in the skills module, which may be imported in this way:

```python
from skypy.skills import Skill
```

This will import the `Skill`-Class. 

Notice: "This method gets" and "This method returns" will be used interchangeably in this documentation.

## Static Methods and constants
These Methods and constants can be used without creating a Skills instance. However, you must use `Skill.method` (or `Skill.CONSTANT`) to access them.

### Methods

Example: 

```python
from skypy.skills import Skill

print(Skill.getAllSkillNames())
```
Will print: `['Farming', 'Mining', 'Combat', 'Foraging', 'Fishing', 'Enchanting', 'Alchemy', 'Carpentry', 'Runecrafting', 'Social', 'Taming', 'Hunting']`


| Name | Description |
|------|-------------|
| Skill.getAllSkills(updateCache:bool=False) |  Gets all of the skill data. updateCache determines if the cache should be re-build. |
| Skill.getAllSkillKeys() | Gets all the identifying keys of the skills, which then may be used to create an instance. |
| Skill.getAllSkillNames() | Gets all the friendly names of the skills (how they are displayed in-game) | 

### Constants

The constants are used to make creating instances easier. They represent the skill categories that are in-game.

Example: (Creating a farming skill object)
```python
from skypy.skills import Skill 

farming = Skill(Skill.FARMING) # Skill.FARMING is used to identify the farming skill

print(farming.getDescription())
```

Will print: `Harvest crops and shear sheep to earn Farming XP!` 


| Name | Value | In-Game-Description |
|-|-|-|
| Skill.FARMING | "FARMING" | Harvest crops and shear sheep to earn Farming XP! |
| Skill.MINING | "MINING" | Dive into deep caves and find rare ores and valuable materials to earn Mining XP! |
| Skill.COMBAT | "COMBAT" | Fight mobs and special bosses to earn Combat XP! |
| Skill.FORAGING | "FORAGING" | Cut trees and forage for other plants to earn Foraging XP! |
| Skill.FISHING | "FISHING" | Visit your local pond to fish and earn Fishing XP! |
| Skill.ENCHANTING | "ENCHANTING" | Enchant items to earn Enchanting XP! |
| Skill.ALCHEMY | "ALCHEMY" | Brew potions to earn Alchemy XP! |
| Skill.CARPENTRY | "CARPENTRY" | Craft items to earn Carpentry XP! |
| Skill.RUNECRAFTING | "RUNECRAFTING" | Slay bosses and runic mobs, and fuse runes to earn Runecrafting XP! |
| Skill.SOCIAL | "SOCIAL" | Gain Social XP for every new unique guest, hosting guests, and visiting islands! |
| Skill.TAMING | "TAMING" | Level up pets to earn Taming XP! |
| Skill.HUNTING | "HUNTING" | Hunt various monsters to earn Hunting XP! |

## Instance Methods

These are methods that may be used by a `Skill`-instance. Each skill-instance represents one of the skill trees (see above!) exclusively, so "skill" refers to the skill tree that they were initialized with.

### Instancing
The constructor method only takes one argument: The name of the skilltree. capitalization will be normalized to uppercase. The constuctor method will raise a KeyError if such a skilltree does not exist.

Examples:

```python
from skypy.skills import Skill 

farming = Skill(Skill.FARMING) # Skill.FARMING is used as a helper to identify the farming skill

combat = Skill("combat") # here, combat is used directly to select the combat-skilltree

wrong = Skill("programming") # will throw a KeyError
```

### Instance Methods

**Notice: The counting of levels begins at 1!**

| Name | Description |
|-|-|
| getSkill() | Get the complete skill data |
| getName() | Get the friendly name of the skill, as it would appear in-game. |
| getDescription() | Get the in-game description of the skill |
| getMaxLevel() | Get the maximum level of the skill |
| getLevels() | Get all the levels of the skill (in a list)
| getLevel(level:int) | Will get the data for the provided level. Will raise a ValueError if the provided argument is less than one or greater than the max level of this skill. |
| getExpRequired(level:int) | Will return the required Experience for the provided level |
| getUnlocks(level:int) | Will get a list of things that will be unlocked/given to the player once the given level is completed |
| getAllUnlocks(level:int) | Will get a list of all things that will have been gotten unlocked once this level is completed |






  
