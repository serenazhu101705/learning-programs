#To split a list into multiple lists, use:
def extractDigits(lst): 
    res = [] 
    for i in lst: 
        sub = i.split(', ') 
        res.append(sub) 
      
    return(res)

lst = ['alice', 'bob', 'cara'] 
print(extractDigits(lst))

Sum of a range of numbers
y=0

for i in range(1,101):
    y=y+i
  

print(str(y))

 Replace multiple characters at once 
 Using nested replace() 

# initializing string 
test_str = "abbabba"

# printing original string 

to shuffle a string, use ''.join(random.sample(x,len(x)))
print("The original string is : " + str(test_str)) 

# Using nested replace() 
# Replace multiple characters at once 
res = test_str.replace('a', '%temp%').replace('b', 'a').replace('%temp%', 'b') 

# printing result 
print("The string after replacement of positions : " + res)


#To search on Google using webbrowser
import webbrowser

#To change the search, change 'my+name+is+serena' on both ends
url = 'https://www.google.com/search?q=my+name+is+serena&oq=my+name+is+serena&aqs=chrome.0.0l3.2802j0j4&sourceid=chrome&ie=UTF-8'
#images
url = 'https://www.google.com/search?q=hello+world&safe=strict&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj-8K2VjpvqAhWVcc0KHQn1CsUQ_AUoAXoECB4QAw&biw=1038&bih=576'
webbrowser.open(url)
