"""
This program was designed to help people learning about the church who are unfamiliar with church lingo and jargon. 
It asks the user for an unfimiliar word and then attempts to define it. 
We created a small dicitonary for this purpose, and also created a program to scrape the church website which has other definitons. 


Reference links: https://wheatandtares.org/2013/10/08/mormon-jargon/, https://www.churchofjesuschrist.org/comeuntochrist/belong/sunday-services/common-church-lingo
"""


word_dict = { 
'comp': 'Short for companion, usually a missionary companion. ',
'mormon': 'The name “Mormon Church” is a nickname others gave to Church members because we believe in the Book of Mormon. The official name of the Church is The Church of Jesus Christ of Latter-day Saints. We use the full name of the Church whenever possible as a reminder that Christ is central to it.' ,
'stake' : 'A stake is also a geographical unit of the Church, made up of several wards and branches, similar to a Catholic diocese. ' ,
'ward' : 'A ward is a local congregation. It’s a group of Church members who live within a specific geographic area. A ward generally consists of a few hundred members and is presided over by a volunteer Church leader called a bishop.',
'branch' : 'Branches are much smaller congregations in areas with fewer Church members.',
'church ball' : 'For all those who didn\'t make their professional careers a reality, church ball promises to provide some unhealthy amounts of competition and contention in sports of all kinds ',
'mutual' : 'A word used to described a weeknight activity for youth, which is usually held on wednesday nights.',
'cultural hall' : 'A basketball court used for cattle-like potluck feedings and shoestring-budget wedding receptions; neither a hall nor particularly cultural',

}
# Revmoves HTML tags from a string. 
def remove_html_tags(text):
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

# Checks for the word in our dictionary - if it doesn't exist, it then checks on the website. 
def is_on_website(user_word):
    import requests
    r = requests.get('https://www.churchofjesuschrist.org/comeuntochrist/belong/sunday-services/common-church-lingo')
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.text, features="html.parser")

    titles = soup.find_all(['h3'])
    paragraphs = soup.find_all(['p'])
    for i in range(len(titles)):
        titles[i] = remove_html_tags(str(titles[i])).lower()
    for i in range(len(paragraphs)):
        paragraphs[i] = remove_html_tags(str(paragraphs[i]))
    if (user_word not in titles) == True:
        return("Sorry, we don't have a definiton for that word yet.")
    else:
        print(f"The definition of '{user_word.capitalize()}' is: \n {paragraphs[titles.index(user_word)+2]}")
        return





# Ask for the user's word. 
def get_input():
    print('\nWelcome to the Church of Jesus Christ of Latter-day Saints slang translator!')
    print()
    takein = input('What slang word would you like to search? ').lower()
    print()
    return takein

def return_definition(user_word):
    if (user_word not in word_dict) == False:
        value = word_dict[f'{user_word}']
        print(f'Word: {user_word.capitalize()} \n\n{value}')
        return
    elif (user_word not in word_dict) == True:
        return is_on_website(user_word)
    else:
        print("idk what happened")
        return

    
def run():
    return return_definition(get_input())

run()
