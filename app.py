#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################
# Discord BOT
# Title: Discord Bot for statistics of channels
# Author: Vojtěch Petrásek
# Generated: 013/1/2023 16:17:01
##################################################

###
# imports
###

import os
import sys
import time

import discord



if __name__ == '__main__':
    try:
        with open('token') as t:
            token = t.readline()
            print(token)
        t.close()
        bot.run(token)
    except Exception as e:
        print('Exited with error: {}'.format(e))
        sys.exit(1)