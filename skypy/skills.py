import requests
import json


class Skill:
    """
    Represents a skill.
    """
    
    global _skillCache
    _skillCache = None
    
    def _updateCache() -> None:
        global _skillCache
        _skillCache = json.loads(requests.get("https://api.hypixel.net/v2/resources/skyblock/skills").text)
    
    def getAllSkills(updateCache:bool=False) -> dict[str:object]:
        """
        **(Static method)**
        
        Gets all of the skill data
        
        Parameter: updateCache (defaults to false): If the cache should be updated
        """
        global _skillCache
        
        if _skillCache == None or updateCache:
            Skill._updateCache()
        
        return _skillCache["skills"]
    
    def getAllSkillKeys() -> list[str]:
        """
        **(Static method)**
        
        Gets all the identifying keys of the skills
        """
        return list(Skill.getAllSkills().keys())
    
    def getAllSkillNames() -> list[str]:
        """
        **(Static method)**
        
        Gets all the friendly names of the skills
        """
        return [Skill.getAllSkills()[el]["name"] for el in Skill.getAllSkillKeys()]

    
    
    FARMING = "FARMING"
    MINING = "MINING"
    COMBAT = "COMBAT"
    FORAGING = "FORAGING"
    FISHING = "FISHING"
    ENCHANTING = "ENCHANTING"
    ALCHEMY = "ALCHEMY"
    CARPENTRY = "CARPENTRY"
    RUNECRAFTING = "RUNECRAFTING"
    SOCIAL = "SOCIAL"
    TAMING = "TAMING"
    HUNTING = "HUNTING"
    
    def __init__(self, skillName:str):
        """
        ## Parameters
        **skillName**: The identifying name / key of the skill 
        
        *(An overview of all keys can be acquired with Skill.getAllSkillKeys() )*
        """
        self.skillName = skillName.upper()
        if self.skillName not in Skill.getAllSkillKeys():
            raise KeyError(f"{self.skillName}")
    
    def getSkill(self):
        """
        Get the complete skill data
        """
        return Skill.getAllSkills()[self.skillName]
    
    def getName(self) -> str:
        """
        Get the friendly skill name
        """
        return self.getSkill()["name"]

    def getDescription(self) -> str:
        """
        Get the skill description
        """
        return self.getSkill()["description"]
    
    def getMaxLevel(self) -> int:
        """
        Get the maximum level of the skill
        """
        return self.getSkill()["maxLevel"]
    
    def getLevels(self) -> list[dict[str:object]]:
        """
        Get all the level data of the skill
        """
        return self.getSkill()["levels"]
    
    def getLevel(self, level:int) -> dict[str:object]:
        """
        Gets the data of a specific skill level
        
        ## Parameters
        **level**:int Specifies the level. Minimum: 1, Maximum: Can be checked with getMaxLevel().
                 
        ## Notice
        **Level counting begins at 1!**
        """
        if (level < 1 or level > self.getMaxLevel()) and type(level) == type(1):
            raise ValueError(f"{level} (Invalid level)") # TODO: More precise errors
        
        
        assert self.getLevels()[level-1]["level"] == level
        return self.getLevels()[level-1]
    
    def getExpRequired(self, level:int) -> int:
        """
        Get the amount of XP required to unlcok the specified level.
        
        ## Parameters
        **level**:int Specifies the level. Minimum: 1, Maximum: Can be checked with getMaxLevel().
                 
        ## Notice
        **Level counting begins at 1!**
        """
        return int(self.getLevel(level=level)["totalExpRequired"])
    
    def getUnlocks(self, level:int) -> list[str]:
        """
        Get the unlocks of the specified level.
        
        ## Parameters
        **level**:int Specifies the level. Minimum: 1, Maximum: Can be checked with getMaxLevel().
                 
        ## Notice
        **Level counting begins at 1!**
        """
        return self.getLevel(level=level)["unlocks"]
    
    def getAllUnlocks(self, level:int) -> list[str]:
        """
        Get everything that will be unlocked up to this level, including the given level.
 
        ## Parameters
        **level**:int Specifies the level. Minimum: 1, Maximum: Can be checked with getMaxLevel().
                 
        ## Notice
        **Level counting begins at 1!**
        """
                
        unlocks = []
        for i in range(1, level+1):
            unlocks.extend(self.getUnlocks(i))
        return unlocks
    
    
        
        
    