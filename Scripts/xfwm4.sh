#!/usr/bin/bash
killall dcompmgr
killall cairo-compmgr
xfconf-query --channel=xfwm4 --property=/general/use_compositing --set=true
