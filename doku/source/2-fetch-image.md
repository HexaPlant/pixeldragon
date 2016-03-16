# Process Images

## Create image definition

Each image is defined by a json file defining the URL and the internal identifier of an image.

fetch_wikipedia.json

```bash
{
    "args": ["https://upload.wikimedia.org/wikipedia/commons/8/8d/Small_bodies_of_the_Solar_System.jpg", "Small_bodies_of_the_Solar_System"]
}
```

If necessary the json file can include the necessary user credential.

fetch_with_auth.json

 ```bash
{
    "args": ["https://USER:PWD@fedora.phaidra-sandbox.univie.ac.at/fedora/get/o:99045/bdef:Content/download", "99045"]
}
```

##  Fetch image

Once defined the the image definitions can be passed to the fetch_image task. Which will fetch and process the image to be distributed by the Internet Image Protocol Server

```bash
HOSTNAME=labrat03.phaidra.org
curl -H "Content-Type: application/json" --data @fetch_wikipedia.json http://$HOSTNAME/api/task/send-task/tasks.fetch_image
curl -H "Content-Type: application/json" --data @fetch_with_auth.json http://$HOSTNAME/api/task/send-task/tasks.fetch_image
```

