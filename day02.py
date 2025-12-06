def compute(program, noun, verb):

    program[1] = noun
    program[2] = verb

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
    with open("inputs/day02", "r", encoding="utf-8-sig") as input_file:
        program = [int(code) for code in input_file.read().split(',')]

    print("-----DAY 02-----")
    print("Solutions:")
    print(f'Part1: {compute(program.copy(), 29, 2)}')

    for noun in range(100):
        for verb in range(100):
            if compute(program.copy(), noun, verb) == 19690720:
                print(f'Part2: {100 * noun + verb}')