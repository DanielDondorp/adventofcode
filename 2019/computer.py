import numpy as np

class Computer:
    def __init__(self):
        self.log = []
            # set how many parameters need to be read from the program for a given opcoode, so we can get params based on the opcode
            self.N_READ_PARAMS = {1: 2, 
                     2: 2, 
                     3: 0, 
                     4: 1, 
                     5: 2, 
                     6: 2, 
                     7: 2, 
                     8: 2, 
                     99: 0}

    def parse_opcode(self, opcode):
        if abs(opcode) < 10:
            return opcode, [0,0,0] #all params are 0 --> position mode
        else:
            opcode = str(opcode)
            #pad to len 5
            while len(opcode) < 5:
                opcode = "0"+opcode
            #split into opcode and parameter instructions
            params = [int(x) for x in list(opcode[:3])[::-1]]
            opcode = int(opcode[-2:])
            print(f"{opcode=}, {params=}")
            return opcode, params
            


    def get_values_from_params(self, program, current_index, params):
        vals = []
        for i, param in enumerate(params):
            val_index = current_index+i+1
            if param == 1:
                vals.append(program[val_index])
            else:
                index = program[val_index]
                vals.append(program[index])
        print(vals)
        return vals

    def log_output_value(self, value):
        print(f"> {value}")
        self.log.append(value)
    
    def intcode(self, program):
        current_index = 0
        while True:
            opcode, params = self.parse_opcode(program[current_index])
            if opcode == 99: #99 signals immediate program halt
                return program
            vals = self.get_values_from_params(program, current_index, params[:self.N_READ_PARAMS[opcode]])
            if opcode == 1: #opcode one signals addition of d1 and d2, and stores the result in dest by overwriting the value that is there
                dest= program[current_index+3]
                program[dest] = vals[0] + vals[1]
                current_index += 4
            elif opcode == 2: #opcode 2 signals multiplication of d1 and d2, store result in dest
                dest= program[current_index+3]
                program[dest] = vals[0] * vals[1]
                current_index += 4
            elif opcode == 3: #takes an integer input and stores it to the index 
                d1 = program[current_index+1]
                input_value = int(input("computer requests integer input:"))
                program[d1] = input_value
                current_index += 2
            elif opcode == 4: #writes output to log
                self.log_output_value(vals[0])
                current_index += 2
            elif opcode == 5: 
                #if first value nonzero, go to index of second value
                if vals[0] != 0:
                    current_index = vals[1]
                else:
                    current_index += 3
            elif opcode == 6:
                if vals[0] == 0:
                    current_index = vals[1]
                else:
                    current_index += 3
            elif opcode == 7:
                dest= program[current_index+3]
                if vals[0] < vals[1]:
                    program[dest] = 1
                else:
                    program[dest] = 0
                current_index += 4
            elif opcode == 8:
                dest= program[current_index+3]
                if vals[0] == vals[1]:
                    program[dest] = 1
                else:
                    program[dest] = 0
                current_index += 4
            else:
                raise Exception(f"Unknown opcode {opcode}!")