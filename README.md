# CMM-Directory-Script
- This program monitors a specified folder for CMM (Coordinate Measuring Machine) reports and compiles them into a single report for each inspected part. This facilitates easier uploading and file management for quality assurance processes. Originally created for Hexagon TIGO SF.

______
## Summary
1. Monitors a specified folder for the different files created by the CMM for the same part.
2. Once all of the runs are completed for a certain part, consolidates the CMM information for all the files into a single one.
3. Continuously checks every 5 minutes until the program is quit.

## For the main function
1. Enter the Input folder (where the files are stored)
2. Enter the Output folder (where the converted files will be sent)
3. Enter the number of runs/sides for every part
4. The program will execute every 5 minutes. If it finds the correct number of files in the Input folder it will combine them to one file in the Output folder.

** The files must be in **(Part Name)-(Rev #) [SIDE#] Part#000.TXT** format, for example:<br/>
<p align="center">
<i> "28124-REV A [S1] Part#001.TXT" </i> or <i> "2025142-008-REV C [S3] Part#006.TXT"</i>
</p>

<h2>Option functionality </h2> 
Right click the icon in the taskbar to display the options: <br/>
- <i>Pause:</i> Pauses the execution of the program, but continues to store the input folder, output folder, and side number<br/>
- <i>Unpause:</i> Unpauses the execution<br/>
- <i>Restart:</i> Restarts the program if you want to look into different folders / different completed parts<br/>
- <i>Quit:</i> Completely exits the program.<br/>
