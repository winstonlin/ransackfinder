RansackFinder
=============
Use [Agent Ransack](https://www.mythicsoft.com/agentransack) from within [Sublime Text](http://www.sublimetext.com/).

Works with both Sublime Text 2 and 3.

Installation
------------
For the time being, this plugin can only be installed via github.

Usage
-----

### Setup your path to Agent Ransack.
Setup your path to Agent Ransack ("agent_ransack_path") in your user settings. Point it towards the executable for Agent Ransack.

Here is an example in Windows:
``` js
{
    "agent_ransack_path" : "C:\\Program Files\\Mythicsoft\\Agent Ransack\\AgentRansack.exe"
}
```

### Command: Find In Current Folder
This command will open Agent Ransack, take your currently selected text, and place it in the ``Containing text`` field. It will also take the folder of the currently opened file (in Sublime Text) and put it in the ``Look in`` field.

If no text is currently selected, then it will still open Agent Ransack, but without any ``Containing text``.

### Key Bindings
The default shortcut is ``Ctrl + Shift + q``.

If you would like to customize the key bindings, the command name is ``rs_find_in_current_folder``.
