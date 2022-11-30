# Federated Learning using Keras and PyGAD

Training a Keras model using the genetic algorithm ([PyGAD](https://pygad.readthedocs.io)) using federated learning of multiple clients.


# Project Files

The project has the following files:

- `server.py`: The server Kivy app. It creates a Keras model that is trained on the clients' devices using FL with PyGAD.
- `client1.py`: The client Kivy app which trains the Keras model sent by the server 
- `client2.py`: Another client Kivy app that trains the server's Keras model 


# Running the Project

Start the project by running the [`server.py`](https://github.com/ahmedfgad/FederatedLearning/blob/master/KerasFederated/server.py) file. The GUI of the server Kivy app is shown below. Follow these steps to make sure the server is running and listening for connections.

* Click on the **Create Socket** button to create a socket. 

* Enter the IPv4 address and port number of the server's socket. `localhost` is used if both the server and the clients are running on the same machine. This is just for testing purposes. Practically, they run on different machines. Thus, the user need to specify the IPv4 address (e.g. 192.168.1.4).
* Click on the **Bind Socket** button to bind the create socket to the entered IPv4 address and port number.
* Click on the **Listen to Connections** button to start listening and accepting incoming connections. Each connected device receives the current model to be trained by its local data. Once the model is trained, then no more models will be sent to the connected devices.

After running the server, next is to run one or more clients. The project creates 2 clients but you can add more. The only expected change among the different clients is the data being used for training the model sent by the server.

Just run any client and a GUI will appear like that. You can either run the client at a desktop or a mobile device.

Follow these steps to run the client:

* Click on the **Create Socket** button to create a socket. 

* Enter the IPv4 address and port number of the server's socket. If both the client and the server are running on the same machine, just use `localhost` for the IPv4 address. Otherwise, specify the IPv4 address (e.g. 192.168.1.4).s
* Click on the **Connect to Server** button to create a TCP connection with the server.
* Click on the **Receive & Train Model** button to ask the server to send its current ML model. The model will be trained by the client's local private data. The updated model will be sent back to the server. Once the model is trained, the message **Model is Trained** will appear.


