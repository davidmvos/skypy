import json
import requests
import base64
from typing import final

class Item:
    global _itemCache
    _itemCache = None
    
    def _updateCache():
        global _itemCache
        _itemCache = json.loads(requests.get("https://api.hypixel.net/v2/resources/skyblock/items").text)
        print("Cache updated!")
    
    def getAllItems(upateCache:bool=False) -> list[dict[str:object]]:
        """
        get all of the item data
        """
        global _itemCache
        if upateCache or _itemCache == None:
            Item._updateCache()
        
        return _itemCache["items"]
    
    def getAllItemKeys() -> list[str]:
        """
        Get all of the item IDs
        """
        return [el["id"] for el in Item.getAllItems()]
    
    def getAllItemNames() -> list[str]:
        """
        Get all of the item friendly names
        """
        return [el["name"] for el in Item.getAllItems()]
    
    def __init__(self, itemName:str):
        self.itemName = itemName.upper()
        
        if self.itemName not in Item.getAllItemKeys():
            raise KeyError(self.itemName)
        
        self.itemDataCache = None
        
        # Write cache
        self.getItemData()
        
    def _getItemData(self) -> dict[str:object]:
        """
        Get item data for instanced item without using the cache. This has the time complexity of O(n) (with n=num items) because the array of items is not indexed.
        """
        foundElement = None
        for el in Item.getAllItems():
            if el["id"] == self.itemName:
                foundElement = el
                
        assert foundElement != None # TODO: Add key error here
        
        return foundElement
    
    def getItemData(self) -> dict[str:object]:
        """
        Get the data of the instanced item (in O(1) time after initialization)
        """
        if self.itemDataCache == None:
            self.itemDataCache = self._getItemData()
        return self.itemDataCache
    
    def getMaterial(self) -> str:
        """
        Get the minecraft-id reepresentation of the material.
        """
        return self.getItemData()["material"]
    
    def getName(self) -> str:
        """
        Get the in-game friendly name of the item.
        """
        return self.getItemData()["name"]
    
    def getTier(self) -> str: # ["COMMON", "UNCOMMON", "RARE", "EPIC", "LEGENDARY", "MYTHIC", "SUPREME", "SPECIAL", "VERY_SPECIAL"]:
        """
        Gets the rarity tier (like uncommon)
        """
        return self.getItemData()["tier"]
    
    def getColor(self) -> str:
        """
        Gets the item's (name) color
        """
        return self.getItemData()["color"]
    
    def getSkinTextureUrl(self) -> str:
        """
        IF item is skull, will return a url to an image of the skull texture. 
        
        Will throw a ValueError if instanced item is not a skull.
        """
        decoded = base64.b64decode(self.getSkin()).decode("utf-8")
        skinData = json.loads(decoded)
        
        return skinData["textures"]["SKIN"]["url"]
    
    def getSkin(self) -> str:
        """
        If item is skull, will get the base64 representation of the skin texture.
        
        Will throw a ValueError if instanced item is not a skull.
        """
        try:
            return self.getItemData()["skin"]["value"]
        except KeyError:
            ex = TypeError(self.itemName)
            ex.add_note("This item does not have a skull texture")
            raise ex
    
    def getStats(self) -> dict[str:object]:
        """
        Get the stats of the item.
        
        Will throw a ValueError if instanced item des not have stats.
        """
        try:
            return self.getItemData()["stats"]
        except KeyError:
            ex = TypeError(self.itemName)
            ex.add_note("This item does not have any stats")
            raise ex
    
    def getDamage(self) -> int:
        """
        Get the damage that this item deals.
        
        Will throw a ValueError if instanced item des not deal damage.
        """
        try:
            return int(self.getStats()["DAMAGE"])
        except KeyError:
            ex = TypeError(self.itemName)
            ex.add_note("This item does not deal any damage")
            raise ex
    
    def getStrength(self) -> int:
        """
        Gets the strength of the item.
        
        Will throw a ValueError if instanced item des not have a strength.
        """
        try:
            return int(self.getStats()["STRENGTH"])
        except KeyError:
            ex = TypeError(self.itemName)
            ex.add_note("This item does not have any strength")
            raise ex
        
        
    
    
    
    
    