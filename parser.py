data = list(set())

def parse():

    with open("requirements.txt", "r", newline="\n") as f:
        content = f.read()
        clean = content.splitlines()

        for item in clean:
            data.append(item)

    return data

if __name__ == "__main__":
    parse()

