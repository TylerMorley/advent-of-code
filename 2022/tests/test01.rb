require 'test/unit'
require 'code/day01'

class Part1 < Test::Unit::TestCase
  def test_get_elves
    day_one = Day01.new

    elves = day_one.get_elves('inputs/testinput01.txt')
    
    exp_length = 5
    assert_equal exp_length, elves.length
    expected = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]
    assert_equal expected, elves
  end

  def test_get_calories
    day_one = Day01.new
    elves = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]

    calories = day_one.get_calories(elves)

    exp_length = 5
    assert_equal exp_length, calories.length
    expected = [6000, 4000, 11000, 24000, 10000]
    assert_equal expected, calories
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
    day_one = Day01.new
    input_calories = [6000, 4000, 11000, 24000, 10000]

    top_three = day_one.get_calories_top3(input_calories)

    expected = 45000
    assert_equal expected, top_three
  end
end
