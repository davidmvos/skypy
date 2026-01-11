# Collections

Collections are a player-specific progress system. Progress can be made by farming, forageing or acquiring the item in another way.

To do anything with collections, the Collection and CollectionItem class may be imported:

```python
from skypy.collections import Collection, CollectionItem
```

Notice: "This method gets" and "This method returns" will be used interchangeably in this documentation.

CollectionItem is a child of collection.

# Collection Class
The collection class represents the entirety of a collection.

## Static Methods and constants
These Methods and constants can be used without creating a `Collection` instance. However, you must use `Collection.method` (or `Collection.CONSTANT`) to access them.

Example:

```python
from skypy.collections import Collection

print(Collection.getAllCollectionKeys())
```

This will output a list of all collection keys.

### Static Methods
These are the static methods:

| Name | Description |
|-|-|
| Collection.getAllCollections(updateCache:bool=False) | Gets all of the collection data. updateCache determines if the cache should be re-build |
| Collection.getAllCollectionKeys() | Gets all the identifying keys of the collections |
| Collection.getAllCollectionNames() | Gets all the friendly names of the collections |

### Static constants

The constants are used to make creating instances easier. They represent the collection categories that are available in-game.

| Name | Value |
|-|-|
| Collection.FARMING | "FARMING" |
| Collection.MINING | "MINING" |
| Collection.COMBAT | "COMBAT" |
| Collection.FORAGING | "FORAGING" |
| Collection.FISHING | "FISHING" |
| Collection.RIFT | "RIFT" |


## Instance Methods

These metods may be used by any `Collection` or `CollectionItem` instance. 
Each `Collection`-Instance represents one of the collection archetypes, and each `CollectionItem` instance represents a item which's collection is tracked. 
As such, the `ColectionItem` class is a child of the `Collection` class.

### Constructing a `Collection` object
To construct a `Collection` object, one must supply the archetype / name of the collection. If a unknown type is given, the constructor will throw a `KeyError`.

Examples:
```python
from skypy.collections import Collection

farming = Collection(Collection.FARMING) # Using a static constant to define what type of collection is wanted

fishing = Collection("fishing") # using a string, which will get normalized to uppercase

wrong = Collection("programming") # will throw a KeyError
```

### `Collection` instance methods
These methods are also **inherited** by the `CollectionItem` class.

| Name | Description |
|-|-|
| get() | Get the complete data of the collection |
| getItemKeys() | Get the names of all the items which are tracked by this collection |
| getItemNames() | Get the friendly names of all the items which are tracked by this collection |

### Constructing a `CollectionItem` object
To create a `CollectionItem` object, a colelction archetype and an item name must be specified. You can get every item of a collection by using `getItemkeys()` (see above)

```python
from skypy.collections import Collection, CollectionItem

cactus = CollectionItem(Collection.FARMING, "CACTUS")

print("Items required for Tier 4: ", cactus.getItemsRequired(4))

```

### `CollectionItem` instance methods
In addition to all of the methods that are listed above and inherited from the `Collection`-Class, a `CollectionItem` will also have these methods.

| Name | Description |
|-|-|
| getItem() | Gets the complete data for this item's progress |
| getMaxTier() | Gets the maximum tier of the collection |
| getName() | Gets the friendly name of the item, as it would appear in-game |
| getTiers() | Gets all of the tier data |
| getTier(tier:int) | Will get the data for the specified tier. Will raise a ValueError if the provided argument is less than one or greater than the max tier of this collection
| getItemsRequired(tier:int) | Will get the amount of items required for this tier's completion |
| getUnlocks(tier:int) | Will get a list of things that are unlocked or given to the player after this tier's completion |
| getAllUnlocks(tier:int) | Will get a list of all things that will have been gotten unlocked once this tier is completed |








