➜  cupomhuskybot git:(main) ✗ python bot_telegram.py
Traceback (most recent call last):
  File "/home/h7/Projects/cupomhuskybot/.cupbot/lib/python3.8/site-packages/urllib3/connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "/home/h7/Projects/cupomhuskybot/.cupbot/lib/python3.8/site-packages/urllib3/connectionpool.py", line 449, in _make_request
    six.raise_from(e, None)
  File "<string>", line 3, in raise_from
  File "/home/h7/Projects/cupomhuskybot/.cupbot/lib/python3.8/site-packages/urllib3/connectionpool.py", line 444, in _make_request
    httplib_response = conn.getresponse()
  File "/usr/lib/python3.8/http/client.py", line 1348, in getresponse
    response.begin()
  File "/usr/lib/python3.8/http/client.py", line 316, in begin
    version, status, reason = self._read_status()
  File "/usr/lib/python3.8/http/client.py", line 277, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
  File "/usr/lib/python3.8/socket.py", line 669, in readinto
    return self._sock.recv_into(b)
  File "/usr/lib/python3.8/ssl.py", line 1241, in recv_into
    return self.read(nbytes, buffer)
  File "/usr/lib/python3.8/ssl.py", line 1099, in read
    return self._sslobj.read(len, buffer)
ConnectionResetError: [Errno 104] Connection reset by peer

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/h7/Projects/cupomhuskybot/.cupbot/lib/python3.8/site-packages/requests/adapters.py", line 489, in send
    resp = conn.urlopen(
  File "/home/h7/Projects/cupomhuskybot/.cupbot/lib/python3.8/site-packages/urllib3/connectionpool.py", line 787, in urlopen
    retries = retries.increment(
  File "/home/h7/Projects/cupomhuskybot/.cupbot/lib/python3.8/site-packages/urllib3/util/retry.py", line 550, in increment
    raise six.reraise(type(error), error, _stacktrace)
  File "/home/h7/Projects/cupomhuskybot/.cupbot/lib/python3.8/site-packages/urllib3/packages/six.py", line 769, in reraise
    raise value.with_traceback(tb)
  File "/home/h7/Projects/cupomhuskybot/.cupbot/lib/python3.8/site-packages/urllib3/connectionpool.py", line 703, in urlopen
    httplib_response = self._make_request(
  File "/home/h7/Projects/cupomhuskybot/.cupbot/lib/python3.8/site-packages/urllib3/connectionpool.py", line 449, in _make_request
    six.raise_from(e, None)
  File "<string>", line 3, in raise_from
  File "/home/h7/Projects/cupomhuskybot/.cupbot/lib/python3.8/site-packages/urllib3/connectionpool.py", line 444, in _make_request
    httplib_response = conn.getresponse()
  File "/usr/lib/python3.8/http/client.py", line 1348, in getresponse
    response.begin()
  File "/usr/lib/python3.8/http/client.py", line 316, in begin
    version, status, reason = self._read_status()
  File "/usr/lib/python3.8/http/client.py", line 277, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
  File "/usr/lib/python3.8/socket.py", line 669, in readinto
    return self._sock.recv_into(b)
  File "/usr/lib/python3.8/ssl.py", line 1241, in recv_into
    return self.read(nbytes, buffer)
  File "/usr/lib/python3.8/ssl.py", line 1099, in read
    return self._sslobj.read(len, buffer)
urllib3.exceptions.ProtocolError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "bot_telegram.py", line 47, in <module>
    bot.polling()
  File "/home/h7/Projects/cupomhuskybot/.cupbot/lib/python3.8/site-packages/telebot/__init__.py", line 1047, in polling
    self.__threaded_polling(non_stop=non_stop, interval=interval, timeout=timeout, long_polling_timeout=long_polling_timeout,
  File "/home/h7/Projects/cupomhuskybot/.cupbot/lib/python3.8/site-packages/telebot/__init__.py", line 1122, in __threaded_polling
    raise e
  File "/home/h7/Projects/cupomhuskybot/.cupbot/lib/python3.8/site-packages/telebot/__init__.py", line 1077, in __threaded_polling
    polling_thread.raise_exceptions()
  File "/home/h7/Projects/cupomhuskybot/.cupbot/lib/python3.8/site-packages/telebot/util.py", line 116, in raise_exceptions
    raise self.exception_info
  File "/home/h7/Projects/cupomhuskybot/.cupbot/lib/python3.8/site-packages/telebot/util.py", line 98, in run
    task(*args, **kwargs)
  File "/home/h7/Projects/cupomhuskybot/.cupbot/lib/python3.8/site-packages/telebot/__init__.py", line 653, in __retrieve_updates
    updates = self.get_updates(offset=(self.last_update_id + 1), 
  File "/home/h7/Projects/cupomhuskybot/.cupbot/lib/python3.8/site-packages/telebot/__init__.py", line 627, in get_updates
    json_updates = apihelper.get_updates(self.token, offset, limit, timeout, allowed_updates, long_polling_timeout)
  File "/home/h7/Projects/cupomhuskybot/.cupbot/lib/python3.8/site-packages/telebot/apihelper.py", line 334, in get_updates
    return _make_request(token, method_url, params=payload)
  File "/home/h7/Projects/cupomhuskybot/.cupbot/lib/python3.8/site-packages/telebot/apihelper.py", line 156, in _make_request
    result = _get_req_session().request(
  File "/home/h7/Projects/cupomhuskybot/.cupbot/lib/python3.8/site-packages/requests/sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "/home/h7/Projects/cupomhuskybot/.cupbot/lib/python3.8/site-packages/requests/sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "/home/h7/Projects/cupomhuskybot/.cupbot/lib/python3.8/site-packages/requests/adapters.py", line 547, in send
    raise ConnectionError(err, request=request)
requests.exceptions.ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
