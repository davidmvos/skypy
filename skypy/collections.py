import requests
import json


class Collection:
    """
    Represents a collection
    """
    global _collectionCache
    _collectionCache = None
    
    def _updateCache() -> None:
        global _collectionCache
        _collectionCache = json.loads(requests.get("https://api.hypixel.net/v2/resources/skyblock/collections").text)
        
    def getAllCollections(updateCache:bool=False) -> dict[str:object]:
        """
        **(Static method)**
        
        Gets all of the collection data
        
        Parameter: updateCache (defaults to false): If the cache should be updated
        """
        global _collectionCache
        
        if updateCache or _collectionCache == None:
            Collection._updateCache()
        
        return _collectionCache["collections"]
    
    def getAllCollectionKeys() -> list[str]:
        """
        **(Static method)**
        
        Gets all the identifying keys of the collections
        """
        return list(Collection.getAllCollections().keys())
    
    def getAllCollectionNames() -> list[str]:
        """
        **(Static method)**
        
        Gets all the friendly names of the collections
        """
        return [Collection.getAllCollections()[el]["name"] for el in Collection.getAllCollectionKeys()]
    
    FARMING = "FARMING"
    MINING = "MINING"
    COMBAT = "COMBAT"
    FORAGING = "FORAGING"
    FISHING = "FISHING"
    RIFT = "RIFT"
    
    def __init__(self, collectionName:str):
        """
        ## Parameters
        **collectionName**: The identifying name / key of the collection 
        
        *(An overview of all keys can be acquired with Collection.getAllCollectionKeys() )*
        """
        self.collectionName = collectionName.upper()
        
        if self.collectionName not in Collection.getAllCollectionKeys():
            raise KeyError(f"{self.collectionName}")
    
    def get(self) -> dict[str:object]:
        """
        Get complete collection data
        """
        return Collection.getAllCollections()[self.collectionName]
    
    def getItemKeys(self) -> list[str]:
        """
        Get the identifying keys of all items of the collection
        """
        return list(self.get()["items"].keys())
    
    def getItemNames(self) -> list[str]:
        """
        Get the friendly names of all the items of the collection
        """
        return [self.get()["items"][el]["name"] for el in self.getItemKeys()]
    
class CollectionItem(Collection):
    def __init__(self, collectionName:str, itemName:str):
        super().__init__(collectionName=collectionName)
        
        self.itemName = itemName
    
        if self.itemName not in self.getItemKeys():
            raise KeyError(f"{self.itemName}")
    
    def getItem(self) -> dict[str:object]:
        """
        Get the complete item data
        """
        return Collection.getAllCollections()[self.collectionName]["items"][self.itemName]
        
    def getMaxTier(self) -> int:
        """
        The maximum tier of the item
        """
        return self.getItem()["maxTiers"]
    
    def getName(self) -> str:
        """
        The friendly name of the item
        """
        return self.getItem()["name"]
    
    def getTiers(self) -> list[dict[str:object]]:
        """
        Get all the tier data
        """
        return self.getItem()["tiers"]
    
    def getTier(self, tier:int) -> dict[str:object]:    
        """
        Data of one tier which must be specified using the tier parameter
        
        ## Parameters
        **tier**:int Specifies the tier. Minimum: 1, Maximum: Can be checked with getMaxTier().
                 
        ## Notice
        **Tier counting begins at 1!**
        """
                
        if (tier < 1 or tier > self.getMaxTier()) and type(tier) == type(1):
            raise ValueError(f"{tier} (Invalid tier)") # TODO: More precise errors
        
        
        assert self.getTiers()[tier-1]["tier"] == tier
        return self.getTiers()[tier-1]
    
    def getItemsRequired(self, tier:int) -> int:
        """
        Get the number of items required to unlock the given tier.
        
        ## Parameters
        **tier**:int Specifies the tier. Minimum: 1, Maximum: Can be checked with getMaxTier().
                 
        ## Notice
        **Tier counting begins at 1!** 
        """
        return self.getTier(tier=tier)["amountRequired"]
    
    def getUnlocks(self, tier:int) -> list[str]: 
        """
        Gets everything that completing this tier unlocks.
        
        ## Parameters
        **tier**:int Specifies the tier. Minimum: 1, Maximum: Can be checked with getMaxTier().
                 
        ## Notice
        **Tier counting begins at 1!**
        
        """
        return self.getTier(tier=tier)["unlocks"]
    
    def getAllUnlocks(self, tier:int) -> list[str]:
        """
        Get everything that will be unlocked up to this tier (including the given tier)
        
        ## Parameters
        **tier**:int Specifies the tier. Minimum: 1, Maximum: Can be checked with getMaxTier().
                 
        ## Notice
        **Tier counting begins at 1!**
        """
        
        unlocks = []
        for i in range(1, tier+1):
            unlocks.extend(self.getUnlocks(i))
        return unlocks

        
        
        
        
        
        
        
    

            