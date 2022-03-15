# complex_watcher_poc

> Auto-generated documentation index.

Full Complex_watcher project documentation can be found in [Modules](MODULES.md#complex_watcher-modules)

- [complex_watcher_poc](#complex_watcher_poc)
  - [Complex_watcher Modules](MODULES.md#complex_watcher-modules)

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
        queue: test```

## run
execute `complex_watcher`
