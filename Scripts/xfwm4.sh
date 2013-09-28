#!/usr/bin/bash
killall dcompmgr
killall cairo-compmgr
xfconf-query --channel=xfwm4 --property=/general/use_compositing --set=false
sleep 0.1
xfconf-query --channel=xfwm4 --property=/general/use_compositing --set=true
