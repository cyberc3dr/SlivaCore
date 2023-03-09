SlivaCore
======

High performance CraftBukkit server fork


How To
-----------

Apply Patches : `python3 patcher.py applyPatches`

### Create patch for server ###

`cd SlivaCore-Server`

Add files for commit : `git add .`

Commit : `git commit -m <msg>`

`cd ..`

Create Patch `python3 patcher.py rebuildPatches`

### Create patch for API ###

`cd SlivaCore-API`

Add files for commit : `git add .`

Commit : `git commit -m <msg>`

`cd ..`

Create Patch `python3 patcher.py rebuildPatches`




Compilation
-----------

We use maven to handle our dependencies.

* Install [Maven 3](http://maven.apache.org/download.html)
* Clone this repo and: `mvn clean install`
