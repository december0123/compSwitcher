#!/usr/bin/bash
xfconf-query --channel=xfwm4 --property=/general/use_compositing --set=false
killall dcompmgr
cairo-compmgr &
