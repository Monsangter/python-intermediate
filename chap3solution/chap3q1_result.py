#다음 코드의 결과값은 무엇일까.
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

'''
가장먼저 참이 되는 문장인 
shirt가 출력된다
'''