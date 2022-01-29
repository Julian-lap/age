def try_me(age):
    me = 24
    if age < 0:
        answer = 'You are not born yet or you are cheating, then I guess you cheat'
    elif 0 < age < 24:
        answer = 'You are young'
    elif age > 24:
        answer = 'Hello grandpapa'
    
    return answer

if __name__ == "__main__":
    age = 48
    answer = try_me(age)
    print(answer)
