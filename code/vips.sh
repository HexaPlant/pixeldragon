#!/bin/bash
 
vips im_vips2tiff --vips-progress --vips-concurrency=4  /data/tmp/e0202a /data/public/e0202a.tif:deflate,tile:256x256,pyramid
