def day02_1(path):
    with open(path, "r", encoding="utf-8-sig") as input_file:
        program = [int(code) for code in input_file.read().split(',')]
    program[1] = 12
    program[2] = 2

    for i in range(0, len(program), 4):
        opcode, arg1, arg2, res = program[i:i+4]
        match opcode:
            case 1:
                program[res] = program[arg1] + program[arg2]
            case 2:
                program[res] = program[arg1] * program[arg2]
            case 99:
                break
            case _:
                raise ValueError(f"THERE IS NO {opcode}! EVERYTHING IS ON FIRE!!")
    return program[0]



if __name__ == '__main__':
    print("-----DAY 02-----")
    print("Solutions:")
    print(f'Part1: {day02_1("inputs/day02")}')