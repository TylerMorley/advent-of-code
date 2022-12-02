#!/usr/bin/ruby

class Day02
  def get_strategy_guide (filename)
    lines = File.read(filename).to_s
    guide = lines.split("\n").map{|line| line.split(" ")}

    return guide
  end

  def decode (column, mode)
    codes = nil

    if mode == 'opp'
      codes = {'A':'rock', 'B':'paper', 'C':'scissors'}
    elsif mode == 'me_1'
      codes = {'X':'rock', 'Y':'paper', 'Z':'scissors'}
    elsif mode == 'me_2'
      codes = {'X':'lose', 'Y':'tie', 'Z':'win'}
    end

    return codes[column.to_sym]
  end

  def apply_rules (my_choice, opponent_choice, mode)
    rules = {
      'rock': {'rock':'tie', 'paper': 'win', 'scissors':'lose'}, 
      'paper': {'rock':'lose', 'paper':'tie', 'scissors':'win'}, 
      'scissors': {'rock':'win', 'paper':'lose', 'scissors':'tie'}
    }
    
    output = nil

    if mode == '1'
      output = rules[opponent_choice.to_sym][my_choice.to_sym]
    elsif mode == '2'
      output = rules[opponent_choice.to_sym].key(my_choice).to_s
    end

    return output
  end

  def get_score (my_choice, outcome)
    values = {'rock': 1, 'paper':2, 'scissors':3, 'lose':0, 'tie':3, 'win':6}
    score = values[my_choice.to_sym] + values[outcome.to_sym]
    return score
  end

  def calculate_round (codes, mode)
    opponent_code = codes[0]
    my_code = codes[1]
    opponent_choice = decode(opponent_code, 'opp')

    my_choice = nil
    outcome = nil
    if mode == '1'
      my_choice = decode(my_code, 'me_1')
      outcome = apply_rules(my_choice, opponent_choice, mode)
    elsif mode == '2'
      outcome = decode(my_code, 'me_2')
      my_choice = apply_rules(outcome, opponent_choice, mode)
    end

    score = get_score(my_choice, outcome)
    return score
  end

  def calculate_score (guide, mode)
    score = 0

    guide.each do |line|
      score += calculate_round(line, mode)
    end

    return score
  end

end

if __FILE__ == $0    
  day2 = Day02.new
  guide = day2.get_strategy_guide('inputs/realinput02.txt')

  score1 = day2.calculate_score(guide, '1')
  print "Part 1:\n"
  print score1.to_s + "\n"

  score2 = day2.calculate_score(guide, '2')
  print "Part 2:\n"
  print score2.to_s + "\n"
end
