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
    mode = 'opp'
    choice = day2.decode(column, mode)
    expected = 'rock'

    assert_equal expected, choice

    column2 = 'Y'
    mode2 = 'me_1'
    choice2 = day2.decode(column2, mode2)
    expected2 = 'paper'

    assert_equal expected2, choice2
  end

  def test_apply_rules
    day2 = Day02.new

    my_choice = 'rock'
    opponent_choice = 'scissors'
    outcome = day2.apply_rules(my_choice, opponent_choice, '1')
    expected = 'win'

    assert_equal expected, outcome
  end

  def test_get_score
    day2 = Day02.new
    
    my_choice1 = 'paper'
    outcome1 = 'win'
    expected1 = 8
    score1 = day2.get_score(my_choice1, outcome1)
    assert_equal expected1, score1

    my_choice2 = 'rock'
    outcome2 = 'lose'
    expected2 = 1
    score2 = day2.get_score(my_choice2, outcome2)
    assert_equal expected2, score2
  end

  def test_calculate_round
    day2 = Day02.new
    round = ['A', 'Y']

    score = day2.calculate_round(round, '1')

    expected = 8
    assert_equal expected, score
  end

  def test_calculate_score
    day2 = Day02.new
    guide = [['A', 'Y'], ['B', 'X'], ['C', 'Z']]

    score = day2.calculate_score(guide, '1')

    expected = 15
    assert_equal expected, score
  end
end

class Part2 < Test::Unit::TestCase
  def test_decode_2
    day2 = Day02.new
    column = 'Y'
    mode = 'me_2'
    choice = day2.decode(column, mode)
    expected = 'tie'

    assert_equal expected, choice
  end

  def test_apply_rules_2
    day2 = Day02.new
    
    my_choice = 'tie'
    opponent_choice = 'scissors'
    outcome = day2.apply_rules(my_choice, opponent_choice, '2')
    expected = 'scissors'

    assert_equal expected, outcome
  end

  def test_calculate_round_2
    day2 = Day02.new

    round1 = ['A', 'Y']
    score = day2.calculate_round(round1, '2')
    expected = 4
    assert_equal expected, score

    round2 = ['B', 'X']
    score = day2.calculate_round(round2, '2')
    expected = 1
    assert_equal expected, score
    end

  def test_calculate_score_2
    day2 = Day02.new
    guide = [['A', 'Y'], ['B', 'X'], ['C', 'Z']]

    score = day2.calculate_score(guide, '2')

    expected = 12
    assert_equal expected, score
  end
end
