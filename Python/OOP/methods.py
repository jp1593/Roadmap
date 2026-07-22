class Youtube: 
    def __init__(self, username, subscribers=0, subscriptions=0):
        self.username = username 
        self.subscribers = subscribers
        self.subscriptions = subscriptions

    def subscribe(self, user): 
        user.subscribers += 1
        self.subscriptions += 1


user1 = Youtube("Elextron") 
user2 = Youtube("Popshti")
user1.subscribe(user2)
print("U1 Subscribers:", user1.subscribers)
print("U1 Subscriptions:", user1.subscriptions)   
print("U2 Subscribers:", user2.subscribers)
print("U2 Subscriptions:", user2.subscriptions)