#!/usr/bin/ruby

class Day02
  def get_strategy_guide (filename)
    lines = File.read(filename).to_s
    guide = lines.split("\n").map{|line| line.split(" ")}

    return guide
  end

  def decode (column)
    codes = {'A':'rock', 'B':'paper', 'C':'scissors', 'X':'rock', 'Y':'paper', 'Z':'scissors'}
    return codes[column.to_sym]
  end

  def apply_rules (my_choice, opponent_choice)
    rules = {'rock': {'rock':'tie', 'paper': 'lose', 'scissors':'win'}, 'paper': {'rock':'win', 'paper':'tie', 'scissors':'lose'}, 'scissors': {'rock':'lose', 'paper':'win', 'scissors':'tie'}}
    
    return rules[my_choice.to_sym][opponent_choice.to_sym]
  end

  def calculate_round (round)
    values = {'rock': 1, 'paper':2, 'scissors':3, 'lose':0, 'tie':3, 'win':6}

    opponent_choice = decode(round[0].to_sym)
    my_choice = decode(round[1].to_sym)

    outcome = apply_rules(my_choice, opponent_choice)
    score = values[my_choice.to_sym] + values[outcome.to_sym]

    return score
  end

  def calculate_score (guide)
    score = 0

    guide.each do |line|
      score += calculate_round(line)
    end

    return score
  end

end

if __FILE__ == $0    
  day2 = Day02.new
  guide = day2.get_strategy_guide('inputs/realinput02.txt')
  score = day2.calculate_score(guide)

  print "Part 1:\n"
  print score.to_s + "\n"
end
