# HTTP Anarchy

## introduce

This project is a raw TCP server written in Python that bypasses standard HTTP library restrictions. It allows you to send **illegal**, **non-standard**, and **arbitrary** HTTP status codes to web browsers to see how they react.

It also features a "Magic Byte" mode that reads a file's header (e.g., PNG, JPEG) and sends its hex signature as the status code.

##  Why can't define own status code
Standard web servers (Node.js, Nginx, Apache) strictly follow RFC specifications and will throw errors if you try to send a status code like `-200` or `9999`. By using Python's `socket` module, we operate at the TCP layer, constructing raw HTTP response strings manually to break these rules.

##  Features
- **Negative Status Codes**: Send `-200` and watch Chrome treat it as success.
- **Huge Integers**: Send `999999` or arbitrary numbers.
- **Strings as Codes**: Send `foo` or any text (Status line injection).
- **Magic Bytes Mode**: Request a local file (e.g., `/image.png`), and the server will extract its **file signature (Magic Bytes)** and use it as the HTTP status code (e.g., `FFD8FFE0...`).

## Usage
1. execute the program 
```
python3 main.py
```
2. open any web browser to input，like edge chrome firefox ...

3. input the server ip and port in the search bar
<img width="279" height="30" alt="image" src="https://github.com/user-attachments/assets/578a7ae1-719f-4b64-85a6-6edba0dd1c7d" />

4. input you want to input the self status code after the server ip and port
<img width="157" height="27" alt="image" src="https://github.com/user-attachments/assets/deaa3e90-e064-4d99-b73b-3c9cf481cc10" />


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

### curl negative number 
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

### curl big number 
```c
curl -v http://127.0.0.1:8080/999999 
*   Trying 127.0.0.1:8080...
* Connected to 127.0.0.1 (127.0.0.1) port 8080
> GET /999999 HTTP/1.1
> Host: 127.0.0.1:8080
> User-Agent: curl/8.5.0
> Accept: */*
> 
* Unsupported HTTP/1 subversion in response
* Closing connection
curl: (1) Unsupported HTTP/1 subversion in response
```
### curl string status code
```c
curl -v http://127.0.0.1:8080/foo
*   Trying 127.0.0.1:8080...
* Connected to 127.0.0.1 (127.0.0.1) port 8080
> GET /foo HTTP/1.1
> Host: 127.0.0.1:8080
> User-Agent: curl/8.5.0
> Accept: */*
> 
* Unsupported HTTP/1 subversion in response
* Closing connection
curl: (1) Unsupported HTTP/1 subversion in response
```

### curl image header status code
```c
curl -v http://127.0.0.1:8080/r.png
*   Trying 127.0.0.1:8080...
* Connected to 127.0.0.1 (127.0.0.1) port 8080
> GET /r.png HTTP/1.1
> Host: 127.0.0.1:8080
> User-Agent: curl/8.5.0
> Accept: */*
> 
* Unsupported HTTP/1 subversion in response
* Closing connection
curl: (1) Unsupported HTTP/1 subversion in response
```


##  web browser with -200 status code 

### edge
<img width="1920" height="927" alt="image" src="https://github.com/user-attachments/assets/036bce33-78d3-49d1-a782-53b4fd89a32a" />

### chrome
<img width="1920" height="918" alt="image" src="https://github.com/user-attachments/assets/362422a0-b6ca-4f92-aa4f-dfcec43dc4f8" />

### brave
<img width="1915" height="1042" alt="image" src="https://github.com/user-attachments/assets/bc898185-e97b-4b3d-a469-e713e11ee729" />

### firefox
<img width="1909" height="1040" alt="image" src="https://github.com/user-attachments/assets/41144ed9-129b-4972-9582-dd6a8c01e715" />

## web browser with big number status code 

### edge
<img width="1919" height="927" alt="image" src="https://github.com/user-attachments/assets/b3423ce2-70a1-4088-bd39-c625899218f5" />

### chrome
<img width="1920" height="869" alt="image" src="https://github.com/user-attachments/assets/4a5b41f8-f80a-406b-9a36-9363a2a44e26" />


### brave
<img width="1920" height="927" alt="image" src="https://github.com/user-attachments/assets/f57f98cd-3b80-4df4-9b6a-cf76fa885e11" />

### firefox
<img width="1870" height="929" alt="image" src="https://github.com/user-attachments/assets/aecc4429-a92a-490f-bcfa-a99c7f9de662" />

## web browser with string status code 

### edge
<img width="1920" height="924" alt="image" src="https://github.com/user-attachments/assets/df2b7714-eb46-44f8-9aa1-54ed94908a39" />

### chrome
<img width="1920" height="863" alt="image" src="https://github.com/user-attachments/assets/853a38fe-a7ca-4e01-b25c-2ad26155551f" />

### brave
<img width="1920" height="923" alt="image" src="https://github.com/user-attachments/assets/1fd12e2e-aa46-4d7d-b0a9-2146c1ab03b4" />

### firefox
<img width="1870" height="927" alt="image" src="https://github.com/user-attachments/assets/d30bcb7c-3294-4e1f-b000-6955c52f1d18" />

## web browser with image header status code 

### edge
<img width="1918" height="924" alt="image" src="https://github.com/user-attachments/assets/b213b8b7-283c-47e3-b8db-165c350df8e8" />

### chrome
<img width="1920" height="866" alt="image" src="https://github.com/user-attachments/assets/7ca27f4a-fae6-4c6c-afdd-07c62e51ef53" />

### brave
<img width="1920" height="923" alt="image" src="https://github.com/user-attachments/assets/4af0bf49-e06c-45b0-ba95-ca09094ab6b1" />

### firefox
<img width="1868" height="930" alt="image" src="https://github.com/user-attachments/assets/14dfb0a5-431b-4cae-8ef6-d358c164ba98" />



## reference
https://www.youtube.com/watch?v=I7i6fToaNho
https://developer.mozilla.org/zh-TW/docs/Web/HTTP/Reference/Status
