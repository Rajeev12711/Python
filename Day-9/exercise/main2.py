travel = [
    {
        "country": "spain",
        "city": ["madrid","lugo", "biscay",],
        "visits": 10
    },
    {
        "county": "japan",
        "city": ["tohoku", "kanto", "kinki",],
        "visits": 5
    },
    ]
def add_new_country(country, city, visits):
    travel_point = {
        "country":country,
        "city": city,
        "visits": visits,
    }
    travel.append(travel_point)

# def add_new_country(country, city, visits):
#     travel_point = {}
#     travel_point["country"]= country
#     travel_point["city"]= city
#     travel_point["visits"]= visits
#     travel.append(travel_point)


add_new_country("Russia", ["moscow", "saint petersburg"], 2,)
print(travel)