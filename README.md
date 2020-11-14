# spectra_comparator  
Spectra comparator with matplotlib and tkinter GUI  

Parses tab separated txt files in the given directory and lets you graph the spectra you want together.  
Some plot configuration is allowed in GUI, but you can easily change things in comparator.py file.  

The names in the legend by default will be numeric but if you place a file named "nombres.txt" in the same folder or one up the data folder, it will use those names to label the data.  
<br/>
## How to run it  
You can run in it in you terminal by calling `python comp_tk.py` while you are in the same directory.  
You could make a batch file (or bash script in Mac/Linux) to run it with double click, I'm leaving a batch file example for you to edit.  
<br/>
### Considerations  
You need the python libraries matplotlib and pandas  
<br/>
Example  
![](example.png)
