#title and background
print()
print('TEXT ADVENTURE GAME')
print()
print('Backstory: The year is 1899 and you are currently living in the New Austin territory. Your')
print('name is Arthur Morgan and you are currently part of a small gang that you have been with for')
print('a few years now. There has been contention stiring amoung the gang about money and about')
print('choices that the gang leader Dutch has made. Everyone is on edge because they have been ')
print('running from the law. Now it is up to you to determine the fate of Arthur and the rest of')
print('the gang. Remember you need to keep an eye on your health, karma, and money. This will affect')
print('the story.')
print()
print('MAIN CHARACTERS: Arthur Morgan, Dutch Vanderlin, John Marston, Molly Ohern, Sadie Adler')
#stats
health = 3
karma = 0
money = 500

#scenario 1
print('STATS:')
print(f'HEALTH: {health}')
print(f'KARMA: {karma}')
print(f'MONEY: ${money}')
print('You wake up at camp and start to head out when you are stopped by a man by the name of ')
print('Straus. He is a german immigrant that joined the gang because it provided him a place to ')
print('stay and food to eat. He is in charge of the accounting for the camp and he tells you that')
print('he needs help collecting some debt of people whom the gang lended money to. do you help him?')
scene_1 = input('HELP / LEAVE : ')
print()
#scene 1 help
if scene_1.upper() == 'HELP':
    print('You decide to help Straus out, but you realize that the people that you are collecting')
    print('from are very desperate and can hardly pay. You get the money, but it certainley')
    print('does not make you look very good to others.')
    karma = karma - 1
    money = money + 100
#scene 1 leave
elif scene_1.upper() == 'LEAVE':
    print('You decide that it would be best if you not take the job because you do not feel right')
    print('about the job. You tell Straus that you can not take the job. Other people in the camp')
    print('notice what you have done and respect your moral character that you have shown.')
    karma = karma + 1
#scene 1 nothing
else:
    print('You forget to make a choice and do nothing.')
    print(f'HEALTH: {health}')
    print(f'KARMA: {karma}')
    print(f'MONEY: ${money}')

#Scenario 2
print()
print('Tensions build in camp and the gang finds out that there has been a spy in the camp who has')
print('feeding information to the Federal agents. Molly Ohern then stumbles into camp clearly drunk')
print('and continue to tell everyone that it was her that was feeding the Feds information. She says')
print('that she did it because of the choices that Dutch has been making for the gang. Everybody breaks')
print('into an argument and people start taking sides. On one hand, Dutch thinks that she should be')
print('killed for betraying the gang, but on the other hand John thinks that this was a result of poor')
print('choices by Dutch and that there needs to be changes. should you side with John or Dutch?')
scene_2 = input('DUTCH / JOHN : ')
print()
#scene 2 dutch
if scene_2.upper() == 'DUTCH':
    print('You choose to side with Dutch but others in the camp disagree with your decision. As a result')
    print('of your decision, the other Gang members do not trust you as much. The quarell ends with John')
    print('being kicked out of the camp. The gang members are not happy with you but Dutch trust you more.')
    karma = karma - 2
    money = money + 400
    print(f'HEALTH: {health}')
    print(f'KARMA: {karma}')
    print(f'MONEY: ${money}')
    print()
    print('The next day Dutch comes to you with money for you to reward you for helping him out. He also ')
    print('tells you about his plans for the gang in the future. Dutch is planning on robbing a bank in the')
    print('nearby town of Blackwater with a small team and he wants you to help him. He asks for your advice')
    print('on the bank job. He wants to know if it would be better to go in fast with guns and overwhelm the')
    print('tellers or if you should go in quietly to avoid detection. Should you go in loud or quiet?')
    scene_2_1 = input('LOUD / QUIET : ')
    print()
    #Scene 2 choice 1 Loud
    if scene_2_1.upper() == 'LOUD':
        print('You manage to overwhelm the tellers and control the rest of the civilians in the bank long enough')
        print('to take all of the money your gang can carry. You escape the bank on horseback and make it back to')
        print('camp with all of the money from the job.')
        money = money + 1500
        print(f'HEALTH: {health}')
        print(f'KARMA: {karma}')
        print(f'MONEY: ${money}')
    #scene 2 choice 1 Quiet
    elif scene_2_1.upper() == 'QUIET':
        print('You decide to try to sneak into the bank undetected at nightime. You find a window on the side and break')
        print('it. A nearby deputy hears the noise and rushes towards you to find out what happened. One of the gang')
        print('members panics and shoots him. The job is a bust and you all flee the scene and head back to camp.')
        print(f'HEALTH: {health}')
        print(f'KARMA: {karma}')
        print(f'MONEY: ${money}')
    #scene 2 choice 1 nothing
    else:
        print('You choose not to do anything and forget about the bank heist idea. Life goes on.')
