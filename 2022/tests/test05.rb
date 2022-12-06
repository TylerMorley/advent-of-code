require 'test/unit'
require 'code/day05'

class Part1 < Test::Unit::TestCase
  def test_get_assignments
    day5 = Day05.new

    assignments = day5.get_input('inputs/testinput05.txt')
    expected = [[[nil, 'D', nil],
                 ['N', 'C', nil],
                 ['Z','M', 'P']
                ],
                [[1, 2, 1],
                 [3, 1, 3],
                 [2, 2, 1],
                 [1, 1, 2]
                ]
               ]

    assert_equal expected, assignments
  end

  def test_refine_stacks
    day5 = Day05.new
    input = "    [D]    "

    stacks = day5.refine_stacks(input)
    expected = [nil, 'D', nil]
    assert_equal expected, stacks

    input2 = "[N] [C]    "
    stacks = day5.refine_stacks(input2)
    expected = ['N', 'C', nil]
    assert_equal expected, stacks

    input3 = "[Z] [M] [P]"
    stacks = day5.refine_stacks(input3)
    expected = ['Z', 'M', 'P']
    assert_equal expected, stacks
  end

  def test_refine_crate
    day5 = Day05.new

    input = [" ", " ", " ", "  "]
    output = day5.refine_crate(input)
    expected = nil
    assert_equal expected, output

    input2 = ["[", "D", "]", " "]
    output = day5.refine_crate(input2)
    expected = 'D'
    assert_equal expected, output
  end

  def test_refine_procedure
    day5 = Day05.new
    input = "move 1 from 2 to 1"

    procedure = day5.refine_procedure(input)
    expected = [1, 2, 1]
    assert_equal expected, procedure

    input2 = "move 3 from 1 to 3"
    input3 = "move 2 from 2 to 1"
    input4 = "move 1 from 1 to 2"
  end

  def test_to_stacks
    day5 = Day05.new
    input = [[nil, 'D', nil],
             ['N', 'C', nil],
             ['Z','M', 'P']
            ]
    stacks = day5.to_stacks(input)
    expected = [['Z', 'N'],
                ['M', 'C', 'D'],
                ['P']
               ]

    assert_equal expected, stacks
  end

  def test_execute_step
    day5 = Day05.new
    input = [['Z', 'N'],
             ['M', 'C', 'D'],
             ['P']
            ]
    step1 = [1, 2, 1]
    output = day5.execute_step(input, step1)
    expected = [['Z', 'N', 'D'],
                ['M', 'C'],
                ['P']
               ]
    assert_equal expected, output
  end

  def test_execute_procedure
    day5 = Day05.new
    stacks = [['Z', 'N'],
              ['M', 'C', 'D'],
              ['P']
             ]
    procedure = [[1, 2, 1],
                 [3, 1, 3],
                 [2, 2, 1],
                 [1, 1, 2]
                ]
    expected  = [['C'],
                 ['M'],
                 ['P', 'D', 'N', 'Z']
                ]
    output = day5.execute_procedure(stacks, procedure, 1)
    assert_equal expected, output
  end

  def test_get_top_crates
    day5 = Day05.new
    input = [['C'],
             ['M'],
             ['P', 'D', 'N', 'Z']
            ]
    expected = 'CMZ'
    output = day5.get_top_crates(input)
    assert_equal expected, output
  end
end  

class Part2 < Test::Unit::TestCase
  def test_execute_step_2
    day5 = Day05.new
    input = [['Z', 'N'],
             ['M', 'C', 'D'],
             ['P']
            ]
    step1 = [2, 2, 1]
    output = day5.execute_step_2(input, step1)
    expected = [['Z', 'N', 'C', 'D'],
                ['M'],
                ['P']
               ]
    assert_equal expected, output
  end

  def test_execute_procedure_2
    day5 = Day05.new
    input = [['Z', 'N'],
             ['M', 'C', 'D'],
             ['P']
            ]
    procedure = [[1, 2, 1],
                 [3, 1, 3],
                 [2, 2, 1],
                 [1, 1, 2]
                ]
    expected = [['M'],
                ['C'],
                ['P', 'Z', 'N', 'D']
               ]
    output = day5.execute_procedure(input, procedure, 2)
    assert_equal expected, output
  end
end
