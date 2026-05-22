dictionary = {
    "name": "7D 건조 망고",
    "type" : "당절임",
    "ingredient": ["망고", "설탕"],
    "origin" : "필리핀"
}

key = input("> 접근하고자 하는 키 : ")

if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키입니다.")


