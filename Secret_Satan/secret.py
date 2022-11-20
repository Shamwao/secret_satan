import random

givers = [
    'Dave',
    'Chris',
    'Jenny',
    'Dustin',
    'Lyndsay',
    'Mac',
    'Claire',
    'Jason'
]

receivers = givers[:]

excludes = {
    'Dave':'Chris',
    'Jenny':'Dustin',
    'Lyndsay':'Mac',
    'Claire':'Jason'
}


def secretSatan():
    result = []
    restart = True
    while restart == True:
        for i in range(len(givers)):
            restart = False
            giver = givers[i]
            receiver=random.choice(receivers)
            #if giver and receiver are the same OR are on the exclusion list
            if giver == receiver or receiver in excludes and giver == excludes[receiver]:
                restart = True
                break
            else:
                result.append(giver + ' is buying for ' + receiver)
                receivers.remove(receiver)
    if len(receivers) == 0:         
        for r in result:
            print(r)
secretSatan()


