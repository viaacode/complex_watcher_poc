# complex_watcher_poc

- config example:
```
viaa:
  logging:
    level: DEBUG
app:
      watcher:
        dest_path: /incoming/dest/
        dest_host: dest_host_ftp 
        dest_user: auser 
        dest_pass: apass         
        source_host: source_host_ftp
        source_path: /incoming/complex/
        source_user: ftpuser
        source_pass: pass 
      amqpPublisher:
        host: mq-host
        user: auser 
        pass: ww         
        queue: test```
