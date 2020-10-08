def uncover_hydra(communications, fury):
    messages = dict()

    for cmnt in communications:
        _parse_communication(cmnt, messages)

    print(_find_hydra_agents(messages, fury))

def _parse_communication(cmnt, messages):
    msg = cmnt.split(':')
    sender = msg[0].strip()
    receivers = [receiver.strip() for receiver in msg[1].split(',')]
    messages[sender] = receivers


def _find_hydra_agents(agents_msg, fury):
    hydra, shield_agents, agents = set(), set(), [fury]

    while len(agents) > 0:
        current = agents.pop()
        shield_agents.add(current)

        if current in agents_msg:
            for agent in agents_msg[current]:
                if agent not in shield_agents:
                    agents.append(agent)

 
    for sender in agents_msg.keys():
        if sender not in shield_agents:
            hydra.add(sender)

        for receiver in agents_msg[sender]:
            if receiver not in shield_agents:
                hydra.add(receiver)

    return hydra


communication = ["Nick Fury : Tony Stark, Maria Hill, Norman Osborn",
                 "Hulk : Tony Stark, HawkEye, Rogers",
                 "Rogers : Thor",
                 "Tony Stark: Pepper Potts, Nick Fury",
                 "Agent 13 : Agent-X, Nick Fury, Hitler",
                 "Thor: HawkEye, BlackWidow",
                 "BlackWidow:Hawkeye",
                 "Maria Hill : Hulk, Rogers, Nick Fury",
                 "Agent-X : Agent 13, Rogers",
                 "Norman Osborn: Tony Stark, Thor"]

uncover_hydra(communication, "Nick Fury")