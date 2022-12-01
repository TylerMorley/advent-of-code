require 'test/unit'
require 'code/day01'

class Part1 < Test::Unit::TestCase
  def test_get_elves
    day_one = Day01.new
    elves = day_one.get_elves('inputs/testinput01.txt')
    
    expected_len = 5
    assert_equal expected_len, elves.length

    assert_equal 3, elves[0].length
    assert_equal 1, elves[1].length
    assert_equal 2, elves[2].length
    assert_equal 3, elves[3].length
    assert_equal 1, elves[4].length
  end

  def test_get_calories
    elves = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]

    day_one = Day01.new
    calories = day_one.get_calories(elves)

    expected = 24000
    assert_equal expected, calories
  end
end
