# iOS Shortcuts
A collection of shortcuts for the [Shortcuts app](https://support.apple.com/en-ca/HT208309).

_(To view the original collection of Workflows for iOS 11 and earlier using Workflow App, [click here](https://github.com/heliomass/iOSWorkflows/tree/v1).)_

## Table of Contents

* [Replenish](#-replenish)
* [Cab Fare Calculator](#-cab-fare-calculator)
* [Office Bucket](#-office-bucket)
* [Do Not Disturb](#-do-not-disturb)
* [Down for Everyone?](#-down-for-everyone)
* [Brew Tea](#-brew-tea)
* [Metro Status](#-metro-status)
* [Bixi](#-bixi)
* [Search](#-search)
* [Guess the Number](#-guess-the-number)
* [Functions](#-functions)

## ![](readme_images/replenish-icon-small.png) Replenish
### Description
This Shortcut helps you and your family to manage replacing essential items around the house. For example, if you run out of coffee, run the shortcut, simply select "Coffee" and let the rest of the magic happen:

* The item will be added to a shared Reminders list.
* You'll get an alert when you're nearby the designated shop for that item.
* A text will be sent to chosen people to let them know the item has run out.

![](readme_images/replenishitem01.png)

### Installation
Installation and setup requires a few separate steps to complete, but once done you won't need to make any changes except to add or remove items.
    
1. **Configure the list of Items and Locations**

    The Shortcut consults a JSON file of these items. Named `replenish_items.json`, it lives in the Shortcuts folder of your iCloud drive.
    
    To stare you off, there's an example file [here](replenish_items.json), but obviously you'll want to adjust it to your own needs. The easiest way to do this is using a text editor, but there are also iOS specific apps for editing JSON such as [Jayson](https://itunes.apple.com/ca/app/jayson/id1447750768?mt=8) if you don't have a Mac or Windows machine to use.
    
    There are two main sections to the JSON file:
    
    * **Locations**
    
        This section lists locations you want to be reminded to buy something at. For example, `"My Grocery Store": "4516  Dundas St, London, ON, N6B 3L5"`. What's key is that the address would be a valid one in an Apple Maps search.
    
    * **Items**

        Here's where you keep your list of things to replenish, complete with a signifying emoji! Each item is linked back to one of the locations you listed above. For example:
        
            "Coffee": {
                "item": "Coffee",
                "location": "My Grocery Store",
                "emoji": "☕️"
            }

    It's as simple as that!
    
2. **Sharing the Item List**

    If you're sharing between multiple household members, place `replenish_items.json` in your iCloud "Shortcuts" folder and share this file with anyone you need to. Ensure others have the file in the same location as you do. This way, when you edit the contents, the changes will be shared with everyone.
    
3. **Download and Configure the Shortcut**

    **_Click [here](Replenish.shortcut) to install_**.
    
    When you run it for the first time, you'll be asked for the following information:
    
    * The location of `replenish_items.json`
    * An optional list of contacts to send a text to each time an item needs to be replenished (don't include yourself in the list)
    * The Reminders list to use

    Anyone else installing this Shortcut will need to go through the same questions.
    
    This Shortcut is best run from the widget and does not require the phone to be unlocked.

## ![](readme_images/cabfarecalculator-icon-small.png) Cab Fare Calculator

### Description
I’m bad at working out quickly how much to tip a cab driver in my head, and just as bad at working how much to ask for in change if I give them the fare in dollar notes.

This Shortcut provides a Today widget to calculate the tip for you, telling you how much to give the driver in $10 increments and how much to ask back for in change.

![](readme_images/cabfarecalculator01.png)

![](readme_images/cabfarecalculator02.png)

### Installation
**_Click [here](Cab%20Fare%20Calculator.shortcut) to install._**

## ![](readme_images/officebucket-icon-small.png) Office Bucket

### Description
This is for when you remember something you need to do at the office, but you're not at the office. Run this Shortcut and it will be added to a Reminders list. Then, you can forget about the task until you arrive at the office. The reminder item is tied to your office location, so you'll get a friendly reminder on arrival at your desk.

### Installation
**_Click [here](Office%20Bucket.shortcut) to install._**

## ![](readme_images/donotdisturb-icon-small.png) Do Not Disturb

### Description
Provides more granular control over Do Not Disturb (DND) from the widget. Whereas Control Center lets you set DND for one hour, this Shortcut will let you activate DND until a specific time.

### Installation
**_Click [here](Do%20Not%20Disturb.shortcut) to install._**

## ![](readme_images/downforeveryone-icon-small.png) Down for Everyone?
### Description
Consults [downforeveryoneorjustme.com](https://downforeveryoneorjustme.com) to tell you the status of the current web page. Call it up from the iOS share sheet in your favourite browser when a website won't load, and it'll tell you if the site is down or not.

### Installation
**_Click [here](Down%20for%20Everyone.shortcut) to install._**

## ![](readme_images/brewtea-icon-small.png) Brew Tea

### Description
Sets a tea timer. Very important. 🇬🇧

On first run, it'll ask you how many minutes you prefer your tea to be brewed, as well as which Reminders list to use. After that, you can launch it from the widget whenever you need it.

### Installation
**_Click [here](Brew%20Tea.shortcut) to install._**

## ![](readme_images/mtlmetrostatus-icon-small.png) Metro Status
### Description
Metro Status provides realtime updates on the status of the Montreal Metro direct from [metroapp.heliomass.com](http://metroapp.heliomass.com) in your Today widget.

![](readme_images/mtlmetrostatus01.png)

![](readme_images/mtlmetrostatus02.png)

### Installation
**_Click [here](Metro%20Status.shortcut) to install._**

## ![](readme_images/bixi-icon-small.png) Bixi
### Description
Locates the nearest Montreal [Bixi](http://bixi.com) dock in your Today Widget, and tells you how many bikes and free docks are available. Optionally, it will also provide walking or cycling directions.

I created this because sometimes you know the area and just want to see at a glance which cross-street the nearest station is at, and whether you could dock your bike there.

![](readme_images/bixi01.png)

![](readme_images/bixi02.png)

This widget is powered by [Bixi Time](http://bixitime.com). You can get the source code for Bixi Time [here](https://github.com/euoia/bixitime-website).

### Installation
**_Click [here](Bixi.shortcut) to install._**

##![](readme_images/search-icon-small.png) Search
### Description
Simply searches Google. Run the shortcut directly to be prompted. Use the shortcut in the Share Sheet with highlighted text to search from anywhere.

### Installation & Dependencies
**_Click [here](Search.shortcut) to install._**

⚠️ **_You will need the [Input Filter](#-input-filter) function installed._**

## ![](readme_images/guessthenumber-icon-small.png) Guess the Number
### Description
A simple game for your Today widget. Try and guess the secret number in under 10 tries!

![](readme_images/guessthenumber01.png)

![](readme_images/guessthenumber02.png)

![](readme_images/guessthenumber03.png)

### Installation
**_Click [here](Guess%20the%20Number.shortcut) to install._**

## ![](readme_images/functions-icon-small.png) Functions
Functions are Shortcuts which get called from other Shortcuts. They provide reusable functionality for common tasks. Some of the main Shortcuts here may have dependencies on these.

### Input Filter
Prompts the user for input if your shortcut's input is empty.

You'd use this if you have a Shortcut which can be used on its own, but also from the Share Sheet. In the former case, you'd want to prompt the user for input. In the latter case, the input would be retrieved via the Share Sheet.

To use, create a dictionary with the following two keys and pass it to the Input Filter workflow:

* `Data` - The Shortcut Input
* `Prompt` - A prompt for the user if Shortcut Input was empty

The user will then be prompted to fill out the missing information in the case the Shortcut Input was empty.

**_Click [here](Filter%20Workflows%20and%20Run.shortcut) to install._**