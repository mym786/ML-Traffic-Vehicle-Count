# # integer
#
# i = 1
# print(i)
# # float
# i = 123.5
# print(i)
# # string
# i = "Hello World"
# print(i)
#
#
# ######
#
# x = 2
# i > x
#
# ###
# sum = 0
# for i in [1,2,3,4,5,6,7,8,9,10]:
#     sum = sum + i
#
# print(sum)
#
#
# ######
#
# def sum(x,y):
#     return x+y
# def average(x,y):
#     return (x+y)/2
# def power(x,y):
#     return x**y
#
#
# #####
#
# class person:
#     count=0
#     def __init__(self):
#         self.name="unknown"
#         self.age=0
#     def displayInfo(self):
#         print(self.name, self.age)
#
# p = person()


# #####
# import cv2
# import numpy as np
#
# cap = cv2.VideoCapture("input.mp4")
#
# _, first_frame = cap.read()
# first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
# first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)
# cv2.imshow("First frame", first_gray)
#
# _, frame = cap.read()
# for i in range(1000):
#     _, frame = cap.read()
# gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
#
# difference = cv2.absdiff(first_gray, gray_frame)
# _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)
#
# cv2.imshow("Frame", frame)
# cv2.imshow("difference", difference)
# while True:
#     key = cv2.waitKey(33)
#     if key == 27:
#         break


import cv2
import numpy as np

cap = cv2.VideoCapture("input.mp4")

_, first_frame = cap.read()
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)

while True:
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

    difference = cv2.absdiff(first_gray, gray_frame)
    _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)

    cv2.imshow("First frame", first_frame)
    cv2.imshow("Frame", frame)
    cv2.imshow("difference", difference)

    key = cv2.waitKey(30)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()