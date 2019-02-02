Wouldn't it be better to retrieve Http header information using a Http header constants, like this `request_headers.get(http.REFERER)`. Constants such as `http.REFERER` for the string `Referer` reduces typos, and having to remember the exact spelling for Http headers. 

This library does the following:
1. Refers to the list of headers registered with IANA: https://www.iana.org/assignments/message-headers/message-headers.xhtml . The definitions are available for download, as CSV files. These files are present in the `references` folder. 
1. Generates the headers, under the `headers` package, using the locally available CSV `references` files.
