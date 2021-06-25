import os
import subprocess

HTML_STR = """
<video controls>
  <source src='{0}' type="video/ogg">
Your browser does not support the video tag.
</video>
"""

if __name__ == '__main__':
    folders = ['.']
    for folder in folders:
        files = os.listdir(folder)
        thisFiles = {}
        for f in files:
            f = "%s/%s"%(folder, f)
            parts = os.path.splitext(f)
            if parts[-1] == '.avi':
                thisFiles[os.path.getmtime(f)] = f
    
        for key in sorted(thisFiles):
            f = thisFiles[key]
            parts = os.path.splitext(f)
            fnew = "%s.ogg"%parts[0]
            subprocess.call(["avconv", "-i", f, "-b", "30000k", fnew])
            print str.format(HTML_STR, fnew)
    

