require 'test/unit'
require 'code/day10'

class Part1 < Test::Unit::TestCase
  def test_get_input
    day10 = Day10.new

    input = day10.get_input('inputs/testinput10.txt')[1]
    expected = ['addx', -11]

    assert_equal expected, input
  end

  def test_execute
    day10 = Day10.new
    state = [1, 1]
    instruction = ['noop', 0]

    state = day10.execute(instruction, state)
    cycle = state[1]
    expected = 2
    assert_equal expected, cycle

    instruction = ['addx', 3]
    state = day10.execute(instruction, state)
    expected = [4, 4]
    assert_equal expected, state

    instruction = ['addx', -5]
    state = day10.execute(instruction, state)
    expected = [-1, 6]
    assert_equal expected, state
  end

  def test_run_program
    day10 = Day10.new
    instructions = day10.get_input('inputs/testinput10.txt')
    check_signal_at = (0..5).to_a.map{|x| x * 40 + 20}
    
    signal_strength = day10.run_program(instructions, check_signal_at)
    # expected = [420, 1140, 1800, 2940, 2880, 3960]
    expected = 13140
    assert_equal expected, signal_strength
  end
end
