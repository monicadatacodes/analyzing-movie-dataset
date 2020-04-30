# --------------
from csv import reader


def explore_data(dataset, start, end, rows_and_columns=False):
    """Explore the elements of a list.
    
    Print the elements of a list starting from the index 'start'(included) upto the index 'end'         (excluded).
    
    Keyword arguments:
    dataset -- list of which we want to see the elements
    start -- index of the first element we want to see, this is included
    end -- index of the stopping element, this is excluded 
    rows_and_columns -- this parameter is optional while calling the function. It takes binary          values, either True or False. If true, print the dimension of the list, else dont.
    """
#    i,length=0,0
#    m_list=[]
#    while (i<=end+1):
#        if rows_and_columns == False:
#            m_list = m_list + movies[i]  
#            print(m_list)
#        else :
#            m_list = m_list + movies[i] 
#            length = len(m_list)
#            print(m_list)
#            print('\nlength is ', length)
#        i+=1
    dataset_i = dataset[start:end]
    for i in dataset_i:
        print(i)
        print('\n')

    if rows_and_columns:
        print('Number of rows:',len(dataset))
        print('Number of coloumns:',len(dataset[0]))    
     


def duplicate_and_unique_movies(dataset, index_):
    """Check the duplicate and unique entries.
    
    We have nested list. This function checks if the rows in the list is unique or duplicated based     on the element at index 'index_'.
    It prints the Number of duplicate entries, along with some examples of duplicated entry.
    
    Keyword arguments:
    dataset -- two dimensional list which we want to explore
    index_ -- column index at which the element in each row would be checked for duplicacy 
    
    """
#    for i in range(len(dataset)):
#        count = 0
#        for j in range(len(index)):
#            if(dataset[i][j] == index[j][i]):
#                count +=1
#                print(dataset[i][j] +' is equal to' , index[j][i])
#                print(count)

    duplicate = []
    unique = []

    for movie in dataset:
        name = movie[index_]
        if name in unique:
            duplicate.append(name)
        else :  
            unique.append(name)  

    print('Number of duplicate Movies:',len(duplicate))
    print('\n')
    print('Some of them are:',duplicate[:10])       


def movies_lang(dataset, index_, lang_):
    """Extract the movies of a particular language.
    
    Of all the movies available in all languages, this function extracts all the movies in a            particular laguage.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.

    Keyword arguments:
    dataset -- list containing the details of the movie
    index_ -- index which is to be compared for langauges
    lang_ -- desired language for which we want to filter out the movies
    
    Returns:
    movies_ -- list with details of the movies in selected language
    
    """
    movies_ = []
    for movie in dataset:
        language = movie[index_]
        if language == lang_ :
                movies_.append(movie)
                 
    print( "Examples of some movies\n")
    explore_data(movies_,0,3,True)    
    return movies_
    



def rate_bucket(dataset, rate_low, rate_high):
    """Extract the movies within the specified ratings.
    
    This function extracts all the movies that has rating between rate_low and high_rate.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.
    
    Keyword arguments:
    dataset -- list containing the details of the movie
    rate_low -- lower range of rating
    rate_high -- higher range of rating
    
    Returns:
    rated_movies -- list of the details of the movies with required ratings
    """
    rated_movies = []
    
    for movie in dataset:
      ratings = float(movie[-4])
      if ((ratings>=rate_low) and (ratings<=rate_high)):
            rated_movies.append(movie)  

    print("Some of the highest Rated movies are \n")
    explore_data(rated_movies,0,3,True)
    return rated_movies




# Read the data file and store it as a list 'movies'
opened_file = open(path, encoding="utf8")
read_file = reader(opened_file)
movies = list(read_file)



# The first row is header. Extract and store it in 'movies_header'.
movies_header = movies[0]
print(movies_header)

# Subset the movies dataset such that the header is removed from the list and store it back in movies
movies = movies[1:]



# Delete wrong data
del movies[4552]
# Explore the row #4553. You will see that as apart from the id, description, status and title, no other information is available.
# Hence drop this row.



# Using explore_data() with appropriate parameters, view the details of the first 5 movies.
explore_data(movies,0,5,True)





# Our dataset might have more than one entry for a movie. Call duplicate_and_unique_movies() with index of the name to check the same.
duplicate_and_unique_movies(movies,-2)



# We saw that there are 3 movies for which the there are multiple entries. 
# Create a dictionary, 'reviews_max' that will have the name of the movie as key, and the maximum number of reviews as values.
reviews_max = {}

for movie in movies:
    mov_name = movie[-2]
    reviews = movie[-3]


    if mov_name in reviews_max and reviews_max[mov_name]<reviews:
        reviews_max[mov_name] = reviews
    elif mov_name not in reviews_max :   
        reviews_max[mov_name] = reviews
print(len(reviews_max))    

# Create a list 'movies_clean', which will filter out the duplicate movies and contain the rows with maximum number of reviews for duplicate movies, as stored in 'review_max'. 
movies_clean = []
movies_exist = []

for movie in movies:
    mov_name = movie[-2]
    reviews = movie[-3]
    if(reviews_max[mov_name]==reviews) and (mov_name not in movies_exist):
        movies_clean.append(movie)
        movies_exist.append(mov_name)     
print(" movies wihout duplicates : ",len(movies_clean))        


# Calling movies_lang(), extract all the english movies and store it in movies_en.
movies_en = movies_lang(movies_clean,3,'en')



# Call the rate_bucket function to see the movies with rating higher than 8.
high_rated_movies = rate_bucket(movies_en, 8, 10)


