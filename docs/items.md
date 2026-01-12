# Items

The SkyblockAPI provides an endpoint that lists every item that is currently in-game. 

The items module may be imported in the following way:

Notice: “This method gets” and “This method returns” will be used interchangeably in this documentation.
```python
from skypy.items import Item
```

## Static methods

These methods may be used without creating an `Item`-instance. However, you **must** use `Item.method` to access them.

### Methods

Example:

```python
from skypy.items import Item

# Get the number of SkyBlock Items that are in-game
print(len(Item.getAllItemKeys()))
```
This will output `5312` as of the time of writing this documentation.

| Name | Description |
|-|-|
| Item.getAllItems(upateCache:bool=False) | Get all of the item data. updateCache determines if the cache should be re-build. |
| Item.getAllItemKeys() | Get all the item-ids. |
| Item.getAllItemNames() | Get all of the "friendly names" of the items, as they would appear in-game. |

## Instance Methods

These methods may be used by an `Item`-instance. Each `Item` object represents one of the over 5000 items that are currently available in SkyBlock. 

### Instancing
To create a new `Item`, you need to know the ID of the item that you would like to have your new object represent. These IDs can be found by using the `Item.getAllItemKeys()` static method.
For example, the ID of a tier 2 gold minion is `GOLD_GENERATOR_2`.
```python
from skypy.items import Item

gold_gen_2 = Item("GOLD_GENERATOR_2")

print(gold_gen_2.getName())
```
Prints: `Gold Minion II`

The constructor will raise a `KeyError` if the item type is unknown.

### Instance Methods

After creating an instance, it can execute these functions.

| Name | Description |
|-|-|
| getItemData() | Get the data of the instanced item |
| getMaterial() | Get the minecraft-id reepresentation of the material |
| getName() | Get the in-game friendly name of the item |
| getTier() | Gets the rarity tier |
| getColor() | Gets the item's (name) color |
| getSkinTextureUrl() | If the item is skull, will return a url to an image of the skull texture, but will throw a ValueError if instanced item is not a skull |
| getSkin() | If item is skull, will get the base64 representation of the skin texture, but will throw ValueError if item is not skull |
| getStats() | Get the stats of the item, will throw a ValueError if instanced item des not have stats |
| getDamage() | Get the direct/base damage that this item deals, will throw a ValueError if instanced item des not deal damage. This does not consider any special ability damage |
| getStrength() | Gets the strength of the item, will throw a ValueError if instanced item des not have a strength |


