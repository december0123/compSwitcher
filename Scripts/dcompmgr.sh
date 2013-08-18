#!/usr/bin/bash
xfconf-query --channel=xfwm4 --property=/general/use_compositing --set=false
killall cairo-compmgr
killall dcompmgr #in case different instance is running
dcompmgr --gl > /dev/null &
