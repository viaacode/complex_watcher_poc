#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 12:05:56 2022
Kind:

    - watchfolder for complex

Discription:
    - Daemon inotify watchfolder
    - Create a msg for fxp when a .complex file is closed on dir
Target:
    - meemoo fxp rabbit consumer : https://github.com/viaacode/fxp_service.git
@author: tina
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from string import Template
import inotify
import inotify.adapters
from publisher import PubMsg
from viaa.observability import logging
from viaa.configuration import ConfigParser
config = ConfigParser()
logger =  logging.get_logger('watcher', config)
dest_host = config.app_cfg['watcher']['dest_host']
dest_user = config.app_cfg['watcher']['dest_user']
dest_pass = config.app_cfg['watcher']['dest_pass']
source_host = config.app_cfg['watcher']['source_host']
source_user = config.app_cfg['watcher']['source_user']
source_pass = config.app_cfg['watcher']['source_pass']
dest_path = config.app_cfg['watcher']['dest_path']
dirname = config.app_cfg['watcher']['source_path']
pub_user = config.app_cfg['amqpPublisher']['user']
pub_pass = config.app_cfg['amqpPublisher']['pass']
pub_host = config.app_cfg['amqpPublisher']['host']
pub_queue = config.app_cfg['amqpPublisher']['queue']
fxpTemplate = Template("""
                         {
                               "destination_file": "$Filename",
                               "destination_host": "$Dhost",
                               "destination_password": "$Dpass",
                               "destination_path": "$Dpath,
                               "destination_user": "$Duser",
                               "source_file": "$Sfile",
                               "source_host": "$Shost",
                               "source_password": "$Spass",
                               "source_path": "$Spath",
                               "source_user": "$Suser",
                               "move": false
                             }
                         """)

def __main__():
    """Watch a dir in dirname = config.app_cfg['watcher']['source_path']:

            - If file is closed send a fxp msg with the publisher.py

    """
    i = inotify.adapters.Inotify()
    i.add_watch((dirname))
    logger.info('Watching dir : {}'.format(dirname))
    try:
        for event in i.event_gen():
            if event is not None:
                (header, type_names, watch_path, filename) = event
                logger.debug(str(type_names) +',' + str(filename))
                if type_names == ['IN_CLOSE_WRITE']:
                    msg = fxpTemplate.substitute(Filename=filename,
                                                Dhost=dest_host,
                                                Dpass=dest_pass,
                                                Dpath=dest_path,
                                                Duser=dest_user,
                                                Sfile=filename,
                                                Shost=source_host,
                                                Spass=source_pass,
                                                Spath=dirname,
                                                Suser=source_user
                                                )

                    filepath = watch_path + '/' + filename
                    ext=os.path.splitext(filepath)[1]
                    if ext == '.complex' or ext == '.COMPLEX':
                        logger.info("Publish msg for file: {}".format(
                            filename))
                        PubMsg(queue=pub_queue,
                               rabhost=pub_host,
                               user=pub_user,
                               passwd=pub_pass,
                               msg=msg)()
    finally:
        # remove the watch on the folders
        i.remove_watch=dirname
        logger.info('Removing watch on dir : {}'.format(dirname))


if __name__ == '__main__':
    __main__()

