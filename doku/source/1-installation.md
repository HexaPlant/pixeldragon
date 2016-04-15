# Installation
 
 
## Install Docker & Docker Compose

```bash
yum install -y epel-release
yum install -y docker python-pip
pip install docker-compose
```
 
## Create Docker LVM

To improve performance Docker images should be stored in a thin provisioned Logical Volume.

```bash
pvcreate /dev/vdb
vgcreate ivg /dev/vdb
lvcreate --wipesignatures y -n data ivg -l 95%VG
lvcreate --wipesignatures y -n metadata ivg -l 5%VG
```

Modify Docker the storage configuration in */etc/sysconfig/docker-storage* to use the new logical volume.

```bash
DOCKER_STORAGE_OPTIONS="--storage-opt dm.datadev=/dev/ivg/data --storage-opt dm.metadatadev=/dev/ivg/metadata"
```

## Enable & Test Docker Installation

```bash
systemctl start docker && systemctl enable docker &&  systemctl status docker
docker run hello-world
docker info
```
## Remove old Docker images

Remove old Docker images if the already exist on the his

```bash
docker-compose rm -f redis
docker-compose rm -f ids
docker-compose rm -f flower
docker-compose rm -f nginx
docker-compose rm -f iipsrv
```


##  Deploy Docker images

Create data directories.

```bash
mkdir -p /data/ids/tmp
mkdir -p /data/ids/public
mkdir -p /data/redis
mkdir -p /data/log/nginx
mkdir -p /data/log/iipsrv
mkdir -p /data/cache/nginx
```
Clone Repository

```bash
mkdir -p /code
cd /code 
git clone https://github.com/HexaPlant/pixeldragon.git
```
Populate data directory

```bash
cp ./data/* /data/ids/public
```
Build and deploy images

```bash
docker-compose build
docker-compose up -d
```


