our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

shared_destinations = our_routes.intersection(competitor_routes)
print(shared_destinations)

only_our_destinations = our_routes.difference(competitor_routes)
print(only_our_destinations)

not_shared_destinations = our_routes.symmetric_difference(competitor_routes)
print(not_shared_destinations)