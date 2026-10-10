
import queue

# Create a Pub/Sub notification system
subscribers = []

# Subscribe function
def subscribe(name):
    q = queue.Queue()
    subscribers.append((name, q))
    print(name, "subscribed successfully")
    return q

# Publisher function
def publish(message):
    print("\nPublisher sent:", message)

    for name, q in subscribers:
        q.put(message)

# Subscriber function
def receive(name, q):
    while not q.empty():
        message = q.get()
        print(name, "received notification:", message)

# Create subscribers
subscriber1 = subscribe("Subscriber 1")
subscriber2 = subscribe("Subscriber 2")

# Publish notification
publish("Low stock alert: Product quantity is below minimum")

# Receive notifications
receive("Subscriber 1", subscriber1)
receive("Subscriber 2", subscriber2)

print("\nPub/Sub notification completed successfully!")

