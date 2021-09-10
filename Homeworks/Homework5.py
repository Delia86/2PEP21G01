"""
Create a class for an object that can get the latest stable version of python by downloading and looking in the
content of this page: https://en.wikipedia.org/wiki/History_of_Python
To download the page try using the following command for windows
powershell -c "Invoke-WebRequest -Uri 'https://en.wikipedia.org/wiki/History_of_Python' -OutFile 'C:\temp\page.html'"
or curl, wget, or some other tools you may have in case of mac.
Compare the retrieved version with the first 2 digits of your installed version and show a message to the user
with current and available version
"""
import subprocess,re,time,os
from subprocess import Popen,run

class PythonVersion():

    def installed_version(self):
        py1 = Popen(['python','--version'],text=True, stdout=subprocess.PIPE)
        output1 = py1.communicate()[0]
        return output1

    def latest_version(self):
        py2=Popen(["powershell -c Invoke-WebRequest-Url https://en.wikipedia.org/wiki/History_of_Python -OutFile page.html"],text=True,stdout=subprocess.PIPE)
        output2=py2.communicate()
        return output2
        with open("page.html", errors='ignore') as page:
            text = page.read()
            result = re.findall(r"Current\sstable\sversion\:\<\/span\>\s\<b\>(\d\.\d)", text)
        return result[0]

compared_versions = PythonVersion()
print(f"Current Pytohn version: {compared_versions.installed_version()}")
print(f"Latest stable version: {compared_versions.latest_version()}")