require 'test/unit'
require 'code/day01'

class Part1 < Test::Unit::TestCase
  def test_get_elves
    day_one = Day01.new
    elves = day_one.get_elves('inputs/testinput01.txt')
    
    expected_len = 5
    assert_equal expected_len, elves.length

    assert_equal 3, elves[0].length
    assert_equal 2, elves[2].length
  end

  def test_get_calories
    elves = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]

    day_one = Day01.new
    calories = day_one.get_calories(elves)

    exp_length = 5
    assert_equal exp_length, calories.length
  end

  def test_get_calories_top1
    day_one = Day01.new
    input_calories = [6000, 4000, 11000, 24000, 10000]

    top_calories = day_one.get_calories_top1(input_calories)
 
    expected = 24000
    assert_equal expected, top_calories
  end
end

class Part2 < Test::Unit::TestCase
  def test_get_calories_top3
    input_calories = [6000, 4000, 11000, 24000, 10000]
    day_one = Day01.new

    top_three = day_one.get_calories_top3(input_calories)

    expected = 45000
    assert_equal expected, top_three
  end
end
