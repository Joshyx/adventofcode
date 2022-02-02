DAYS_TO_SIMULATE = 80       #80 for part 1, 256 for part 2

class Lanternfish:
    daysLeftToReproduce:int
    reproductionDays:int

    def __init__(self, daysToReproduce):
        self.reproductionDays = daysToReproduce
        self.daysLeftToReproduce = self.reproductionDays + 2

    def update(self):
        if not self.canBeUpdated():
            self.daysLeftToReproduce -= 1
            return
        
        self.daysLeftToReproduce = 6

    def canBeUpdated(self):
        return self.daysLeftToReproduce < 1

    def __str__(self):
        return f"Lanternfish: {self.daysLeftToReproduce}"

def main():
    input_string = ''

    with open('input.txt', 'r') as textfile:
        input_string = textfile.read()
    input_array = input_string.split(',')

    fishlist = []

    for day in input_array:
        fish = Lanternfish(int(day) - 1)
        if fish != None:
            fishlist.append(fish)

    for i in range(DAYS_TO_SIMULATE - 1):
        for fish in fishlist:
            if fish.canBeUpdated():
                fishlist.append(Lanternfish(7))
            fish.update()
        print(f"{i / 257 * 100}%")
    print("100%")
    
    print('\nDONE')
    print(len(fishlist))

if __name__ == "__main__":
    main()
