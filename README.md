# HTTP Anarchy

## introduce

This project is a raw TCP server written in Python that bypasses standard HTTP library restrictions. It allows you to send **illegal**, **non-standard**, and **arbitrary** HTTP status codes to web browsers to see how they react.

It also features a "Magic Byte" mode that reads a file's header (e.g., PNG, JPEG) and sends its hex signature as the status code.

##  Why can't define own status code
Standard web servers (Node.js, Nginx, Apache) strictly follow RFC specifications and will throw errors if you try to send a status code like `-200` or `9999`. By using Python's `socket` module, we operate at the TCP layer, constructing raw HTTP response strings manually to break these rules.

## results
you can use the curl command to check results

the normal connect
```c
curl -v http://127.0.0.1:8080/

*   Trying 127.0.0.1:8080...
* Connected to 127.0.0.1 (127.0.0.1) port 8080
> GET / HTTP/1.1
> Host: 127.0.0.1:8080
> User-Agent: curl/8.5.0
> Accept: */*
> 
< HTTP/1.1 200 MagicResponse
< Content-Type: text/html; charset=utf-8
< Content-Length: 69
< Connection: close
< 
* Closing connection
```

---

send the self define code
```c
curl -v http://127.0.0.1:8080/-200

*   Trying 127.0.0.1:8080...
* Connected to 127.0.0.1 (127.0.0.1) port 8080
> GET /-200 HTTP/1.1
> Host: 127.0.0.1:8080
> User-Agent: curl/8.5.0
> Accept: */*
> 
* Unsupported HTTP/1 subversion in response
* Closing connection
curl: (1) Unsupported HTTP/1 subversion in response

```

you can see have -200 status code，of course this is not normal response because this is not officially status code




##  Features
- **Negative Status Codes**: Send `-200` and watch Chrome treat it as success.
- **Huge Integers**: Send `999999` or arbitrary numbers.
- **Strings as Codes**: Send `foo` or any text (Status line injection).
- **Magic Bytes Mode**: Request a local file (e.g., `/image.png`), and the server will extract its **file signature (Magic Bytes)** and use it as the HTTP status code (e.g., `FFD8FFE0...`).

## reference
https://www.youtube.com/watch?v=I7i6fToaNho

