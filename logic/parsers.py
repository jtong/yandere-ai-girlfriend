def parse_action(message):
    starter = message.find("Action:") + len("Action:")
    ender = message.find("\n", starter)
    if ender == -1:
        ender = len(message)
    return message[starter:ender].strip()


def parse_action_input(message):
    if message.find("ActionInput:") != -1:
        return message[message.find("ActionInput:") + len("ActionInput:"):].strip()
    else:
        return None


def parse_after_prefix(message, prefix):
    if message.find(prefix) != -1:
        return message[message.find(prefix) + len(prefix):].strip()
    else:
        return None