#scene 2 choice 2
elif scene_2.upper() == 'JOHN':
    print('You side with John. Dutch has gotten out of control and it is time for someone to do something.')
    print('You confront Dutch and tell him that although Molly was out of line, She is right about Dutch.')
    print('You tell him that he has been making decisions that have been hurting the camp and the only thing')
    print('he seems concerened with is himself. You then ask him to leave the camp. Suddenly Dutch pulls his')
    print('gun and shoots you in the shoulder, knocking you to the ground. The gang retaliates and fires back')
    print('at Dutch, but he is able to escape the camp and the Gang. You are badly damaged from the wound, but')
    print('the gang respects you for what you did.')
    health = health - 2
    karma = karma + 3
    print(f'HEALTH: {health}')
    print(f'KARMA: {karma}')
    print(f'MONEY: ${money}')
    print()
    print('Now you are left with a few problems. You are badly damaged and you have no leader of the gang. Without')
    print('direction, people are uncertain of the future of the group. You decide that the best option is for the ')
    print('gang to get enough money so that they can move somewhere safe. You discuss this together and people come ')
    print('up with 2 possible solutions to getting money. The first being that you could follow and capture some')
    print('large bounties that have been put out on some high risk individuals. This way you be able to keep unwanted')
    print('attention from the law caused by robbing or stealing the money. The other option would be to steal some')
    print('large bonds that are stored at a Oil refinery building nearby. Should you go for the bounty or the bonds?')
    scene_2_john = input('BOUNTY / BONDS : ')
    print()
    #scene 2 choice 2 Bounty
    if scene_2_john.upper() == 'BOUNTY':
        print('You choose to avoid problems with the law by hunting for bounties instead. Everyone agrees that it would')
        print('be best to avoid problems and still get some honest money. People are happy and you get a little money too.')
        karma = karma + 1
        money = money + 500
        print(f'HEALTH: {health}')
        print(f'KARMA: {karma}')
        print(f'MONEY: ${money}')
    #scene 2 choice 2 bonds
    elif scene_2_john.upper() == 'BONDS':
        print('You take a little bit of risk and choose to try to steal the bonds. You sneak into the refinery and as you head')
        print('up to the office, one of the gang members gets shot and falls down the stairs. You retaliate and shoot he killer')
        print('and look at your deceased gang members and see that it is Charles. Following that you go to the office and get the')
        print('bonds. You get the money, but everyone is sad about Charles and blame you for his death.')
        karma = karma - 1
        money = money + 1000
        print(f'HEALTH: {health}')
        print(f'KARMA: {karma}')
        print(f'MONEY: ${money}')
    #scene 2 choice 2 nothing
    else:
        print('You choose to do nothing and you continue on with life.')
#scene 2 nothing
else: 
    print('You cannot decide who to help and in the heat of the argument Dutch and John shoot at eachother with you in the crossfire.')
    print('You recieve fatal wounds and die.')
    health = health - 3

#conclusion
if health >= 1:
    print()
    print('Now you come to an important decision. You need to escape and leave the area before it is too late and the Federal')
    print('agents come. You have 3 options as you see it. The first is that you can buy a riverboat to escape to a tropical')
    print('island somewhere far away: (REQUIRES : 2500 DOLLARS). The next is you could talk to some of the local indian tribes')
    print('and escape further north into reservation land : (REQUIRES 5 KARMA). The final option is you could try your luck and')
    print('escape to the west on horseback. What should you do?')
    print('Listed bellow is your current stats:')
    print(f'HEALTH: {health}')
    print(f'KARMA: {karma}')
    print(f'MONEY: ${money}')
    end = input('BOAT / NORTH / WEST : ')
    print()
    #conclusion boat
    if end.upper() == 'BOAT' and (money >= 2500):
        print('You escape with your gang on boat! You all escape to Tahiti, where you are happy. (MONEY ENDING)')
    #conclusion karma
    elif end.upper() == 'NORTH' and (karma >= 5):
        print('You escape to the north and take refuge in indian reservation land. There you all thrive and build')
        print('a strong relationship with the local tribes. (KARMA ENDING)')
    #conclusion horse
    elif end.upper() == 'WEST':
        print('You and your gang starts heading west but are ambushed by federal agents. You manage to escape, but')
        print('you lose everyone you care about.')
        #conclusion nothing
    else:
        print('You and your gang are ambushed by federal agents and are  all captured. : GAME OVER')
else:
    print('Game over')
print()
