# WOTO-finder

This is a script to find WOTOs in Duke's Comp Sci 201. WOTOs are WOrking TOgether questions, collaborative questions asked during CS201. The professor, Owen Astrachan, opens the WOTO at some point during class, usually about 30-40 minutes in. They're asked in Google Forms, and to get to them, you either have to painstakingly type out the link that's shown in the slides or navigate through several layers of class websites. This can be frustrating because WOTOs are typically only open for 3-5 minutes; there's no time to waste on needless navigation.

This script was written to avoid the odious process of navigating to the WOTO every class. It automatically and intelligently pulls the WOTO link for the day from the class website and regularly checks the link to see if the Google Form is open yet. When the WOTO opens, the script immediately opens the WOTO in a new tab in the default browser. This saves valuable time on the WOTO and automates the process of navigation.

The script is packaged into a standalone executable, which is located in the /build folder.
