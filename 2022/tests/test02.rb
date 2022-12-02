require 'test/unit'
require 'code/day02'

class Part1 < Test::Unit::TestCase
  def test_get_strategy_guide
    day2 = Day02.new

    guide = day2.get_strategy_guide('inputs/testinput02.txt')
    
    expected = [['A', 'Y'], ['B', 'X'], ['C', 'Z']]
    assert_equal expected, guide
  end

  def test_decode
    day2 = Day02.new

    column = 'A'
    choice = day2.decode(column)
    expected = 'rock'

    assert_equal expected, choice
  end

  def test_apply_rules
    day2 = Day02.new

    my_choice = 'rock'
    opponent_choice = 'scissors'
    outcome = day2.apply_rules(my_choice, opponent_choice)
    expected = 'win'

    assert_equal expected, outcome
  end

  def test_calculate_round
    day2 = Day02.new
    round = ['A', 'Y']

    score = day2.calculate_round(round)

    expected = 8
    assert_equal expected, score
  end

  def test_calculate_score
    day2 = Day02.new
    guide = [['A', 'Y'], ['B', 'X'], ['C', 'Z']]

    score = day2.calculate_score(guide)

    expected = 15
    assert_equal expected, score
  end
end
