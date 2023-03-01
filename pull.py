import urllib.request
import html2text

with urllib.request.urlopen("https://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html") as response:
    html = response.read()

myFile = open("droptables.txt", "w")
myFile.write(html2text.html2text(str(html)))
print("success!")
