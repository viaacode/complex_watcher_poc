# complex_watcher_poc

## install
- python setup.py install

## config 
- create a config.yml file 

- config.yml example:
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
        queue: test
```

## run
execute `complex_watcher`
