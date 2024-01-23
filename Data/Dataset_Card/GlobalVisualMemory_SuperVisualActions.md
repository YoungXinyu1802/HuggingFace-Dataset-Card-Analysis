# SuperVisual Actions

SuperVisual actions dataset is collected using tab recording feature in Chrome & Edge browsers.
Each .supervisual file is a zip archive containing a SuperVisual session. 
The session demonstrates action being completed corresponding to a prompt.

### **Each SuperVisual session contains**

- Prompt describing the task being performed
- Video blobs in H264 codec inside a WebM container + Tab audio when available 
- Mouse clicks and Keypress actions along with metadata such key code, click type/location, target div and url
- Highlight image / screenshot of the contents along with OCR text and metadata

### **Loading dataset**

We provide convert.py that loads .supervisual.zip files and stores results in parquet format. 

### **Visualizing SuperVisual Sessions**

SuperVisual Sessions can be visualized by importing the .supervisual file into https://watcher.supervisual.app.    

<img src="https://raw.githubusercontent.com/SuperVisualApp/Bookmarklets/main/example.png" width="50%">

### **Bookmarklet used to collect DOM events and metadata**

The bookmarklet code is available in on [Github](https://github.com/SuperVisualApp/Bookmarklets ) for review.  
We welcome any suggestions that you might have to improve its features and robustness.   
You can learn more about how tab sharing + bookmarklet are used to provide a [secure experience](https://supervisual.app/security/).

More information is available at https://www.supervisual.app

### Citations
Coming soon!
By Global Visual Memory inc.

---
license: cc-by-4.0
