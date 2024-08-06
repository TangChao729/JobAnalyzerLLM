# To initialize a docker container for the marqo database, you need:

1. Configure the server (at your choice) to run the docker container.
   GPU support is only available on Linux server with a GPU.
   To configure docker with GPU support, follow the instructions at:
   url: https://saturncloud.io/blog/how-to-use-gpu-from-a-docker-container-a-guide-for-data-scientists-and-software-engineers/
   
   steps:
   1) install nvidia drivers
   2) install docker
   3) install nvidia container toolkit
   4) configure docker
   5) add user to docker group

2. Create docker storage volume for the database (optional, if you want to save the data into specific location):
   '''
   docker volume create marqo_data
   '''
   
3. Pull the docker image and run with docker commands:
   '''
   docker run --gpus all --name marqo -p 8882:8882 -v marqo_data:/opt/vespa marqoai/marqo:latest
   '''
   After service running, you should see prompt message indicate service is running.


4. Check container if using GPU:
   '''
   docker ps
   sudo docker exec -it {CONTAINERID} /bin/bash
   nvidia-smi
   '''
   If using GPU, you should see the GPU information.

# To access the database, you need:
1. To access the database, use your choice of SDK
    - Python SDK:
    
    pip install marqo
    '''

2. Sample code
   '''
   import marqo

    mq = marqo.Client(url='{server_location}:8882')

    mq.create_index("my-first-index", model="hf/all_datasets_v4_MiniLM-L6")

    mq.index("my-first-index").add_documents([
        {
            "Title": "The Travels of Marco Polo",
            "Description": "A 13th-century travelogue describing Polo's travels"
        }, 
        {
            "Title": "Extravehicular Mobility Unit (EMU)",
            "Description": "The EMU is a spacesuit that provides environmental protection, "
                        "mobility, life support, and communications for astronauts",
            "_id": "article_591"
        }],
        tensor_fields=["Description"]
    )

    results = mq.index("my-first-index").search(
        q="What is the best outfit to wear on the moon?"
    )
    '''

3. Sample result:
    '''
    {'hits': [{'Title': 'Extravehicular Mobility Unit (EMU)',
   'Description': 'The EMU is a spacesuit that provides environmental protection, mobility, life support, and communications for astronauts',
   '_id': 'article_591',
   '_highlights': [{'Description': 'The EMU is a spacesuit that provides environmental protection, mobility, life support, and communications for astronauts'}],
   '_score': 0.5677878507655333},
  {'Title': 'The Travels of Marco Polo',
   'Description': "A 13th-century travelogue describing Polo's travels",
   '_id': '50ed19d8-212b-48d8-8099-f13c59394ded',
   '_highlights': [{'Description': "A 13th-century travelogue describing Polo's travels"}],
   '_score': 0.5467896410949249}],
 'query': 'What is the best outfit to wear on the moon?',
 'limit': 10,
 'offset': 0,
 'processingTimeMs': 64}
 '''

 