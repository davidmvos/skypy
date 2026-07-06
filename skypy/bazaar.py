import requests
import json
from skypy.items import Item

class Bazaar:
    global _bazaarCache
    _bazaarCache = None
    
    def _updateCache() -> None: 
        global _bazaarCache
        _bazaarCache = json.loads(requests.get("https://api.hypixel.net/v2/skyblock/bazaar").text)

    def getBazaarData(updateCache:bool=True) -> dict[str:object]:
        """
        **(Static method)**
        
        Gets all of the bazaar data
        
        Parameter: updateCache (defaults to true): If the cache should be updated
        """
        
        global _bazaarCache
        if updateCache or _bazaarCache == None:
            Bazaar._updateCache()
        
        return _bazaarCache["products"]
    
    def getAllItemKeys() -> list[str]:
        return list(Bazaar.getBazaarData(updateCache=False).keys())
        
class BazaarItem(Item):
    """
    Represents a Bazaar-tradeable item
    """
    
    @classmethod
    def fromItem(cls, item:Item):
        return cls(item.itemName, False)
    
    def __init__(self, itemName:str, checkName:bool=True):
        super().__init__(itemName=itemName, checkName=checkName)
        if checkName:
            if itemName not in Bazaar.getAllItemKeys():
                raise KeyError(itemName)
        
    
    
    def getBazaarStatus(self) -> dict[str:object]:
        """
        Returns the `quick status` of the item:
        - `sellVolume` and `buyVolume` are the sum of item amounts in all orders.
        - `sellPrice` and `buyPrice` are the weighted average of the top 2% of orders by volume.
        - `movingWeek` is the historic transacted volume from last 7d + live state.
        - `sellOrders` and `buyOrders` are the count of active orders.
        """
        
        return Bazaar.getBazaarData()[self.itemName]["quick_status"]
    
    def getBuyPrice(self) -> float:
        return self.getBazaarStatus()["buyPrice"]
    def getBuyVolume(self) -> float:
        return self.getBazaarStatus()["buyVolume"]
    def getSellPrice(self) -> float:
        return self.getBazaarStatus()["sellPrice"]
    def getSellVolume(self) -> float:
        return self.getBazaarStatus()["sellVolume"]
    
    def getBuySummary(self) ->list[dict[str:object]]:
        """
        Top 30 Buy orders of the item
        """
        return Bazaar.getBazaarData()[self.itemName]["buy_summary"]
    def getSellSummary(self) ->list[dict[str:object]]:
        """
        Top 30 sell offers of the item
        """
        return Bazaar.getBazaarData()[self.itemName]["sell_summary"]
