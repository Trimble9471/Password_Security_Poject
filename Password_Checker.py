#Import Regular Expressions Module
#Searches for paterns within strings; letters, digits, special characters.
import re

#Define the function that checks the input password against parameters.
#Create score system for each parameter to associate with strength
def password_strength(password):
    score = 0
    recommendations = []

    #Parameter 1: Check to see if password is >= 8
    if len(password) >= 8:
        score += 1
    else:
        recommendations.append("Use atleast 8 characters.")

    #Parameter 2: Searches password for atleast 1 uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        recommendations.append("Use atleast 1 uppercase letter.")

    #Parameter 3: Searches password for atleast 1 lowercase letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        recommendations.append("Use atleast 1 lowercase letter.")

    #Parameter 4: Searches password for atleast 1 digit/number
    if re.search(r"\d", password):
        score += 1
    else:
        recommendations.append("Use atleast 1 number.")

    #Parameter 5: Searches password for atleast 1 special character
    if re.search(r"[!@#$%^&*(),./\":{}|<>]", password):
        score += 1
    else:
        recommendations.append("Use atleast 1 special character.")

    #Define strength level based on score
    #\u is for Unicode emoji
    if score <= 2:
        strength = "\u274c Weak Password"
    elif score in [3,4]:
        strength = "\u26A0\uFE0F Medium Password"
    else:
        strength = "\u2705 Strong Password"

    #Display the password strength and score
    result = f"Password strength: {strength} (score: {score}/5)"
    if recommendations:
        result += "\nRecommendations:"
        for r in recommendations:
            result += f"\n - {r}"
    return result, strength

#Prevent automatically running if imported
#Also incorporates a while True loop to prompt user to try again until strong.
if __name__ == "__main__":
    while True:
        user_input = input("Enter a password to check: ")
        result, strength = password_strength(user_input)
        print(result)

        if "Strong" in strength:
            print("\U0001F389 Congratulations! Your password is strong!!")
            break
        else:
            print("Try again.\n")
    

        
