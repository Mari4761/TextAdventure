print("Welcome to the Vagina Power, to continue at anytime, press the space bar")

user = input(" ")

intro = '''You, the only surviving female doctor of your vilage, are in a desperate search of a cure for a life threatening disease named Duck Face Caseinate Influenza, which has brought your entire village a decreasing population. Your suspicions on where the cure is located is either through the nearby fields or the woods surrounding your area.
'''

if user == " ":
    print(intro)

print("type 'woods' to enter the woods or 'fields' to enter the fields")
location = input()

bad_end = "Try again by pressing the up arrow and hitting enter."

while True:
    if location == "woods":
        print("You slowly walk into the darkened woods, careful not to disturb any unknown, nearby wildlife. Despite all, you suddenly realized you startled a black mama bear, infuriating it in the process. You only have two choices: run away or play dead so that the bear will go away?")
        print("Type 'flight' to run or 'flop' to play dead")
        sit_1 = input()
        if sit_1 =="flop":
            print("Don't pretend to be dead when confronted by a black bear. You just died. FAILURE", bad_end)
        if sit_1=="flight":
            print("You scattered to a nearby tree and climbed up. The bear didn't seem to leave so now it's morning and you've spent the night on a tree branch.")
            print("You  climb down and continue wandering in search for the life-saving cure. You stumble upon a village that happens to carry a cure. They share it with you and you successfully deliver it to your sick people. VICTORY", bad_end)
        break
    elif location == "fields":
        print("It's getting icreasingly dark and you have to hurry back before nightfall. You run too quickly and you fall into a ditch, spraining your ankle in the process. Despite your sudden shock, you only have two options: Wait to be rescued or make a splint")
        sit_2= input()
        if sit_2 == "Wait to be rescued":
            print("After waiting for hours, you are finally rescued by stunning young woman who brings you back to the village. Soon you catch the disease, Duck Face Caseinate Influenza, and die. FAILURE", bad_end)
        if sit_2 == "Make a splint":
            print("Salvaging a random stick to make your splint, you find your way out of the ditch. You soon encounter a friendly doctor who coincidentally has the cure Duck Face Caseinate Influenza. You bring it back to your little village and cure all. VICTORY", bad_end)
        break
