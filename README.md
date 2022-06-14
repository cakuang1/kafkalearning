# Mini-Kafka
Created to learn concepts the basic concepts of Apache Kafka. This version will only contain the implementations of topics and brokers. There will also be producer and consumer APIs.


# Data Structures/Concepts

**Messages**
Data in bytes stored in topics

**Topics**
A basic list of messages

**Producers**
Produce messages and pushes them into a chosen topic.

**Consumers**
Consumes messages from topics. Main purpose is to subscribe to a topic and be able to process streamed data from the producer. Consumers themselves are also servers. More into detail below.

**Brokers**
A server that listens to producers and consumers. Helps update topics and deliver messages.

# Simple diagram of how this works

![Untitled presentation (1)](https://user-images.githubusercontent.com/70300980/173268040-379f0faa-fc8b-461c-95ab-a47c7d10f9b0.jpg)







# Quick start


1 . Clone the repository into a directory of your choosing.

Change your directory into the new folder
2 . Start the server by running 'python server.py' to start running your broker.

Now that you have got your server running lets look at a few command line arguments.

3. Start by creating a new topic and adding a message. Open a new terminal change directory into the same folder and call 'python createtopic 








3.









**Using the producer and consumer APIs for creating your own application**



















