def app(environ, start_response):
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])

"""
$ gunicorn -w 4 gunicorn_demo:app
[2017-06-02 15:40:37 -0700] [25242] [INFO] Starting gunicorn 19.7.1
[2017-06-02 15:40:37 -0700] [25242] [INFO] Listening at: http://127.0.0.1:8000 (25242)
[2017-06-02 15:40:37 -0700] [25242] [INFO] Using worker: sync
[2017-06-02 15:40:37 -0700] [25245] [INFO] Booting worker with pid: 25245
[2017-06-02 15:40:37 -0700] [25246] [INFO] Booting worker with pid: 25246
[2017-06-02 15:40:37 -0700] [25247] [INFO] Booting worker with pid: 25247
[2017-06-02 15:40:37 -0700] [25248] [INFO] Booting worker with pid: 25248

In another terminal:
$ http http://127.0.0.1:8000
HTTP/1.1 200 OK
Connection: close
Content-Length: 14
Content-Type: text/plain
Date: Fri, 02 Jun 2017 22:40:53 GMT
Server: gunicorn/19.7.1

Hello, World!
"""
