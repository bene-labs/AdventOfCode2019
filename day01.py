def day01_part1(path):
    total_fuel_required = 0
    for model_mass in [int(mass) for mass in open(path, "r", encoding="utf-8-sig").read().splitlines()]:
        total_fuel_required += model_mass // 3 - 2
    return total_fuel_required

def day01_part2(path):
    total_fuel_required = 0
    for model_mass in [int(mass) for mass in open(path, "r", encoding="utf-8-sig").read().splitlines()]:
        fuel_to_add = model_mass // 3 - 2
        while fuel_to_add > 0:
            total_fuel_required += fuel_to_add
            fuel_to_add = fuel_to_add // 3 - 2
    return total_fuel_required

if __name__ == '__main__':
    print("-----DAY 01-----")
    print("Solutions:")
    print(f'Part1: {day01_part1("inputs/day01")}')
    print(f'Part2: {day01_part2("inputs/day01")}')