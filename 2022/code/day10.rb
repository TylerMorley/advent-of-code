#!/usr/bin/ruby

class Day10
  def get_input (filename)
    input = File.read(filename).split("\n").map{|line| line.strip.split(' ')}
    input.map{|line| [line[0], line[1].to_i]}
  end

  def execute(instruction, state)
    xval = state[0]
    cycle = state[1]
    if instruction[0] == 'noop'
      cycle += 1
    elsif instruction[0] == 'addx'
      xval += instruction[1]
      cycle += 2
    end
    return [xval, cycle]
  end

  def run_program(instructions, check_signal_at)
    state = [1,1]
    signal_strength = Array.new
    instructions.each do |instr|
      xval = state[0]
      cycle = state[1]
      next_cycle = state[1] + 1

      if check_signal_at.include? cycle
        signal_strength.append(xval * cycle)
      elsif (instr[0] == 'addx') and (check_signal_at.include? next_cycle)
        signal_strength.append(xval * next_cycle)
      end
      state = execute(instr, state)
    end
    return signal_strength.sum
  end
end

if __FILE__ == $0    
  day10 = Day10.new
  instructions = day10.get_input('inputs/realinput10.txt')
  check_signal_at = (0..5).to_a.map{|x| x * 40 + 20}

  part1 = day10.run_program(instructions, check_signal_at)
  print "Part 1:\n"
  print part1.to_s + "\n"

  # knots2 = Array.new(10).map{|x| [0,0]}
  # part2 = day9.moves(knots2, input)[1]
  # print "Part 2:\n"
  # print part2.to_s + "\n"
end
