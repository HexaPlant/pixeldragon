# Access Images

Pixeldragon supports the [International Image Interoperability Framework 2.0 API](http://iiif.io/api/image/2.0/) using the scheme:

```bash
http://server/fcgi-bin/iipsrv.fcgi?IIIF=image.tif/{region}/{size}/{rotation}/{quality}.{format}
```

Pixeldragon also support accesing images via Zoomify

```bash
http://server/fcgi-bin/iipsrv.fcgi?Zoomify=image.tif
```

and DeepZoom protocol

```bash
http://server/fcgi-bin/iipsrv.fcgiDeepZoom==image.tif
```

## Examples

### Resize image to 256x256 pixels

```bash
 http://iiif.hexaplant.com/iipsrv/iipsrv.fcgi?IIIF=/e0202a.tif/full/256,256/0/default.jpg
 ```
![](http://iiif.hexaplant.com/iipsrv/iipsrv.fcgi?IIIF=/e0202a.tif/full/256,256/0/default.jpg)

### Resize image to 20%

```bash
http://iiif.hexaplant.com/iipsrv/iipsrv.fcgi?IIIF=/e0202a.tif/full/pct:20/0/default.jpg
 ```
![](http://iiif.hexaplant.com/iipsrv/iipsrv.fcgi?IIIF=/e0202a.tif/full/pct:20/0/default.jpg)


### Crop image by position and resize width to 256px

```bash
http://iiif.hexaplant.com/iipsrv/iipsrv.fcgi?IIIF=/e0202a.tif/125,15,500,500/256,/0/default.jpg
 ```
![](http://iiif.hexaplant.com/iipsrv/iipsrv.fcgi?IIIF=/e0202a.tif/125,15,500,500/256,/0/default.jpg)


### Crop image by percent and resize height to 256px

```bash
http://iiif.hexaplant.com/iipsrv/iipsrv.fcgi?IIIF=/e0202a.tif/pct:50,0,40,70/,256/0/default.jpg
 ```
![](http://iiif.hexaplant.com/iipsrv/iipsrv.fcgi?IIIF=/e0202a.tif/pct:50,0,40,70/,256/0/default.jpg)

### Resize image to 256x256 pixels and rotate by 180%

```bash
http://iiif.hexaplant.com/iipsrv/iipsrv.fcgi?IIIF=/e0202a.tif/full/256,256/180/default.jpg
 ```
![](http://iiif.hexaplant.com/iipsrv/iipsrv.fcgi?IIIF=/e0202a.tif/full/256,256/180/default.jpg)
