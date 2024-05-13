# question 19  
# Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article 
# on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
# The article is long, so it is split up between 4 pages. Your task is to print out the text to 
# the screen so that you can read the full article without having to click any buttons.

# answer

# import requests
# from bs4 import BeautifulSoup

# def print_to_text(base_url):
#     r = requests.get(base_url)
#     soup = BeautifulSoup(r.text)
#     with open("work less.txt", "w") as textfile:
#         for paragraph in soup.find_all(dir="ltr"):
#             textfile.write(paragraph.text.replace("<span>",""))

# if __name__ == "__main__":
#     base_url = "http://www.theatlantic.com/business/archive/2014/08/to-work-better-work-less/375763/"
#     base_url2 = "http://www.theatlantic.com/business/archive/2014/08/to-work-better-work-less/375763/2/"
#     print_to_text(base_url)
#     print_to_text(base_url2)



# question 20
# Write a function that takes an ordered list of numbers (a list where the elements are in order from 
# smallest to largest) and another number. The function decides whether or not the given number is inside 
# the list and returns (then prints) an appropriate boolean.
# Extras:
# Use binary search.

# answer

# import random;

# def basic_approach(list,find):
#     for i in range(0,len(list)):
#         if list[i] == find:
#             return True;
#     return False;

# # def binary_search(list,find):
# #     low,high,mid=0,len(list)-1,(low +high)//2;
# #     while find != list[low] or list[mid] or list[high]:
# #         if find < list[mid] :
# #             high = mid;
# #         else :
# #             low =mid;
# #         mid =(low+high)//2;
# #         if mid == low or high:
# #             return False;
# #     return True;

# def binary_search(list, find):
#     low, high = 0, len(list) - 1
#     while low <= high:  # Continue until low and high cross
#         mid = (low + high) // 2
#         if list[mid] == find:
#             return True  # Element found
#         elif find < list[mid]:
#             high = mid - 1  # Search in the lower half
#         else:
#             low = mid + 1  # Search in the upper half
#     return False  # Element not found
    
# if __name__=='__main__':
#     list=random.sample(range(1,30),15);
#     list.sort(reverse=False);
#     print(list)
#     find=int(input("What number do you want to search here ??"));
#     # result=basic_approach(list,find);
#     result=binary_search(list,find);
#     print(result);



# question 22


# answer

# import requests;

# url='https://www.practicepython.org/assets/nameslist.txt';
# r=requests.get(url);

# with open('nameslist.txt','w') as f:
# 	f.write(r.text)

# counter_dict = {}

# with open('nameslist.txt') as f:
# 	line = f.readline()
# 	while line:
# 		line = line.strip()
# 		if line in counter_dict:
# 			counter_dict[line] += 1
# 		else:
# 			counter_dict[line] = 1
# 		line = f.readline()

# print(counter_dict)



# question 23

# answer 

import requests;

url1='https://www.practicepython.org/assets/primenumbers.txt';
url2='https://www.practicepython.org/assets/happynumbers.txt';

