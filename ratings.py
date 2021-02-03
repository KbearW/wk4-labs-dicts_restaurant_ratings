"""Restaurant rating lister."""


def restaurant_ratings():
    '''Return data in dict format {restaurant-name, scores}.'''
# Reads the ratings in from the file
    scores_txt = open('scores.txt')
# create an empty dict
    scores = {}
    # iterate over each line in the src file
    for item in scores_txt:
        # rstip out the last character within each line
        item = item.rstrip()
        # unpacking item in the list (list = newly created by using the split function)
        restaurant, score = item.split(':')
        # assign the value to the empty dict and make the score as int (for calculation use later)
        scores[restaurant] = int(score)
    # print(scores)
    return scores

def add_restaurant(scores):
    '''Add a restaurant and rating.'''
    print("Please add a rating for your favorite restaurant!")
    restaurant = input("Restaurant name> ")
    rating = int(input("Rating> "))

    scores[restaurant] = rating
    
# And finally, spits out the ratings in alphabetical order by restaurant

def print_sorted_scores(scores):
    '''Print restaurants and ratings, sorted.'''

    for restaurant, rating in sorted(scores.items()):
        print(f"{restaurant} is rated at {rating}.")    

scores = restaurant_ratings()
add_restaurant(scores)
print_sorted_scores(scores)