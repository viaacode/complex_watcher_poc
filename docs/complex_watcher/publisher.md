# Publisher

> Auto-generated documentation for [complex_watcher.publisher](../../complex_watcher/publisher.py) module.

Created on Tue Mar 15 13:21:11 2022

- [Complex_watcher](../README.md#complex_watcher_poc) / [Modules](../MODULES.md#complex_watcher-modules) / [Complex Watcher](index.md#complex-watcher) / Publisher
    - [PubMsg](#pubmsg)

- Usage:

msg=json.dumps({'test':'result'})
o = pubMsg(queue='test',rabhost='host.com',
       user='UUUUU',
       passwd='XXXXXX',
       msg=msg)
print(o())

@author: tina

## PubMsg

[[find in source code]](../../complex_watcher/publisher.py#L27)

```python
class PubMsg():
    def __init__(
        queue,
        rabhost,
        user,
        passwd,
        msg,
        routing_key='complex_fxp',
        vhost='/',
    ):
```

Publish a message to a queue with exchange and routing key
