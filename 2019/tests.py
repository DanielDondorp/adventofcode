import pytest
from computer import Computer
import builtins

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


def test_input_program(monkeypatch):
    """tests opcode 3, which takes an input and writes it to a destination"""
    monkeypatch.setattr(builtins, 'input', lambda x: 50)
    cpu = Computer()
    # ponytail: [3,0,99] stores input at addr 0 then hits halt
    output = cpu.intcode([3, 0, 99])
    assert output == [50, 0, 99]




    