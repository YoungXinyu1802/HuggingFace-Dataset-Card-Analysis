The dataset is in the form of a json lines file with 1,20,000 examples, where an example consists of text (extracted from C4 English dataset) and metadata fields (website description extracted from Wikipedia).

Example:
```
{
    "text": "US10289222B2 - Handling of touch events in a browser environment - Google Patents\nHandling of touch events in a browser environment Download PDF\nUS10289222B2\nUS10289222B2 US13/857,848 US201313857848A US10289222B2 US 10289222 B2 US10289222 B2 US 10289222B2 US 201313857848 A US201313857848 A US 201313857848A US 10289222 B2 US10289222 B2 US 10289222B2\nUS13/857,848\nUS20130222244A1 (en\nEli Joshua FIDLER\nMichael Thomas Winkler\nMatthew Nicholaos STAIKOS\nJoseph Charles MASON\n2011-01-05 Priority to US12/985,337 priority Critical patent/US8438473B2/en\n2013-04-05 Application filed by BlackBerry Ltd filed Critical BlackBerry Ltd\n2013-04-05 Priority to US13/857,848 priority patent/US10289222B2/en\n2013-06-26 Assigned to RESEARCH IN MOTION CORPORATION reassignment RESEARCH IN MOTION CORPORATION ASSIGNMENT OF ASSIGNORS INTEREST (SEE DOCUMENT FOR DETAILS). Assignors: Winkler, Michael Thomas\n2013-06-26 Assigned to RESEARCH IN MOTION LIMITED reassignment RESEARCH IN MOTION LIMITED ASSIGNMENT OF ASSIGNORS INTEREST (SEE DOCUMENT FOR DETAILS). Assignors: Fidler, Eli Joshua, Mak, Genevieve Elizabeth, Mason, Joseph Charles, STAIKOS, MATTHEW\n2013-08-29 Publication of US20130222244A1 publication Critical patent/US20130222244A1/en\n2016-03-08 Assigned to RESEARCH IN MOTION LIMITED reassignment RESEARCH IN MOTION LIMITED ASSIGNMENT OF ASSIGNORS INTEREST (SEE DOCUMENT FOR DETAILS). Assignors: RESEARCH IN MOTION CORPORATION\n2019-05-14 Publication of US10289222B2 publication Critical patent/US10289222B2/en\nHandling of touch events in a browser environment is disclosed. An example method includes, while a document is displayed on a touchscreen display of a device, detecting a touch event at the touchscreen display, and selectively processing the detected touch event using one of a default hander, a touch event handler, and a conversion to one or more mouse events, according to a touch event handling property defined for the document.\nThe present application relates generally to the processing of detected user input events in a web browser.\nComputing devices such as desktop computers are typically equipped with external pointing devices, such as a mouse, to permit cursor-based user interaction with content executing on the computer., 
    "metadata": [
        {
            "key": "website_description",
            "type": "global",
            "value": "Google Patents is a search engine from Google that indexes patents and patent applications."
        }
    ]
}
```