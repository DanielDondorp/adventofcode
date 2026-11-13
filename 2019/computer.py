import numpy as np

class Computer:
    def __init__(self):
        pass

    def intcode(self, program):
        current_index = 0
        while True:
            # print(f"current_index: {current_index} ")
            opcode =  program[current_index]
            if opcode == 99: #99 signals immediate program halt
                return program
            else:
                #get value d1, value d2 and the destination from the program
                d1, d2, dest = program[current_index+1:current_index+4]
                if opcode ==1: #opcode one signals addition of d1 and d2, and stores the result in dest by overwriting the value that is there
                    program[dest] = program[d1]+program[d2]
                elif opcode ==2: #opcode 2 signals multiplication of d1 and d2, store result in dest
                    program[dest] = program[d1]*program[d2]
                else:
                    raise Exception(f"Unknown opcode {opcode}!")
            current_index += 4 # go to the next opcode