# File_Rename_Automation
Renames all files in a folder

When you run the program you will first be asked for the name of the file, keep in mind it has to be a valid file name or the code will ask you again for another file name.

Your file explorer will then pop up, please select the folder where you want to change the file names.

All files will keep the corrrect extension they already have so it's fine to mix what types of files you have in the folder (Images, .mp4, .mp3)

Option 1 allows you to rename all files that have a number in them, but skips any files without a number, for example "Vid - 1" ---> "Park_Trip - 1" while a file named "Superman Thumbnail" will not be touched.

Option 2 does the same as 1, but this time changes the files without a number, for example "Random Vid" ---> "Random Vid [Current date and time]"

option 3 simply renames all the files to a name of your choosing and increments the file by 1, for example if you chose to name the file "Hero" the files will be "Hero - 1" then "Hero - 2 and so on"
The reason this option renames all files to the current date and time before changing the name to what you actually want is to prevent duplication errors in a case where you may already have an existing file with the name you want.

Option 4 quits the application.
