from selenium import webdriver

browser = webdriver.Firefox()

# Go to browser to check out app home page
browser.get('http://localhost:8000')

# Page title and header mention to-do lists
assert 'To-do' in browser.title

# User is invited to enter a to-do task straight away

# User types in "Buy Peacock feathers"

# When user hits enter, the page updates, and now the page lists:
# "1: Buy Peacock feathers" as an item on a to-do list

# There is still a text box inviting the user to add another item. She
# enters "Use peacock feathers to make a fly"

# The page updates again, and now shows both items on her list


# User wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# She visits that URL - her to-do list is still there.

# Satisfied, she goes back to sleep

browser.quit()
