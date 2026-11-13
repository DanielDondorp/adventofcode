import pytest
from computer import Computer

@pytest.mark.parametrize("program, expected", [([1,0,0,0,99], [2,0,0,0,99]), #tests opcode 1, add index 0 + index 0, store at index zero: 1+1=2
                                               ([2,3,0,3,99], [2,3,0,6,99]), #tests opcode 2. multiply index 3 with index 0, store at 3: 3*2 = 6
                                               ([2,4,4,5,99,0], [2,4,4,5,99,9801]), #tests using the exit-opcode as input for multiplication
                                               ([1,1,1,4,99,5,6,0,99], [30,1,1,4,2,5,6,0,99]), #combining opcodes
                                               ([1,9,10,3,2,3,11,0,99,30,40,50], [3500,9,10,70,2,3,11,0,99,30,40,50]), #day 2 base program test
                                              ])
def test_base_programs(program, expected):
    cpu = Computer()
    output = cpu.intcode(program)
    assert output == expected

# def test_addition(cpu):
#     """tests opcode 1, add index 0 + index 0, store at index zero: 1+1=2"""
#     program = [1,0,0,0,99] 
#     output = cpu.intcode(program)
#     assert output == [2,0,0,0,99]

# def test_multiplication(cpu):
#     """tests opcode 2. multiply index 3 with index 0, store at 3: 3*2 = 6 """
#     program = [2,3,0,3,99]
#     output = cpu.intcode(program)
#     assert output == [2,3,0,6,99]

# def test_multiplication_2(cpu)
#     """tests using the exit-opcode as input for multiplication"""
#     program = [2,4,4,5,99,0]
#     output = cpu.intcode(program)
    


    