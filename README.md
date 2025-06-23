# mitmproxy Reflector
## Description
A lightweight script that mimics the functionality of the [Burp Suite Reflector](https://github.com/elkokc/reflector/tree/master) extension, designed to automatically detect potential **XSS vulnerabilities** by testing user-controlled inputs for reflection.
 
## How to use
```sh
mitmproxy -s ./mitm-reflector.py [aggressive/passive]
```
In aggressive mode, every time when reflection is found, the mitm-reflector will check which of special-symbols are displayed on this page from vulnerable parameters. For this action, mitm-reflector compose additional requests for each reflected parameter.
